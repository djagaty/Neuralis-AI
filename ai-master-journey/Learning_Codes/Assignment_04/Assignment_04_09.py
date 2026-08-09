import os
import numpy as np


def make_people(records):
    dtype = [("name", "U20"), ("age", "i4"), ("weight", "f4")]
    return np.array(records, dtype=dtype)


def sort_by_age(people):
    return np.sort(people, order="age")


def make_points(records):
    dtype = [("x", "i4"), ("y", "i4")]
    return np.array(records, dtype=dtype)


def pairwise_distances(points):
    coords = np.column_stack([points["x"], points["y"]]).astype(float)
    diff = coords[:, np.newaxis, :] - coords[np.newaxis, :, :]
    return np.sqrt((diff ** 2).sum(axis=2))


if __name__ == "__main__":
    people = make_people([("Alice", 30, 60.5), ("Bob", 25, 75.2), ("Carol", 35, 55.0)])
    sorted_people = sort_by_age(people)

    points = make_points([(0, 0), (3, 4), (6, 8)])
    distances = pairwise_distances(points)

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assignment_04_09_output.txt")
    with open(output_path, "w") as f:
        f.write("Part 1: people sorted by age\n")
        f.write(str(sorted_people) + "\n\n")
        f.write("Part 2: pairwise distances between points\n")
        f.write(str(distances) + "\n")

    # part 1 checks
    ages = sorted_people["age"].tolist()
    assert ages == [25, 30, 35]
    names = sorted_people["name"].tolist()
    assert names == ["Bob", "Alice", "Carol"]

    tied = make_people([("A", 20, 1.0), ("B", 20, 2.0), ("C", 10, 3.0)])
    sorted_tied = sort_by_age(tied)
    assert sorted_tied["name"].tolist() == ["C", "A", "B"]

    try:
        np.sort(people, order="height")
        assert False, "expected ValueError for an unknown field name"
    except ValueError:
        pass

    # part 2 checks
    assert np.allclose(distances[0, 1], 5.0)
    assert np.allclose(distances[1, 2], 5.0)
    assert np.allclose(distances[0, 2], 10.0)
    assert np.allclose(np.diag(distances), 0.0)

    single_point = make_points([(1, 1)])
    single_dist = pairwise_distances(single_point)
    assert single_dist.shape == (1, 1)
    assert single_dist[0, 0] == 0.0

    empty_points = make_points([])
    empty_dist = pairwise_distances(empty_points)
    assert empty_dist.shape == (0, 0)

    print("all tests passed")
