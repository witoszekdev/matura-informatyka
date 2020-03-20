class Stack:
    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

    def push(self, item):
        self.list.insert(0, item)

    def pull(self):
        return self.list.pop(0)


if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push("lazania")
    my_stack.push("Garfield")
    my_stack.push("John")

    print(my_stack.pull())
    print(my_stack.pull())
