import os
import numpy as np


def elementwise_ops(a, b):
    return a + b, a - b, a * b, a / b


def row_and_column_sums(arr):
    return arr.sum(axis=1), arr.sum(axis=0)


if __name__ == "__main__":
    rng = np.random.default_rng(42)

    a = rng.integers(1, 20, size=(3, 4))
    b = rng.integers(1, 20, size=(3, 4))
    add, sub, mul, div = elementwise_ops(a, b)

    range_arr = np.arange(1, 17).reshape(4, 4)
    row_sums, col_sums = row_and_column_sums(range_arr)

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assignment_04_03_output.txt")
    with open(output_path, "w") as f:
        f.write("Part 1: element-wise operations on two 3x4 random arrays\n")
        f.write(f"a =\n{a}\nb =\n{b}\n")
        f.write(f"a + b =\n{add}\na - b =\n{sub}\na * b =\n{mul}\na / b =\n{div}\n\n")
        f.write("Part 2: row-wise and column-wise sum of a 4x4 range array\n")
        f.write(f"row sums = {row_sums}\ncolumn sums = {col_sums}\n")

    # part 1 checks
    x = np.array([[1, 2], [3, 4]])
    y = np.array([[5, 6], [7, 8]])
    ax, sx, mx, dx = elementwise_ops(x, y)
    assert np.array_equal(ax, [[6, 8], [10, 12]])
    assert np.array_equal(sx, [[-4, -4], [-4, -4]])
    assert np.array_equal(mx, [[5, 12], [21, 32]])
    assert np.allclose(dx, [[0.2, 1 / 3], [3 / 7, 0.5]])

    try:
        elementwise_ops(np.zeros((3, 4)), np.zeros((3, 3)))
        assert False, "expected ValueError for mismatched shapes"
    except ValueError:
        pass

    # part 2 checks
    r, c = row_and_column_sums(range_arr)
    assert np.array_equal(r, [10, 26, 42, 58])
    assert np.array_equal(c, [28, 32, 36, 40])

    single = np.array([[7]])
    r2, c2 = row_and_column_sums(single)
    assert r2[0] == 7 and c2[0] == 7

    print("all tests passed")
