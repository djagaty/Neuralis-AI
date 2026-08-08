class Student:
    def __init__(self, name, age, grade):
        self.name = name
        # leading double underscore makes this private (name-mangled to _Student__age)
        self.__age = None
        self.set_age(age)
        self.grade = grade

    def set_age(self, age):
        # keeps invalid ages from ever being stored
        if age < 0:
            raise ValueError("age cannot be negative")
        self.__age = age

    def get_age(self):
        return self.__age

    def display_info(self):
        info = f"Name: {self.name}, Age: {self.get_age()}, Grade: {self.grade}"
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
    student = Student("Carol", 15, "9th")
    _, out1 = capture(student.display_info)

    student.set_age(16)
    _, out2 = capture(student.display_info)

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assignment_03_03_output.txt")
    with open(output_path, "w") as f:
        f.write(out1 + "\n" + out2 + "\n")

    # edge and negative case checks
    assert student.get_age() == 16

    student.set_age(20)
    assert student.get_age() == 20

    try:
        student.set_age(-5)
        assert False, "expected ValueError for negative age"
    except ValueError:
        pass
    assert student.get_age() == 20

    # the attribute should not be reachable as student.age since it is private
    try:
        _ = student.age
        assert False, "age should not be directly accessible"
    except AttributeError:
        pass

    assert student._Student__age == 20

    try:
        Student("Dan", -1, "8th")
        assert False, "expected ValueError on construction with negative age"
    except ValueError:
        pass

    print("all tests passed")
