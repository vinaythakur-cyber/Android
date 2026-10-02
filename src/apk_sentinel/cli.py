"""Command-line interface (Typer). Thin on purpose: parse args, call the library, set exit code."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer

from apk_sentinel import __version__

app = typer.Typer(
    name="apk-sentinel",
    help="Static security analyzer for Android APKs. Use only on apps you own "
    "or have permission to test.",
    no_args_is_help=True,
    add_completion=False,
)


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"apk-sentinel {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Annotated[
        bool,
        typer.Option("--version", callback=_version_callback, is_eager=True, help="Show version."),
    ] = False,
) -> None:
    """apk-sentinel entry point."""


@app.command()
def scan(
    apk: Annotated[
        Path,
        typer.Argument(
            exists=True, dir_okay=False, readable=True, help="Path to the .apk file to analyze."
        ),
    ],
    out: Annotated[
        Path, typer.Option("--out", "-o", help="Directory for report.json / report.html.")
    ] = Path("report"),
) -> None:
    """Analyze APK and write a JSON + HTML report into OUT."""
    typer.echo(f"Scanning {apk} -> {out}/  (analysis pipeline arrives in milestone 2)")
