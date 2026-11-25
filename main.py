import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
LINE = "Approved: ship Friday, one owner, no follow-up meeting. If it breaks, we meet at the scene of the crime, not in a room about the room."


def main():
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n")


if __name__ == "__main__":
    main()
