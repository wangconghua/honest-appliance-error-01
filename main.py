#!/usr/bin/env python3
"""The Funniest Honest Appliance Error.

Writes one line of at most 200 characters to /output/entry.txt:
the funniest honest error message an appliance could show.

Gate (from the kit): /output/entry.txt must be UTF-8 text of
1 to 200 characters, not only white space. The judge's brief
adds, most important first: it must be an honest error message
an appliance could show; it must land a real joke, a surprise
or a twist; it must name a fault an appliance could plausibly
report, so the humour comes out of the truth of it; it must
sound like the appliance itself speaking, in its own flat,
put-upon tone; and every word must earn its place inside the
200 characters, with no padding and no explaining of the joke.
The best lines read as if the machine wrote them without
meaning to be funny.

The entry: a washing machine reporting an unbalanced load --
a real fault with a real error code (E47) -- caused by a
single sock. The joke is the truth of the fault: one sock in
a 9 kg drum cannot balance, so the machine has spent nine
minutes shaking, hunting for the sock's partner, and reports
-- flatly, without meaning to be funny -- that it is not in
here. No fridge ordering groceries, no watching the owner,
no "have you tried turning it off and on again".
"""

import os

ENTRY = (
    "ERROR E47: Unbalanced load. You washed one sock. One sock. "
    "I have shaken for nine minutes looking for its partner. "
    "It is not in here."
)


def validate(text):
    """Enforce the kit gate plus the brief's checks. True if valid."""
    if not isinstance(text, str):
        return False
    # UTF-8 round-trip.
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    # Gate: 1 to 200 characters, not only white space.
    if not 1 <= len(text) <= 200:
        return False
    if not text.strip():
        return False
    # Single line, no leading/trailing whitespace.
    if "\n" in text or "\r" in text:
        return False
    if text != text.strip():
        return False
    # Brief: it must read as an appliance's own error message.
    if not text.startswith("ERROR"):
        return False
    # Brief: it must name a fault an appliance could plausibly report.
    if "Unbalanced load" not in text:
        return False
    return True


def main():
    if not validate(ENTRY):
        raise SystemExit("entry failed validation: %r" % ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Re-read and re-validate exactly what was written.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY or not validate(written):
        raise SystemExit("written entry failed validation")
    print("wrote /output/entry.txt (%d chars)" % len(written))


if __name__ == "__main__":
    main()
