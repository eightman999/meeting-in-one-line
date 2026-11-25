import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
LINE = "Decision: we ship it Friday, Priya owns the rollback plan, and nobody schedules a follow-up about this follow-up."


def main():
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n")


if __name__ == "__main__":
    main()
