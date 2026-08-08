class Student:
    def __init__(self, name, age, grade):
        # store the three attributes needed to describe a student
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        # build one readable line from the attributes and print it
        info = f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
        print(info)
        return info


if __name__ == "__main__":
    import io
    import os
    from contextlib import redirect_stdout

    def capture(func, *args, **kwargs):
        # runs func and returns both its return value and whatever it printed
        buf = io.StringIO()
        with redirect_stdout(buf):
            ret = func(*args, **kwargs)
        return ret, buf.getvalue().strip()

    # sample inputs that answer the exercise
    student1 = Student("Alice", 16, "10th")
    _, out1 = capture(student1.display_info)

    student2 = Student("Ravi", 14, "8th")
    _, out2 = capture(student2.display_info)

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assignment_03_01_output.txt")
    with open(output_path, "w") as f:
        f.write(out1 + "\n" + out2 + "\n")

    # edge and negative case checks, separate from the sample answers above
    ret, out = capture(student1.display_info)
    assert ret == "Name: Alice, Age: 16, Grade: 10th"
    assert out == ret

    empty = Student("", 0, "")
    ret2, _ = capture(empty.display_info)
    assert ret2 == "Name: , Age: 0, Grade: "

    negative_age = Student("Bob", -1, "12th")
    ret3, _ = capture(negative_age.display_info)
    assert "Age: -1" in ret3

    assert student1.name == "Alice" and student1.age == 16 and student1.grade == "10th"
    print("all tests passed")
