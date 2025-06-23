"""Command-line interface."""
import click

from app.cli import run_cli


@click.command()
@click.version_option()
def main() -> None:
    run_cli()


if __name__ == "__main__":
    main()  # pragma: no cover
