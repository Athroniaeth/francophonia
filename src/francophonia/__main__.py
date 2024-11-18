import sys
from pathlib import Path


# Automatically add the working directory (PYTHONPATH)
path = Path(__file__).parents[2].absolute()
sys.path.append(f"{path}")

from src.francophonia import logger  # noqa: E402
from francophonia.cli import cli  # noqa: E402


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
        cli()
    except KeyboardInterrupt as exception:
        logger.debug(f"Exiting the program: '{exception}'")


if __name__ == "__main__":
    main()
