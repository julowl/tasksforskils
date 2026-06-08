"""Exercise 3 — Transpose a matrix using nested for loops

Implement transpose(matrix) which takes a 2D list (list of rows) and returns
its transpose (list of columns). Assume all rows have the same length.
"""

from typing import List


def transpose(matrix: List[List[object]]) -> List[List[object]]:
    """Return the transpose of the given 2D matrix.

    Args:
        matrix: list of rows (each row is a list)

    Returns:
        Transposed matrix as a list of rows.
    """
    # Use nested for loops to create the transposed matrix
    result = []

    for col in range(len(matrix[0])):  # по столбцам
        new_row = []
        for row in range(len(matrix)):  # по строкам
            new_row.append(matrix[row][col])
        result.append(new_row)

    return result


if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6]]
    print(transpose(m))  # expect [[1,4],[2,5],[3,6]]
