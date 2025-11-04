"""Simple smoke test for the SiliconFlow embedding API."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv


API_URL = "https://api.siliconflow.cn/v1/embeddings"
ENV_KEY_NAME = "SF_TOKEN"
ENV_MODEL_KEY = "EMBED_MODEL"


def load_api_key() -> str:
    """Load API key from .env file."""
    env_file = Path(".env")
    load_dotenv(dotenv_path=env_file, override=False)
    if not env_file.exists():
        print("⚠️  .env file not found in project root.", file=sys.stderr)
    value = os.environ.get(ENV_KEY_NAME)
    if not value:
        raise RuntimeError(
            f"Environment variable {ENV_KEY_NAME} is missing. "
            "Ensure it is present in the .env file."
        )
    return value


def load_model_name() -> str:
    """Load embedding model from .env or fall back to default."""
    env_file = Path(".env")
    load_dotenv(dotenv_path=env_file, override=False)
    model = os.environ.get(ENV_MODEL_KEY)
    if not model:
        raise RuntimeError(
            f"Environment variable {ENV_MODEL_KEY} is missing. "
            "Ensure it is present in the .env file."
        )
    return model


def run_smoke_test(text: str) -> dict:
    """Call the embedding API and return the parsed JSON response."""
    api_key = load_api_key()
    model = load_model_name()
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "input": text,
    }
    response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
    response.raise_for_status()
    return response.json()


def main() -> None:
    text = "你好，这是一本书签摘要嵌入接口的连通性检查。"
    try:
        result = run_smoke_test(text)
    except Exception as exc:  # pragma: no cover - simple CLI feedback
        print(f"❌ Embedding API call failed: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc

    data = result.get("data", [])
    first_vector = data[0]["embedding"] if data else []
    print("✅ Embedding API call succeeded")
    print(f"- model: {result.get('model')}")
    print(f"- vector length: {len(first_vector)}")
    print(f"- prompt tokens: {result.get('usage', {}).get('prompt_tokens')}")
    print(f"- total tokens: {result.get('usage', {}).get('total_tokens')}")

    preview = first_vector[:5]
    print("- vector preview:")
    print(json.dumps(preview, indent=2))


if __name__ == "__main__":
    main()
