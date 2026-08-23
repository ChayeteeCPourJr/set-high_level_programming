#!/usr/bin/python3

import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)


def solve(row, queens, columns, diagonals1, diagonals2):
    if row == n:
        print(queens)
        return

    for col in range(n):
        if col in columns:
            continue

        if row - col in diagonals1:
            continue

        if row + col in diagonals2:
            continue

        queens.append([row, col])
        columns.add(col)
        diagonals1.add(row - col)
        diagonals2.add(row + col)

        solve(row + 1, queens, columns, diagonals1, diagonals2)

        queens.pop()
        columns.remove(col)
        diagonals1.remove(row - col)
        diagonals2.remove(row + col)


solve(0, [], set(), set(), set())
