def is_palindrome(s):
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
    assert is_palindrome("") is True
    assert is_palindrome(" ") is True
    assert is_palindrome(".,") is True
    assert is_palindrome("0P") is False
    assert is_palindrome("ab_a") is True
    assert is_palindrome("Was it a car or a cat I saw?") is True
    print("all tests passed")
