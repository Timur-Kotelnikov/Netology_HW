'''Итераторы'''

nested_list = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]


class MakeListFlat:

    def __init__(self, some_list):
        self.cursor = 0
        self.cursor_index = -1
        self.list_ = some_list

    def __iter__(self):
        return self

    def __next__(self):
        self.cursor_index += 1
        while self.cursor_index > len(self.list_[self.cursor]) - 1:
            self.cursor += 1
            self.cursor_index = 0
            if self.cursor > len(self.list_) - 1:
                raise StopIteration
        return self.list_[self.cursor][self.cursor_index]


print([i for i in MakeListFlat(nested_list)])

