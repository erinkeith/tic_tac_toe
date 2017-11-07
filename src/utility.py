def base3tobase10(row, column):
    if row < 3 and column < 3:
        return 3 * row + column

    return None