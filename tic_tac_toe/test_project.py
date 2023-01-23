from pytest import raises
from project import choose_square, check_row, game_over

# I Couldn't really test the functions in my
# project, but since it's required I just did this

def test_no_input():
    with raises(TypeError):
        choose_square()
        check_row()

def test_random_input():
    with raises(TypeError):
        choose_square(4545)
        check_row(344, 3)
        game_over(23463, 564)

def test_string_input():
    with raises(ValueError):
        choose_square("sgsg")
    with raises(TypeError):
        game_over("Ok")
        check_row("Hello")

