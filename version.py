#!/usr/bin/env python3
"""
podman-tools version information.

This file is the single source of truth for the package version.
It is updated automatically by tools/release.py.
"""

# Version format: MAJOR.MINOR.PATCH
VERSION = "0.1.2"
BUILD_DATE = "2026-05-28"


def get_version() -> str:
    return VERSION
