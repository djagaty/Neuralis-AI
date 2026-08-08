def roman_to_int(s):
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    for i in range(len(s)):
        if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
            total -= values[s[i]]
        else:
            total += values[s[i]]
    return total


if __name__ == "__main__":
    assert roman_to_int("III") == 3
    assert roman_to_int("LVIII") == 58
    assert roman_to_int("MCMXCIV") == 1994
    assert roman_to_int("IV") == 4
    assert roman_to_int("IX") == 9
    assert roman_to_int("") == 0
    assert roman_to_int("MMMCMXCIX") == 3999
    print("all tests passed")
