from collections import Counter


def top_k_frequent(nums, k):
    counts = Counter(nums)
    return [item for item, _ in counts.most_common(k)]


if __name__ == "__main__":
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert top_k_frequent([1], 1) == [1]
    assert sorted(top_k_frequent([4, 1, -2, -2, 1, 4, 4], 2)) == [1, 4]
    assert top_k_frequent([], 0) == []
    assert sorted(top_k_frequent([5, 5, 5, 6, 6, 7], 3)) == [5, 6, 7]
    print("all tests passed")
