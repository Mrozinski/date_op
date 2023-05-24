import pytest
from scr.dateop import date_check, date_diff

def test_date_check_1():
    res = date_check("01012020")
    assert res == True

def test_date_check_2():
    res = date_check("01132020")
    assert res == False

def test_date_check_3():
    res = date_check("40102020")
    assert res == False

def test_date_check_4():
    res = date_check("4012020")
    assert res == False

def test_date_diff_1():
    res = date_diff("22031981", "24052023")
    valid_res = 15403
    assert res == valid_res

def test_date_diff_2():
    res = date_diff("24052023", "24052023")
    valid_res = 0
    assert res == valid_res

def test_date_diff_3():
    res = date_diff("22/03/1981", "24/05/2023", date_format="%d/%m/%Y")
    valid_res = 15403
    assert res == valid_res

def test_date_diff_4():
    res = date_diff("24-05-2023", "24-05-2023", date_format="%d-%m-%Y")
    valid_res = 0
    assert res == valid_res