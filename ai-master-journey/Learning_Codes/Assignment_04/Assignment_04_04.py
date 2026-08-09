import os
import numpy as np


def summary_stats(arr):
    return arr.mean(), np.median(arr), arr.std(), arr.var()


def normalize(arr):
    std = arr.std()
    if std == 0:
        return np.zeros_like(arr, dtype=float)
    return (arr - arr.mean()) / std


if __name__ == "__main__":
    rng = np.random.default_rng(42)

    stats_arr = rng.integers(1, 50, size=(5, 5))
    mean, median, std, var = summary_stats(stats_arr)

    norm_source = np.arange(1, 10).reshape(3, 3)
    normalized = normalize(norm_source)

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assignment_04_04_output.txt")
    with open(output_path, "w") as f:
        f.write("Part 1: statistics of a 5x5 random array\n")
        f.write(f"array =\n{stats_arr}\n")
        f.write(f"mean={mean}, median={median}, std={std}, var={var}\n\n")
        f.write("Part 2: normalized 3x3 range array\n")
        f.write(str(normalized) + "\n")

    # part 1 checks
    fixed = np.arange(1, 26).reshape(5, 5)
    mean2, median2, std2, var2 = summary_stats(fixed)
    assert mean2 == np.mean(fixed)
    assert median2 == np.median(fixed)
    assert std2 == np.std(fixed)
    assert var2 == np.var(fixed)
    assert mean2 == 13.0

    single = np.array([[5]])
    assert summary_stats(single) == (5.0, 5.0, 0.0, 0.0)

    # part 2 checks
    assert abs(normalized.mean()) < 1e-9
    assert abs(normalized.std() - 1.0) < 1e-9

    constant = np.full((3, 3), 7)
    result = normalize(constant)
    assert np.all(result == 0)

    print("all tests passed")
