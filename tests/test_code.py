import pytest
import utils.code as code

def test_up_first():
    assert code.up_first("ученье") == "Ученье"

def test_up_first_for_empty():
    assert code.up_first("") == ""

def test_up_first_for_space():
    assert code.up_first(" ") == " "

