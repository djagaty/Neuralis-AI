def to_camel_case(sentence):
    words = sentence.split()
    result = ""
    for w in words:
        result += w[0].upper() + w[1:]
    return result


if __name__ == "__main__":
    assert to_camel_case("I get it") == "IGetIt"
    assert to_camel_case("geeks for geeks") == "GeeksForGeeks"
    assert to_camel_case("") == ""
    assert to_camel_case("hello") == "Hello"
    assert to_camel_case("   a   b  ") == "AB"
    assert to_camel_case("convert this string") == "ConvertThisString"
    print("all tests passed")
