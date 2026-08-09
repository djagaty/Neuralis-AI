import os
import numpy as np


def make_array_with_column_replaced(rows, cols, low, high, col_index, value, rng):
    arr = rng.integers(low, high + 1, size=(rows, cols))
    arr[:, col_index] = value
    return arr


def make_range_array_with_zero_diagonal(n):
    arr = np.arange(1, n * n + 1).reshape(n, n)
    np.fill_diagonal(arr, 0)
    return arr


if __name__ == "__main__":
    rng = np.random.default_rng(42)

    arr1 = make_array_with_column_replaced(5, 5, 1, 20, 2, 1, rng)
    arr2 = make_range_array_with_zero_diagonal(4)

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assignment_04_01_output.txt")
    with open(output_path, "w") as f:
        f.write("Part 1: 5x5 random array with 3rd column set to 1\n")
        f.write(str(arr1) + "\n\n")
        f.write("Part 2: 4x4 range array with diagonal set to 0\n")
        f.write(str(arr2) + "\n")

    # part 1 checks
    test_rng = np.random.default_rng(1)
    a = make_array_with_column_replaced(5, 5, 1, 20, 2, 1, test_rng)
    assert a.shape == (5, 5)
    assert np.all(a[:, 2] == 1)
    assert np.all(a >= 1) and np.all(a <= 20)

    single = make_array_with_column_replaced(1, 1, 5, 5, 0, 1, np.random.default_rng(0))
    assert single.shape == (1, 1)
    assert single[0, 0] == 1

    try:
        make_array_with_column_replaced(3, 3, 1, 5, 5, 1, np.random.default_rng(0))
        assert False, "expected IndexError for out of range column"
    except IndexError:
        pass

    # part 2 checks
    b = make_range_array_with_zero_diagonal(4)
    assert b.shape == (4, 4)
    assert np.all(np.diag(b) == 0)
    off_diag_expected = np.array([2, 3, 4, 5, 7, 8, 9, 10, 12, 13, 14, 15])
    off_diag_actual = b[~np.eye(4, dtype=bool)]
    assert np.array_equal(np.sort(off_diag_actual), off_diag_expected)

    c = make_range_array_with_zero_diagonal(1)
    assert np.array_equal(c, np.array([[0]]))

    d = make_range_array_with_zero_diagonal(0)
    assert d.shape == (0, 0)

    print("all tests passed")
