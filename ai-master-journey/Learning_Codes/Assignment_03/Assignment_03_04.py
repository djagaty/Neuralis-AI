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


# works with any object that has a display_info method, regardless of its class
def print_student_info(student):
    return student.display_info()


if __name__ == "__main__":
    import io
    from contextlib import redirect_stdout

    def capture(func, *args, **kwargs):
        buf = io.StringIO()
        with redirect_stdout(buf):
            ret = func(*args, **kwargs)
        return ret, buf.getvalue().strip()

    base = Student("Alice", 16, "10th")
    hs = HighSchoolStudent("Bob", 17, "11th", "Junior")

    ret1, out1 = capture(print_student_info, base)
    assert ret1 == "Name: Alice, Age: 16, Grade: 10th"
    assert out1 == ret1

    ret2, out2 = capture(print_student_info, hs)
    assert ret2 == "Name: Bob, Age: 17, Grade: 11th, Grade Level: Junior"
    assert out2 == ret2

    class NotAStudent:
        pass

    try:
        print_student_info(NotAStudent())
        assert False, "expected AttributeError for object without display_info"
    except AttributeError:
        pass

    print("all tests passed")
