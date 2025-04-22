from typing import List

from ch06_school.error import StudentNotFoundException
from ch06_school.model.student import StudentResponse
from ch06_school.data import student as student_dao


def find_all() -> List[StudentResponse]:
    return student_dao.find_all()


def find_by_id(student_id) -> StudentResponse:
    _student = student_dao.find_by_id(student_id)
    if _student is None:
        raise StudentNotFoundException(student_id)
    return _student


def create(student):
    return student_dao.create(student)