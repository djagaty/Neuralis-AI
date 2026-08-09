import os
import numpy as np


def get_corners(arr):
    rows = [0, 0, -1, -1]
    cols = [0, -1, 0, -1]
    return arr[rows, cols]


def clip_above(arr, threshold):
    result = arr.copy()
    result[result > threshold] = threshold
    return result


if __name__ == "__main__":
    rng = np.random.default_rng(42)

    corner_source = rng.integers(1, 50, size=(5, 5))
    corners = get_corners(corner_source)

    clip_source = rng.integers(1, 20, size=(4, 4))
    clipped = clip_above(clip_source, 10)

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assignment_04_08_output.txt")
    with open(output_path, "w") as f:
        f.write("Part 1: corner elements of a 5x5 random array\n")
        f.write(f"array =\n{corner_source}\ncorners = {corners}\n\n")
        f.write("Part 2: values above 10 clipped to 10 in a 4x4 random array\n")
        f.write(f"array =\n{clip_source}\nclipped =\n{clipped}\n")

    # part 1 checks
    fixed = np.arange(1, 26).reshape(5, 5)
    assert np.array_equal(get_corners(fixed), [1, 5, 21, 25])

    single = np.array([[9]])
    assert np.array_equal(get_corners(single), [9, 9, 9, 9])

    try:
        get_corners(np.empty((0, 0)))
        assert False, "expected IndexError for an empty array"
    except IndexError:
        pass

    # part 2 checks
    fixed2 = np.arange(1, 17).reshape(4, 4)
    expected = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 10, 10], [10, 10, 10, 10]])
    assert np.array_equal(clip_above(fixed2, 10), expected)

    zeroed = clip_above(fixed2, 0)
    assert np.all(zeroed == 0)

    empty_result = clip_above(np.array([]), 10)
    assert empty_result.shape == (0,)

    print("all tests passed")
