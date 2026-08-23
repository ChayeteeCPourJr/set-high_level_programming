#!/usr/bin/python3
"""Log parsing and metrics module."""

import sys


def print_stats(total_size, status_counts):
    """Print the current metrics."""
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts):
        print("{}: {}".format(status_code, status_counts[status_code]))


total_size = 0
status_counts = {}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()

        if len(parts) < 9:
            continue

        try:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
        except (ValueError, IndexError):
            continue

        total_size += file_size

        if status_code in (200, 301, 400, 401, 403, 404, 405, 500):
            status_counts[status_code] = status_counts.get(status_code, 0) + 1

        line_count += 1

        if line_count == 10:
            print_stats(total_size, status_counts)
            line_count = 0

except KeyboardInterrupt:
    print_stats(total_size, status_counts)
