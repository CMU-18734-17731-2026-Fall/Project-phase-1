"""Verify that Git LFS materialized the course model checkpoint correctly."""

from __future__ import annotations

import hashlib
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CHECKPOINT = PROJECT_ROOT / "models" / "gpt2_phase1" / "model.safetensors"
EXPECTED_SIZE = 497_774_208
EXPECTED_SHA256 = "1a205d3e68c7997ace3cc2641c746f93cb14d6b1c2631b24c544430bd30bc83d"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as checkpoint_file:
        for chunk in iter(lambda: checkpoint_file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    if not CHECKPOINT.is_file():
        raise SystemExit(
            f"ERROR: checkpoint is missing: {CHECKPOINT}\n"
            "Run `git lfs install` followed by `git lfs pull`."
        )

    actual_size = CHECKPOINT.stat().st_size
    if actual_size != EXPECTED_SIZE:
        hint = ""
        with CHECKPOINT.open("rb") as checkpoint_file:
            header = checkpoint_file.read(42)
        if header == b"version https://git-lfs.github.com/spec/v1":
            hint = " The file is a Git LFS pointer, not the checkpoint."
        raise SystemExit(
            f"ERROR: checkpoint size is {actual_size:,} bytes; expected "
            f"{EXPECTED_SIZE:,}.{hint}\n"
            "Run `git lfs install` followed by `git lfs pull`."
        )

    actual_sha256 = sha256(CHECKPOINT)
    if actual_sha256 != EXPECTED_SHA256:
        raise SystemExit(
            "ERROR: checkpoint checksum does not match the published model.\n"
            f"Expected: {EXPECTED_SHA256}\n"
            f"Actual:   {actual_sha256}\n"
            "Delete the checkpoint and run `git lfs pull` again."
        )

    print(f"Checkpoint: {CHECKPOINT.relative_to(PROJECT_ROOT)}")
    print(f"Size:       {actual_size:,} bytes")
    print(f"SHA-256:    {actual_sha256}")
    print("Model checkpoint verification: PASS")


if __name__ == "__main__":
    main()
