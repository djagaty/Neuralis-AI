import os
import numpy as np
import numpy.ma as ma


def mask_above_and_sum(arr, threshold):
    masked = ma.masked_greater(arr, threshold)
    return masked, masked.sum()


def mask_diagonal_and_fill(arr):
    if arr.shape[0] != arr.shape[1]:
        raise ValueError("array must be square")
    mask = np.eye(arr.shape[0], dtype=bool)
    masked = ma.array(arr.astype(float), mask=mask)
    mean_val = masked.mean()
    return masked.filled(mean_val)


if __name__ == "__main__":
    rng = np.random.default_rng(42)

    sum_source = rng.integers(1, 20, size=(4, 4))
    masked1, total = mask_above_and_sum(sum_source, 10)

    fill_source = rng.integers(1, 20, size=(3, 3))
    filled = mask_diagonal_and_fill(fill_source)

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assignment_04_10_output.txt")
    with open(output_path, "w") as f:
        f.write("Part 1: sum of unmasked elements in a 4x4 array, values above 10 masked\n")
        f.write(f"array =\n{sum_source}\nmasked =\n{masked1}\nsum of unmasked = {total}\n\n")
        f.write("Part 2: diagonal masked and filled with the mean of a 3x3 array\n")
        f.write(f"array =\n{fill_source}\nfilled =\n{filled}\n")

    # part 1 checks
    fixed = np.arange(1, 17).reshape(4, 4)
    _, fixed_sum = mask_above_and_sum(fixed, 10)
    assert fixed_sum == 55

    _, all_masked_sum = mask_above_and_sum(fixed, 0)
    assert ma.is_masked(all_masked_sum)

    try:
        mask_above_and_sum(fixed, "ten")
        assert False, "expected TypeError for a non-numeric threshold"
    except TypeError:
        pass

    # part 2 checks
    fixed2 = np.arange(1, 10).reshape(3, 3)
    filled2 = mask_diagonal_and_fill(fixed2)
    expected = np.array([[5.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 5.0]])
    assert np.allclose(filled2, expected)

    small = np.array([[1, 2], [3, 4]])
    filled_small = mask_diagonal_and_fill(small)
    assert np.allclose(filled_small, [[2.5, 2.0], [3.0, 2.5]])

    try:
        mask_diagonal_and_fill(np.arange(1, 7).reshape(2, 3))
        assert False, "expected ValueError for a non-square array"
    except ValueError:
        pass

    print("all tests passed")
