'''Генераторы'''
nested_list = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]


'''Вариант 1'''


print(list(sub_sub for sub in nested_list for sub_sub in sub))


'''Вариант 2'''


def make_list_flat(some_list):
    for item in some_list:
        if not isinstance(item, list):
            yield item
        else:
            for item_1 in make_list_flat(item):
                yield item_1


print([item for item in make_list_flat(nested_list)])
