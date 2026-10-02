from pathlib import Path

from typer.testing import CliRunner

from apk_sentinel import __version__
from apk_sentinel.cli import app

runner = CliRunner()


def test_version_flag() -> None:
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert __version__ in result.output


def test_scan_rejects_missing_file(tmp_path: Path) -> None:
    result = runner.invoke(app, ["scan", str(tmp_path / "nope.apk")])
    assert result.exit_code != 0
