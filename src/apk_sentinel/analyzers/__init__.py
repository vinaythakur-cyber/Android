"""Security checks. Each module exposes one :class:`Analyzer` subclass."""

from __future__ import annotations

from apk_sentinel.analyzers.base import Analyzer
from apk_sentinel.analyzers.manifest import ManifestAnalyzer


def default_analyzers() -> list[Analyzer]:
    """The analyzers that run on every scan, in report order."""
    return [ManifestAnalyzer()]


__all__ = ["Analyzer", "default_analyzers"]
