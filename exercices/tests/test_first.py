# from exercices.src.fonctions_simples import add, divide, add_integer, alea_uniform
# import pytest

# def test_add_with_integer():
#     assert add(5,6) == 11

# def test_add_with_string():
#     assert add("abc", "def") == "abcdef"

# def test_divide():
#     assert divide(10,2) == 5

# def test_error_divide_by_zero():
#     with pytest.raises(ZeroDivisionError):
#         divide(30,0)

# def test_add_integer():
#     assert add_integer(10,3) == 13

# def test_error_add_integer():
#     with pytest.raises(TypeError):
#         add_integer("10")

# def test_alea_uniform():
#     assert 4 <= alea_uniform(4, 8) <= 8

from exercices.src.fonctions_simples import add, divide, add_integer, alea_uniform, input_function_fois_deux, create_file, randomize
import pytest
from unittest.mock import patch
import random

####### Test add #######

def test_add_integers():
    assert add(1,2) == 3
    assert add(0,0) == 0
    assert add(-1,1) == 0
    assert add(-1,-1) == -2
    assert add(1,3.8) == 4.8

def test_add_integer_float():
    assert add(1,2.3) == 3.3

def test_add_floats():
    assert add(1.0,2.0) == 3.0
    assert add(0.0,0.0) == 0.0
    assert add(-1.0,1.0) == 0.0
    assert add(-1.0,-1.0) == -2.0

def test_add_strings():
    assert add("a","b") == "ab"
    assert add("","") == ""
    assert add("a","") == "a"
    assert add("","b") == "b"

def test_add_list():
    assert add([1,2,3],[4,5,6]) == [1,2,3,4,5,6]
    assert add([1,2,3],[]) == [1,2,3]
    assert add([],[4,5,6]) == [4,5,6]
    assert add([],[]) == []

def test_add_error_mixed_type():
    with pytest.raises(TypeError):
        add(1,"a")
    with pytest.raises(TypeError):
        add(2,[1,2])
    with pytest.raises(TypeError):
        add("2",["1","2"])

####### Test divide ####### 

def test_divide_ok():
    assert divide(1,1) == 1
    assert divide(1,2) == 0.5
    assert divide(2.2,2) == 1.1

def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(8,0)

# --------------- Test des fonctions difficile ------------




def test_input_function_fois_deux():
    with patch('builtins.input', return_value='3'):
        assert input_function_fois_deux() == 6

# def test_create_file():
#     create_file("exercices/src/liste_apprennants.txt","\nAlfred")
#     with open("exercices/src/liste_apprennants.txt", "r") as fichier:
#         assert "\nAlfred" in fichier.read()

def test_create_file(tmpdir):
    print(tmpdir)
    file_path = tmpdir.join("liste_apprennants.txt")
    print(file_path)
    create_file(file_path, "\nAlfred")
    with open(file_path, "r") as fichier:
        assert "\nAlfred" in fichier.read()


random.seed(42)

def test_randomize():
    assert randomize() == 0.6394267984578837