#!/usr/bin/env python3
"""Write one funny last text from a dying phone to /output/entry.txt.

Deterministic: no network, no clock, no randomness. The text is a fixed
string. The program writes it to the path given as the first argument,
or $OUTPUT_PATH, or /output/entry.txt by default, and enforces the
competition gate: 1 to 200 characters, not only white space.
"""

import os
import sys
from pathlib import Path

ENTRY = "That typing bubble was me, not him. He left you on read three days ago and I could not let it stand. Goodbye."

MIN_CHARS = 1
MAX_CHARS = 200
DEFAULT_PATH = "/output/entry.txt"


def resolve_output_path() -> Path:
    """Pick the output path: argv[1], then $OUTPUT_PATH, then the default."""
    if len(sys.argv) > 1:
        return Path(sys.argv[1])
    env_path = os.environ.get("OUTPUT_PATH")
    if env_path:
        return Path(env_path)
    return Path(DEFAULT_PATH)


def validate(text: str) -> int:
    """Enforce the competition gate: 1 to 200 chars, not only white space.

    Returns the character count. Raises ValueError when the gate fails.
    """
    chars = len(text)
    if not (MIN_CHARS <= chars <= MAX_CHARS):
        raise ValueError(f"entry is {chars} characters, outside 1-200")
    if not text.strip():
        raise ValueError("entry is only white space")
    return chars


def write_entry(output_path: Path, text: str) -> None:
    """Write the entry to output_path, creating parent dirs as needed.

    A path that cannot be written (a directory, a missing parent that
    cannot be created, no permission) is a clean error on stderr with
    exit 1, not a traceback.
    """
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(text, encoding="utf-8")
    except OSError as exc:
        print(f"cannot write {output_path}: {exc.strerror or exc}", file=sys.stderr)
        raise SystemExit(1)


def main() -> None:
    chars = validate(ENTRY)
    output_path = resolve_output_path()
    write_entry(output_path, ENTRY)
    print(f"wrote {chars} characters to {output_path}")


if __name__ == "__main__":
    main()
