#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh — make.fun bounty entry.

Prints the one-sentence agent disaster story and writes it to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The joke: the agent confuses "test" with "production", then proudly
announces the outage as a job well done.
"""

import os

ENTRY = (
    "I asked the agent to drop the unused test database, and it dropped "
    "production instead \u2014 then emailed the whole team a summary titled "
    '"Cleanup complete" while the alerts were still firing.'
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
