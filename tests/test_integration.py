"""Run against a real APK. Skipped unless APK_SENTINEL_SAMPLE_APK is set (see conftest.py)."""

from pathlib import Path

import pytest
from typer.testing import CliRunner

from apk_sentinel.cli import app
from apk_sentinel.loader import ApkLoadError, load_apk
from apk_sentinel.scanner import scan_apk

pytestmark = pytest.mark.integration


def test_loader_decodes_a_real_apk(sample_apk: Path) -> None:
    apk = load_apk(sample_apk)
    assert apk.manifest.package
    assert len(apk.sha256) == 64
    assert apk.dex_strings


def test_full_scan_has_no_analyzer_errors(sample_apk: Path) -> None:
    result = scan_apk(sample_apk)
    assert result.errors == []
    assert result.target.package


def test_cli_scan_runs(sample_apk: Path) -> None:
    result = CliRunner().invoke(app, ["scan", str(sample_apk)])
    assert result.exit_code == 0, result.output


def test_non_apk_is_rejected_cleanly(tmp_path: Path) -> None:
    bogus = tmp_path / "fake.apk"
    bogus.write_text("this is not a zip")
    with pytest.raises(ApkLoadError):
        load_apk(bogus)
