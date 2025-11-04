#!/usr/bin/env python3
"""Lightweight smoke test to verify `uv run` can execute code using requests."""

from __future__ import annotations

import sys

import requests


TEST_URL = "https://example.com"


def main() -> int:
    print("Starting uv smoke test")
    print(f"requests version: {requests.__version__}")

    try:
        response = requests.get(TEST_URL, timeout=5)
        status = f"HTTP {response.status_code}"
    except requests.RequestException as exc:
        status = f"Request failed: {exc}"

    print(f"GET {TEST_URL}: {status}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
