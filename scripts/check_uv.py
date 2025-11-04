"""Simple connectivity check to validate `uv run` can execute dependencies."""

import sys

import requests


def main() -> None:
    response = requests.get("https://httpbin.org/get", timeout=10)
    response.raise_for_status()
    data = response.json()
    # Print a small summary so the caller sees we hit the network
    print("uv run ok; request to https://httpbin.org/get succeeded.")
    print(f"origin: {data.get('origin', 'unknown')}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"uv run failed: {exc}", file=sys.stderr)
        sys.exit(1)
