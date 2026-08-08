def max_area(height):
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        h = min(height[left], height[right])
        area = h * (right - left)
        if area > best:
            best = area
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best


if __name__ == "__main__":
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
    assert max_area([4, 3, 2, 1, 4]) == 16
    assert max_area([1, 2, 1]) == 2
    assert max_area([]) == 0
    assert max_area([5]) == 0
    assert max_area([0, 0, 0]) == 0
    print("all tests passed")
