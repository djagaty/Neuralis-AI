class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        info = f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
        print(info)
        return info


class HighSchoolStudent(Student):
    def __init__(self, name, age, grade, grade_level):
        super().__init__(name, age, grade)
        self.grade_level = grade_level

    def display_info(self):
        info = f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}, Grade Level: {self.grade_level}"
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

    base = Student("Alice", 16, "10th")
    ret, out = capture(base.display_info)
    assert ret == "Name: Alice, Age: 16, Grade: 10th"

    hs = HighSchoolStudent("Bob", 17, "11th", "Junior")
    ret2, out2 = capture(hs.display_info)
    assert ret2 == "Name: Bob, Age: 17, Grade: 11th, Grade Level: Junior"
    assert out2 == ret2

    assert isinstance(hs, Student)
    assert hs.grade_level == "Junior"

    hs2 = HighSchoolStudent("", 0, "", "")
    ret3, _ = capture(hs2.display_info)
    assert ret3 == "Name: , Age: 0, Grade: , Grade Level: "

    print("all tests passed")
