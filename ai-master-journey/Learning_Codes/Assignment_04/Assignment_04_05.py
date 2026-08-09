import os
import numpy as np


def add_vector_to_rows(arr, vec):
    return arr + vec


def subtract_vector_from_columns(arr, vec):
    return arr - vec.reshape(-1, 1)


if __name__ == "__main__":
    rng = np.random.default_rng(42)

    arr1 = rng.integers(1, 20, size=(3, 3))
    vec1 = rng.integers(1, 20, size=(3,))
    added = add_vector_to_rows(arr1, vec1)

    arr2 = rng.integers(1, 20, size=(4, 4))
    vec2 = rng.integers(1, 20, size=(4,))
    subtracted = subtract_vector_from_columns(arr2, vec2)

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assignment_04_05_output.txt")
    with open(output_path, "w") as f:
        f.write("Part 1: adding a length-3 vector to every row of a 3x3 array\n")
        f.write(f"array =\n{arr1}\nvector = {vec1}\nresult =\n{added}\n\n")
        f.write("Part 2: subtracting a length-4 vector from every column of a 4x4 array\n")
        f.write(f"array =\n{arr2}\nvector = {vec2}\nresult =\n{subtracted}\n")

    # part 1 checks
    fixed_arr = np.arange(1, 10).reshape(3, 3)
    fixed_vec = np.array([10, 20, 30])
    result = add_vector_to_rows(fixed_arr, fixed_vec)
    expected = np.array([[11, 22, 33], [14, 25, 36], [17, 28, 39]])
    assert np.array_equal(result, expected)

    try:
        add_vector_to_rows(fixed_arr, np.array([1, 2, 3, 4]))
        assert False, "expected ValueError for mismatched vector length"
    except ValueError:
        pass

    # part 2 checks
    fixed_arr2 = np.arange(1, 17).reshape(4, 4)
    fixed_vec2 = np.array([1, 2, 3, 4])
    result2 = subtract_vector_from_columns(fixed_arr2, fixed_vec2)
    expected2 = np.array([[0, 1, 2, 3], [3, 4, 5, 6], [6, 7, 8, 9], [9, 10, 11, 12]])
    assert np.array_equal(result2, expected2)

    try:
        subtract_vector_from_columns(fixed_arr2, np.array([1, 2, 3]))
        assert False, "expected ValueError for mismatched vector length"
    except ValueError:
        pass

    print("all tests passed")
