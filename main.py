"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes one single sentence (143 characters) recalling a childhood
memory to /output/entry.txt, exactly as the competition gate requires:
UTF-8 text of 1 to 280 characters.
"""

import os

ENTRY = (
    "Every rainy afternoon my mother fried tempeh while the zinc roof "
    "drummed above us, and I still wait for that smell whenever the "
    "sky turns grey."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
