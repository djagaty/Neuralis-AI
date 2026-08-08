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
        # let the parent class set up name, age and grade first
        super().__init__(name, age, grade)
        self.grade_level = grade_level

    def display_info(self):
        # overrides the parent version to also show grade_level
        info = f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}, Grade Level: {self.grade_level}"
        print(info)
        return info


if __name__ == "__main__":
    import io
    import os
    from contextlib import redirect_stdout

    def capture(func, *args, **kwargs):
        buf = io.StringIO()
        with redirect_stdout(buf):
            ret = func(*args, **kwargs)
        return ret, buf.getvalue().strip()

    # sample inputs that answer the exercise
    base = Student("Alice", 16, "10th")
    _, out1 = capture(base.display_info)

    hs = HighSchoolStudent("Bob", 17, "11th", "Junior")
    _, out2 = capture(hs.display_info)

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assignment_03_02_output.txt")
    with open(output_path, "w") as f:
        f.write(out1 + "\n" + out2 + "\n")

    # edge and negative case checks
    ret, out = capture(base.display_info)
    assert ret == "Name: Alice, Age: 16, Grade: 10th"

    ret2, out2b = capture(hs.display_info)
    assert ret2 == "Name: Bob, Age: 17, Grade: 11th, Grade Level: Junior"
    assert out2b == ret2

    # HighSchoolStudent should still be a Student because of inheritance
    assert isinstance(hs, Student)
    assert hs.grade_level == "Junior"

    hs2 = HighSchoolStudent("", 0, "", "")
    ret3, _ = capture(hs2.display_info)
    assert ret3 == "Name: , Age: 0, Grade: , Grade Level: "

    print("all tests passed")
