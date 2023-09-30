import pytest
import json
from person import PeopleMatrix

def test_create_matrix():
    test_data = ["Eddie", "Grant"]
    test_matrix = PeopleMatrix(test_data)
    expected_matrix = [[0, 0], [0, 0]]
    assert test_matrix.get_matrix() == expected_matrix

def test_add_partners():
    test_data = ["Eddie", "Grant"]
    test_matrix = PeopleMatrix(test_data)
    test_matrix.add_partners("Eddie", "Grant")
    expected_matrix = [[0, 1], [1, 0]]
    assert test_matrix.get_matrix() == expected_matrix

def test_remove_partners():
    test_data = ["Eddie", "Grant"]
    test_matrix = PeopleMatrix(test_data)
    test_matrix.add_partners("Eddie", "Grant")
    test_matrix.remove_partners("Eddie", "Grant")
    excepted_matrix = [[0, 0], [0, 0]]
    assert test_matrix.get_matrix() == excepted_matrix

def test_add_person():
    test_data = ["Eddie", "Grant"]
    test_matrix = PeopleMatrix(test_data)
    test_matrix.add_person("Camden")
    expected_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert test_matrix.get_matrix() == expected_matrix


def test_print_matrix():
    test_data = ["Eddie", "Grant"]
    test_matrix = PeopleMatrix(test_data)
    test_matrix.add_partners("Eddie", "Grant")
    test_matrix.print_matrix()

def test_save_load_matrix():
    test_data = ["Eddie", "Grant"]
    test_matrix = PeopleMatrix(test_data)
    json_data = [test_matrix.get_names(), test_matrix.get_matrix()]
    json_object = json.dumps(json_data, indent=4)
    with open("test.json", 'w') as json_file:
        json_file.write(json_object)
    with open('test.json', 'r') as json_file:
        people = json.load(json_file)
    assert json_data == people
    