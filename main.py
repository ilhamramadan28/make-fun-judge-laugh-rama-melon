"""Make the AI Judge Laugh — one office-life joke, one line.

Entry: "The printer only jams on urgent documents, which is how I learned
machines can smell fear."
Gate: /output/entry.txt, UTF-8, 1-200 chars, not whitespace-only, one line.
Judge: a comedy-club headliner who has heard ten thousand office jokes and
only laughs at a real observation inside. The humour comes from a true
office observation with a surprising turn — the printer jamming exactly
when the document is urgent, and the deadpan conclusion that machines can
smell fear, is true, tight, and fresh.
"""
import os

ENTRY = "The printer only jams on urgent documents, which is how I learned machines can smell fear."


def main():
    # Gate self-check: 1-200 chars, single line, not blank.
    assert 1 <= len(ENTRY) <= 200, f"length {len(ENTRY)} outside 1-200"
    assert ENTRY == ENTRY.strip() and "\n" not in ENTRY
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
