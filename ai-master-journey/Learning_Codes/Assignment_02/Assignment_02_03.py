def fizz_buzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


if __name__ == "__main__":
    assert fizz_buzz(15) == [
        "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
        "11", "Fizz", "13", "14", "FizzBuzz"
    ]
    assert fizz_buzz(1) == ["1"]
    assert fizz_buzz(0) == []
    assert fizz_buzz(-3) == []
    assert fizz_buzz(3) == ["1", "2", "Fizz"]
    assert fizz_buzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    print("all tests passed")
