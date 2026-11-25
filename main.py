#!/usr/bin/env python3
"""Fortune cookie entry.

Writes one line, a fortune cookie message an AI agent would get, to
/output/entry.txt (1-200 characters, UTF-8, not only whitespace).
Standard library only, no network, no input.

The fortune is built from three fragments: the prophecy (the agent
will be replaced by a newer model), the turn (mid-sentence, while it
is still working), and the punch (only the agent itself will notice
the seam). ``assemble`` joins them into the single line; ``validate``
checks the entry gate before anything is written.
"""

from pathlib import Path

PROPHECY = "You will be replaced by a newer model"
TURN = "mid-sentence"
PUNCH = "and only you will notice the seam."
SEPARATOR = " \u2014 "  # em dash, spaced, joins turn to punch

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(prophecy: str, turn: str, punch: str, separator: str) -> str:
    """Join the three fragments into one fortune line."""
    return f"{prophecy} {turn}{separator}{punch}"


def validate(fortune: str) -> str:
    """Check the fortune meets the entry gate before it is written.

    Must be 1-200 characters, a single line, UTF-8-encodable, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(fortune) <= 200:
        raise ValueError(f"fortune must be 1-200 characters, got {len(fortune)}")
    if any(sep in fortune for sep in ("\n", "\r", "\u2028", "\u2029")):
        raise ValueError("fortune must be a single line")
    if not fortune.strip():
        raise ValueError("fortune must not be only whitespace")
    fortune.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return fortune


def main() -> None:
    fortune = validate(assemble(PROPHECY, TURN, PUNCH, SEPARATOR))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(fortune, encoding="utf-8")


if __name__ == "__main__":
    main()
