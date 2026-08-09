import os
import numpy as np


def extract_middle_block(arr):
    return arr[2:5, 1:4]


def extract_border(arr):
    top = arr[0, :]
    bottom = arr[-1, :]
    left = arr[1:-1, 0]
    right = arr[1:-1, -1]
    return np.concatenate([top, bottom, left, right])


if __name__ == "__main__":
    rng = np.random.default_rng(42)

    base = np.arange(1, 37).reshape(6, 6)
    sub = extract_middle_block(base)

    border_source = rng.integers(1, 100, size=(5, 5))
    border = extract_border(border_source)

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assignment_04_02_output.txt")
    with open(output_path, "w") as f:
        f.write("Part 1: 3rd-5th row, 2nd-4th column block of a 6x6 range array\n")
        f.write(str(sub) + "\n\n")
        f.write("Part 2: border elements of a 5x5 random array\n")
        f.write(str(border) + "\n")

    # part 1 checks
    expected_sub = np.array([[14, 15, 16], [20, 21, 22], [26, 27, 28]])
    assert np.array_equal(sub, expected_sub)

    out_of_range = base[10:20, :]
    assert out_of_range.shape == (0, 6)

    try:
        base[100, 0]
        assert False, "expected IndexError for out of range row"
    except IndexError:
        pass

    # part 2 checks
    fixed = np.arange(1, 26).reshape(5, 5)
    expected_border = np.array([1, 2, 3, 4, 5, 21, 22, 23, 24, 25, 6, 11, 16, 10, 15, 20])
    assert np.array_equal(extract_border(fixed), expected_border)

    small = np.array([[1, 2], [3, 4]])
    assert np.array_equal(np.sort(extract_border(small)), [1, 2, 3, 4])

    try:
        extract_border(np.array([1, 2, 3]))
        assert False, "expected IndexError for a 1D array"
    except IndexError:
        pass

    print("all tests passed")
