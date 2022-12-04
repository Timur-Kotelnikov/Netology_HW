from Stack import Stack


def check_parentheses(some_obj):
    some_obj_list = list(some_obj)
    this_obj = Stack(some_obj_list)
    left_side_elements = ['(', '[', '{']
    right_side_elements = [')', ']', '}']
    unpair_elements = list()
    if len(some_obj) % 2 == 1:
        result = False
    else:
        while not this_obj.isEmpty():
            element = this_obj.peek()
            if element in left_side_elements:
                unpair_elements.append(right_side_elements[left_side_elements.index(element)])
            elif element in right_side_elements:
                unpair_elements.append(left_side_elements[right_side_elements.index(element)])
            this_obj.pop()
            for i in range(len(left_side_elements)):
                if unpair_elements.count(left_side_elements[i]) > 0 and unpair_elements.count(right_side_elements[i]) > 0:
                    unpair_elements.remove(left_side_elements[i])
                    unpair_elements.remove(right_side_elements[i])
        if len(unpair_elements) == 0:
            result = True
        else:
            result = False
    return result
