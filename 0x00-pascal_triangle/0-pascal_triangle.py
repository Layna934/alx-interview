#!/usr/bin/python3
"""
Creating a Pascal Triangle
"""


def pascal_triangle(n):
    """
    Function to create pascal triangle.
    Args:
    n (int): The number of rows in the triangle.

    Returns:
    List[List[int]]: A list of lists representing Pascal's triangle.
    """

    pascal_list = []
    if (n <= 0):
        return pascal_list
    pascal_list.append([1])
    for i in range(1, n):
        row = [1]
        prev_row = pascal_list[i - 1]
        for j in range(1, len(prev_row)):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)
        pascal_list.append(row)
    return pascal_list
