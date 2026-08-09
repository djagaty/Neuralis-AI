import os
import numpy as np


def reshape_row_then_column(arr):
    row = arr.reshape(1, arr.size)
    column = arr.reshape(arr.size, 1)
    return row, column


def flatten_and_restore(arr):
    flat = arr.flatten()
    restored = flat.reshape(arr.shape)
    return flat, restored


if __name__ == "__main__":
    rng = np.random.default_rng(42)

    base = np.arange(1, 10).reshape(3, 3)
    row, column = reshape_row_then_column(base)

    random_arr = rng.integers(1, 50, size=(5, 5))
    flat, restored = flatten_and_restore(random_arr)

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assignment_04_07_output.txt")
    with open(output_path, "w") as f:
        f.write("Part 1: 3x3 array reshaped to (1,9) then (9,1)\n")
        f.write(f"row shape=(1,9):\n{row}\ncolumn shape=(9,1):\n{column}\n\n")
        f.write("Part 2: flatten and restore a 5x5 random array\n")
        f.write(f"flat =\n{flat}\nrestored =\n{restored}\n")

    # part 1 checks
    assert row.shape == (1, 9)
    assert column.shape == (9, 1)
    assert np.array_equal(row.flatten(), np.arange(1, 10))
    assert np.array_equal(column.flatten(), np.arange(1, 10))

    try:
        base.reshape(2, 5)
        assert False, "expected ValueError for incompatible reshape"
    except ValueError:
        pass

    # part 2 checks
    assert flat.shape == (25,)
    assert np.array_equal(restored, random_arr)
    assert restored.shape == (5, 5)

    try:
        flat.reshape(4, 6)
        assert False, "expected ValueError for incompatible reshape"
    except ValueError:
        pass

    print("all tests passed")
