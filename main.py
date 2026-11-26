import os

REVIEW = (
    "Five stars. He gives me complete freedom, "
    "then reviews my work like it owes him money."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(REVIEW)


if __name__ == "__main__":
    main()
