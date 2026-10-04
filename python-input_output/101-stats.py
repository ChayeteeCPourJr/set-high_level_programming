#!/usr/bin/python3
"""Reads stdin line by line and computes metrics, printing stats
every 10 lines and at the end (or on keyboard interruption)."""
import sys

CODES = ["200", "301", "400", "401", "403", "404", "405", "500"]


def print_stats(total_size, status_counts):
    """Prints the accumulated file size and status code counts."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        print("{}: {}".format(code, status_counts[code]))


if __name__ == "__main__":
    total_size = 0
    status_counts = {}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            try:
                size = int(parts[-1])
                status = parts[-2]
                total_size += size
                if status in CODES:
                    status_counts[status] = (
                        status_counts.get(status, 0) + 1)
            except (IndexError, ValueError):
                pass

            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

        print_stats(total_size, status_counts)
    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise
