#!/usr/bin/env python3
"""
pod-tools version information.

This file is the single source of truth for the package version.
It is updated automatically by tools/release.py.
"""

# Version format: MAJOR.MINOR.PATCH
VERSION = "0.1.5"
BUILD_DATE = "2026-06-01"


def get_version() -> str:
    return VERSION
