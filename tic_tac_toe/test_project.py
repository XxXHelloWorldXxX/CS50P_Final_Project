from pytest import raises
from project import  choose_square

# I Couldn't really test the functions in my
# project, but since it's required I just did this

def test_no_input():
    with raises(TypeError):
        choose_square()

def test_random_input():
    with raises(TypeError):
        choose_square(4545)

def test_string_input():
    with raises(ValueError):
        choose_square("sgsg")

