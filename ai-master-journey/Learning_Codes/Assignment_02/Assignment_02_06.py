def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


if __name__ == "__main__":
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert longest_common_prefix(["dog", "racecar", "car"]) == ""
    assert longest_common_prefix([]) == ""
    assert longest_common_prefix([""]) == ""
    assert longest_common_prefix(["a"]) == "a"
    assert longest_common_prefix(["", "b"]) == ""
    assert longest_common_prefix(["interview", "interrupt", "integrate", "interval"]) == "inte"
    print("all tests passed")
