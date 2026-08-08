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


def print_student_info(student):
    # works for any object with a display_info method, Student or HighSchoolStudent
    # the caller does not need to know which class it is, that is polymorphism
    return student.display_info()


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
    hs = HighSchoolStudent("Bob", 17, "11th", "Junior")

    _, out1 = capture(print_student_info, base)
    _, out2 = capture(print_student_info, hs)

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assignment_03_04_output.txt")
    with open(output_path, "w") as f:
        f.write(out1 + "\n" + out2 + "\n")

    # edge and negative case checks
    ret1, out1b = capture(print_student_info, base)
    assert ret1 == "Name: Alice, Age: 16, Grade: 10th"
    assert out1b == ret1

    ret2, out2b = capture(print_student_info, hs)
    assert ret2 == "Name: Bob, Age: 17, Grade: 11th, Grade Level: Junior"
    assert out2b == ret2

    class NotAStudent:
        pass

    try:
        print_student_info(NotAStudent())
        assert False, "expected AttributeError for object without display_info"
    except AttributeError:
        pass

    print("all tests passed")
