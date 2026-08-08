class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        info = f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
        print(info)
        return info


if __name__ == "__main__":
    import io
    from contextlib import redirect_stdout

    def capture(func, *args, **kwargs):
        buf = io.StringIO()
        with redirect_stdout(buf):
            ret = func(*args, **kwargs)
        return ret, buf.getvalue().strip()

    s1 = Student("Alice", 16, "10th")
    ret, out = capture(s1.display_info)
    assert ret == "Name: Alice, Age: 16, Grade: 10th"
    assert out == ret

    s2 = Student("", 0, "")
    ret2, out2 = capture(s2.display_info)
    assert ret2 == "Name: , Age: 0, Grade: "

    s3 = Student("Bob", -1, "12th")
    ret3, out3 = capture(s3.display_info)
    assert "Age: -1" in ret3

    assert s1.name == "Alice" and s1.age == 16 and s1.grade == "10th"
    print("all tests passed")
