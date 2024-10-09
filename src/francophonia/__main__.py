import sys
from pathlib import Path

import uvicorn

# Automatically add the working directory (PYTHONPATH)
path = Path(__file__).parents[1].absolute()
sys.path.append(f"{path}")

from src.francophonia.app import app  # noqa: E402
from src.francophonia import logger  # noqa: E402


def main():
    """
    Main function to run the application.

    Raises:
        SystemExit: If the program is exited.

    Returns:
        int: The return code of the program.
    """
    # Get the arguments for the program
    arguments = " ".join(sys.argv[1:])

    # Add the user command to the logs (first is src path)
    logger.info(f"Arguments passed: {arguments}")

    try:
        uvicorn.run(app, host="0.0.0.0", port=8000)
    except KeyboardInterrupt as exception:
        logger.debug(f"Exiting the program: '{exception}'")


if __name__ == "__main__":
    main()
