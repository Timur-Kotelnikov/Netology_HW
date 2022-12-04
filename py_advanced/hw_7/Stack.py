class Stack:
    def __init__(self, some_list):
        self.some_list = some_list

    def isEmpty(self):
        return len(self.some_list) == 0

    def push(self, new_element):
        self.some_list.append(new_element)
        return

    def pop(self):
        return self.some_list.pop(-1)

    def peek(self):
        return self.some_list[-1]

    def size(self):
        return len(self.some_list)
