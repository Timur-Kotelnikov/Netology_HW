import pytest
import hw_6


fixture_person_by_doc_num = [
    (hw_6.documents, '2207 876234', 'Person with 2207 876234 document number: Василий Гупкин'),
    (hw_6.documents, '11-2', 'Person with 11-2 document number: Геннадий Покемонов'),
    (hw_6.documents, '12345', 'Person with 12345 document number not found')
]

fixture_doc_in_shelf = [
    (hw_6.directories, '11-2', 'Document 11-2 is in shelf № 1'),
    (hw_6.directories, '10006', 'Document 10006 is in shelf № 2'),
    (hw_6.directories, '12345', 'Document 12345 does not exist in this directory')
]

fixture_add_new_doc = [
    (hw_6.documents, hw_6.directories, 'passport', '123', 'Ann', '4', 'This shelf does not exist.'),
    (hw_6.documents, hw_6.directories, 'card', '080909', 'Jaina', '3', ([{'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'}, {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'}, {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}, {'type': 'card', 'number': '080909', 'name': 'Jaina'}], {'1': ['2207 876234', '11-2', '5455 028765'], '2': ['10006'], '3': ['080909']})),
    (hw_6.documents, hw_6.directories, 'list', '450405', 'Julio', '10', 'This shelf does not exist.')
]

fixture_delete_doc = [
    (hw_6.documents, hw_6.directories, '11-2', 'File 11-2 successfully deleted'),
    (hw_6.documents, hw_6.directories, '10006', 'File 10006 successfully deleted'),
    (hw_6.documents, hw_6.directories, '098', 'File 098 does not exist in this directories')
]

fixture_move_doc = [
    (hw_6.directories, '11-2', '3', 'Document 11-2 moved to shelf 3 successfully'),
    (hw_6.directories, '13123', '3', 'Document 13123 does not exist'),
    (hw_6.directories, '11-2', 'qwerty', 'Shelf qwerty does not exist in this directory')
]

fixture_add_shelf = [
    (hw_6.directories, '3', 'Shelf 3 already exists'),
    (hw_6.directories, '4', 'Shelf 4 created successfully'),
    (hw_6.directories, 'wow', 'Shelf wow created successfully')
]


@pytest.mark.parametrize('file_name, doc_num, etalon', fixture_person_by_doc_num)
def test_person_by_doc_num(file_name, doc_num, etalon):
    result = hw_6.person_by_doc_num(file_name, doc_num)
    assert result == etalon
    assert doc_num in [i['number'] for i in file_name]


@pytest.mark.parametrize('file_name, doc_num, etalon', fixture_doc_in_shelf)
def test_doc_in_shelf(file_name, doc_num, etalon):
    result = hw_6.doc_in_shelf(file_name, doc_num)
    assert result == etalon
    assert doc_num in [q for v in file_name.values() for q in v]


@pytest.mark.parametrize('file_name_1, file_name_2, doc_type, doc_number, owner_name, to_shelf, etalon', fixture_add_new_doc)
def test_add_new_doc(file_name_1, file_name_2, doc_type, doc_number, owner_name, to_shelf, etalon):
    result = hw_6.add_new_doc(file_name_1, file_name_2, doc_type, doc_number, owner_name, to_shelf)
    assert result == etalon


@pytest.mark.parametrize('file_name_1, file_name_2, doc_num, etalon', fixture_delete_doc)
def test_delete_doc(file_name_1, file_name_2, doc_num, etalon):
    result = hw_6.delete_doc(file_name_1, file_name_2, doc_num)
    assert result == etalon


@pytest.mark.parametrize('file_name, doc_num, to_shelf, etalon', fixture_move_doc)
def test_move_doc(file_name, doc_num, to_shelf, etalon):
    result = hw_6.move_doc(file_name, doc_num, to_shelf)
    assert result == etalon


@pytest.mark.parametrize('file_name, new_shelf, etalon', fixture_add_shelf)
def test_add_shelf(file_name, new_shelf, etalon):
    result = hw_6.add_shelf(file_name, new_shelf)
    assert result == etalon

