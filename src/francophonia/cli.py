import typer
from typer import Typer

from francophonia import logger

cli = Typer(no_args_is_help=True, pretty_exceptions_enable=False)


@cli.command()
def run(
    app: str = typer.Option("francophonia.app:app", envvar="APP", help="Application to launch."),
    host: str = typer.Option("localhost", envvar="HOST", help="Address on which the server should listen."),
    port: int = typer.Option(8000, envvar="PORT", help="Port on which the server should listen."),
):
    """
    Start the server with the given environment.

    Args:
        app (str): Application to launch.
        host (str): Host IP address of the server.
        port (int): Port number of host server.

    """
    logger.info(f"Starting the server with host: '{host}' and port: '{port}'")

    # Run the Gradio application with the given environment
    launch_app(
        app=app,
        host=host,
        port=port,
    )


def launch_app(
    app: str = "francophonia.app:app",
    host: str = "localhost",
    port: int = 8000,
    log_level: str = "info",
):
    """
    Launch the Gradio application with the given environment.

    Args:
        app (str): Application to launch.
        host (str): Host IP address of the server.
        port (int): Port number of host server.
        log_level (str): Logging level for the server.
    """
    import uvicorn

    uvicorn.run(
        app=app,
        host=host,
        port=port,
        log_level=log_level,
    )


if __name__ == "__main__":
    cli()
