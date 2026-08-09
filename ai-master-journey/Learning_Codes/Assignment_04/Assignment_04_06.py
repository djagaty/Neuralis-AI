import os
import numpy as np


def matrix_properties(matrix):
    det = np.linalg.det(matrix)
    inv = np.linalg.inv(matrix)
    eigenvalues = np.linalg.eigvals(matrix)
    return det, inv, eigenvalues


def multiply(a, b):
    return a @ b


if __name__ == "__main__":
    matrix = np.array([[4, 7, 2], [3, 6, 1], [2, 5, 3]], dtype=float)
    det, inv, eigenvalues = matrix_properties(matrix)

    a = np.arange(1, 7).reshape(2, 3)
    b = np.arange(1, 7).reshape(3, 2)
    product = multiply(a, b)

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assignment_04_06_output.txt")
    with open(output_path, "w") as f:
        f.write("Part 1: determinant, inverse and eigenvalues of a 3x3 matrix\n")
        f.write(f"matrix =\n{matrix}\n")
        f.write(f"determinant = {det}\ninverse =\n{inv}\neigenvalues = {eigenvalues}\n\n")
        f.write("Part 2: matrix multiplication of a (2,3) and a (3,2) array\n")
        f.write(f"a =\n{a}\nb =\n{b}\na @ b =\n{product}\n")

    # part 1 checks
    diag_matrix = np.diag([2.0, 3.0, 4.0])
    d, i, e = matrix_properties(diag_matrix)
    assert abs(d - 24.0) < 1e-9
    assert np.allclose(i, np.diag([0.5, 1 / 3, 0.25]))
    assert np.allclose(np.sort(e), [2.0, 3.0, 4.0])

    singular = np.array([[1.0, 2.0], [2.0, 4.0]])
    assert abs(np.linalg.det(singular)) < 1e-9
    try:
        np.linalg.inv(singular)
        assert False, "expected LinAlgError for a singular matrix"
    except np.linalg.LinAlgError:
        pass

    # part 2 checks
    expected_product = np.array([[22, 28], [49, 64]])
    assert np.array_equal(product, expected_product)

    try:
        multiply(np.zeros((2, 3)), np.zeros((2, 3)))
        assert False, "expected ValueError for incompatible shapes"
    except ValueError:
        pass

    print("all tests passed")
