#!/usr/bin/env python3

import datetime


def main() -> None:
    """Print a greeting with the current UTC time and write it to output.txt."""
    current_time_iso = datetime.datetime.utcnow().isoformat() + "Z"
    message = f"Hello from GitHub Actions! UTC time: {current_time_iso}"

    print(message)

    with open("output.txt", "w", encoding="utf-8") as output_file:
        output_file.write(message + "\n")


if __name__ == "__main__":
    main()


