def group_anagrams(strs):
    groups = {}
    for s in strs:
        key = "".join(sorted(s))
        groups.setdefault(key, []).append(s)
    return list(groups.values())


if __name__ == "__main__":
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    result_sorted = sorted(sorted(g) for g in result)
    expected = sorted(sorted(g) for g in [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])
    assert result_sorted == expected

    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    assert group_anagrams([]) == []
    print("all tests passed")
