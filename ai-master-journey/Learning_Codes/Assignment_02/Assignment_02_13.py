def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))


if __name__ == "__main__":
    assert sorted(intersection([1, 2, 2, 1], [2, 2])) == [2]
    assert sorted(intersection([4, 9, 5], [9, 4, 9, 8, 4])) == [4, 9]
    assert intersection([], [1, 2]) == []
    assert intersection([1, 2], []) == []
    assert intersection([1, 2], [3, 4]) == []
    assert sorted(intersection([1, 1, 1], [1, 1])) == [1]
    print("all tests passed")
