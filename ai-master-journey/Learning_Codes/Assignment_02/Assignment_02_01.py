def contains_duplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False


if __name__ == "__main__":
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False
    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    assert contains_duplicate([]) is False
    assert contains_duplicate([7]) is False
    assert contains_duplicate([-1, -1]) is True
    print("all tests passed")
