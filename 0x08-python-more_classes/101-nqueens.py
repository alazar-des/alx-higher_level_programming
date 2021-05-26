#!/usr/bin/python3
"""places N non-attacking queens on an N×N chessboard.
N should be 4 or greater.
"""


def check(location_list, row, col):
    """Check if queen can be placed in a given row and col, given previously
    placed queens.

    Args:
        location_list (list): location of placed queens.
        row (int): row to be checked
        col (int): col to be checked

    Yields:
        True or False: if non-attacking position Treu otherwise False
    """
    for loc in location_list:
        if loc[1] == col:
            return False
        if loc[0] + loc[1] == row + col:
            return False
        if loc[0] - loc[1] == row - col:
            return False
    return True


def place(location_list, queen, column):
    """Places other queens except the firs queen given in non-attacking
    position

    Args:
        location_list (empty list): the previous saved position of the queens
        queen (int): the queen number starting from 0
        column (int): the previous queen's column position

    Yields:
        True or False: if all queens could position in non attacing position
                       True otherwise False.
    """

    if queen == 0:
        location_list += [[0, column]]
        place(location_list, queen + 1, 1)
    else:
        for col in range(N):
            if check(location_list, queen, col):
                location_list += [[queen, col]]
                if queen + 1 == N:
                    print(location_list)
                place(location_list, queen + 1, 1)
        del location_list[-1]
        if len(location_list) == 0:
            return False


if __name__ == "__main__":
    import sys
    """Program entry point."""
    argc = len(sys.argv)
    if argc != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if N < 4:
        print("N must be at least 4")
        exit(1)
    for column in range(N):
        location_list = []
        place(location_list, 0, column)
