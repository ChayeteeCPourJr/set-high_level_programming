#!/usr/bin/python3
"""Solve the N queens puzzle."""

import sys


def solve_nqueens(n):
    """Find and print all solutions for an n x n chessboard."""
    solutions = []

    def backtrack(row, queens, columns, diagonals1, diagonals2):
        """Place queens row by row using backtracking."""
        if row == n:
            print(queens)
            solutions.append(queens[:])
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

            backtrack(
                row + 1,
                queens,
                columns,
                diagonals1,
                diagonals2
            )

            queens.pop()
            columns.remove(col)
            diagonals1.remove(row - col)
            diagonals2.remove(row + col)

    backtrack(0, [], set(), set(), set())


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

solve_nqueens(n)
