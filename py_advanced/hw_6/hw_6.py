documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
}


def person_by_doc_num(file_name, doc_num):
    for doc in file_name:
        if doc_num == doc['number']:
            result = f'Person with {doc_num} document number: {doc["name"]}'
            break
        else:
            result = f'Person with {doc_num} document number not found'
    return result


#print(person_by_doc_num(documents, '2207'))


def doc_in_shelf(file_name, doc_num):
    for k, v in file_name.items():
        if doc_num in v:
            result = f'Document {doc_num} is in shelf № {k}'
            break
        else:
            result = f'Document {doc_num} does not exist in this directory'
    return result


#print(doc_in_shelf(directories, '5455'))


def all_docs(file1):
    all_docs_list = list()
    for doc in file1:
        all_docs_list.append(f'{doc["type"]} "{doc["number"]}" "{doc["name"]}"')
    return all_docs_list


#print(all_docs(documents))

def add_new_doc(file1, file2, doc_type, doc_number, owner_name, to_shelf):
    new_doc = dict()
    new_doc['type'] = doc_type
    new_doc['number'] = doc_number
    new_doc['name'] = owner_name
    result = None
    if to_shelf in file2.keys():
        file2[to_shelf].append(new_doc["number"])
        file1.append(new_doc)
    else:
        result = 'This shelf does not exist.'
    return result if result else (file1, file2)


#print(add_new_doc(documents, directories, 'list', '450405', 'Julio', '3'))

def delete_doc(file1, file2, doc_num):
    subresult1 = 0
    subresult2 = 0
    for doc in file1:
        if doc_num not in doc.values():
            if subresult1 < 1:
                subresult1 += 1
        else:
            file1.remove(doc)
            subresult1 = 0
            break
    for k, v in file2.items():
        if doc_num not in v:
            if subresult2 < 1:
                subresult2 += 1
        else:
            v.remove(doc_num)
            subresult2 = 0
            break
    if subresult1+subresult2 < 2:
        result = f'File {doc_num} successfully deleted'
    else:
        result = f'File {doc_num} does not exist in this directories'
    return result


#print(delete_doc(documents, directories, '5455 028765'))


def move_doc(file1, doc_num, to_shelf):
    moving_doc = None
    sub_result_1 = 0
    sub_result_2 = None
    for v in file1.values():
        if doc_num not in v:
            if sub_result_1 < 1:
                sub_result_1 += 1
        else:
            moving_doc = doc_num
            v.remove(doc_num)
            sub_result_1 = 0
            break
    if to_shelf not in file1.keys():
        sub_result_2 = 1
    else:
        for k, v in file1.items():
            if to_shelf == k:
                v.append(moving_doc)
    if sub_result_1 == 1:
        result = f'Document {doc_num} does not exist'
    elif sub_result_2:
        result = f'Shelf {to_shelf} does not exist in this directory'
    else:
        result = f'Document {doc_num} moved to shelf {to_shelf} successfully'
    return result


#print(move_doc(directories, '11-2', '3'))


def add_shelf(file1, new_shelf):
    if new_shelf not in file1.keys():
        file1[new_shelf] = []
        result = f'Shelf {new_shelf} created successfully'
    else:
        result = f'Shelf {new_shelf} already exists'
    return result


#print(add_shelf(directories, 'qwe'))

def work_with_docs(user_command, *args):
    if user_command == 'p':
        result = person_by_doc_num(*args)
    elif user_command == 's':
        result = doc_in_shelf(*args)
    elif user_command == 'l':
        result = all_docs(*args)
    elif user_command == 'a':
        result = add_new_doc(*args)
    elif user_command == 'd':
        result = delete_doc(*args)
    elif user_command == 'm':
        result = move_doc(*args)
    elif user_command == 'as':
        result = add_shelf(*args)
    else:
        result = 'There is no such command'
    return result


#print(work_with_docs('l', documents))
