class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]


if __name__ == "__main__":
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    assert ms.get_min() == -3
    ms.pop()
    assert ms.top() == 0
    assert ms.get_min() == -2

    ms2 = MinStack()
    ms2.push(5)
    ms2.push(5)
    ms2.push(2)
    assert ms2.get_min() == 2
    ms2.pop()
    assert ms2.get_min() == 5
    ms2.pop()
    assert ms2.get_min() == 5

    ms3 = MinStack()
    ms3.push(1)
    assert ms3.top() == 1
    assert ms3.get_min() == 1
    print("all tests passed")
