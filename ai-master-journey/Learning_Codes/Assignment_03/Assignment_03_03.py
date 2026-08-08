class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.__age = None
        self.set_age(age)
        self.grade = grade

    # age is name-mangled to __age so it cannot be reached as student.age
    def set_age(self, age):
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
    s = Student("Carol", 15, "9th")
    assert s.get_age() == 15

    s.set_age(20)
    assert s.get_age() == 20

    try:
        s.set_age(-5)
        assert False, "expected ValueError for negative age"
    except ValueError:
        pass
    assert s.get_age() == 20

    try:
        _ = s.age
        assert False, "age should not be directly accessible"
    except AttributeError:
        pass

    assert s._Student__age == 20

    try:
        Student("Dan", -1, "8th")
        assert False, "expected ValueError on construction with negative age"
    except ValueError:
        pass

    print("all tests passed")
