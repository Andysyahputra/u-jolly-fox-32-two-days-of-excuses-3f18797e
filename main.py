"""Two Days of Excuses — entry program.

Writes the one-line excuse to /output/entry.txt.
Deterministic: the same bytes on every run, stdlib only,
no network, no environment secrets, no files outside the repo.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

# The excuse, kept as its two clauses so the single absurd reason
# (a phantom time zone) stays readable in the source.
_CLAUSES = (
    "The deadline was missed because I confidently scheduled it "
    "for a time zone that does not exist,",
    "and the calendar agreed with me.",
)

ENTRY = " ".join(_CLAUSES)


def validate(text: str) -> str:
    """Enforce the competition gate: 1-200 chars, exactly one line."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} characters, must be 1-200")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main() -> None:
    entry = validate(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(entry + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
