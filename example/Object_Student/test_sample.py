from datetime import datetime
import pytest
from Obj.myapp.sample import Student

@pytest.fixture(scope = "module" )
def creat_student():
    print("Create student")
    return Student("Alla", "Markovich", datetime(1998,1,1))

def test_get_age(creat_student):
    creat_student_age = (datetime.now() - creat_student.dr).days//365
    assert creat_student.get_age() ==  creat_student_age

def test_add_mark(creat_student):
    creat_student.add_mark(8)
    assert creat_student.get_mark() == 8

def test_get_mark(creat_student):
    assert creat_student.get_mark() == 0










