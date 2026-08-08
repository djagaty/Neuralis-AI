def longest_palindrome(s):
    if not s:
        return ""
    start, end = 0, 0

    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return l + 1, r - 1

    for i in range(len(s)):
        l1, r1 = expand(i, i)
        if r1 - l1 > end - start:
            start, end = l1, r1
        l2, r2 = expand(i, i + 1)
        if r2 - l2 > end - start:
            start, end = l2, r2
    return s[start:end + 1]


if __name__ == "__main__":
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("") == ""
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") in ("a", "c")
    assert longest_palindrome("forgeeksskeegfor") == "geeksskeeg"
    print("all tests passed")
