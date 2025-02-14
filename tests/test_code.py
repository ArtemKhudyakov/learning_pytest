import pytest
import utils.code as code


def test_up_first():
    assert code.up_first("ученье") == "Ученье"


def test_up_first_for_empty():
    assert code.up_first("") == ""


def test_up_first_for_space():
    assert code.up_first(" ") == " "


def test_reverse_string_numbers(numbers):
    assert code.reverse_string("123") == numbers


def test_reverse_string_letters(letters):
    assert code.reverse_string("hello") == letters


@pytest.mark.parametrize(
    "value, expected",
    [("123", "321"), ("321", "123"), ("world", "dlrow"), ("hello", "olleh")],
)
def test_reverse_string(value, expected):
    assert code.reverse_string(value) == expected

def test_el_type_count():
    assert code.el_type_count([1, '2', [], {}, ('3',)], int) == 1
    assert code.el_type_count([1, '2', [], {}, ('3',), 3], int) == 2
    assert code.el_type_count(['2', [], {}, ('3',)], int) == 0
    assert code.el_type_count([], str) == 0
    assert code.el_type_count(123456, int) == 0

