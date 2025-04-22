from typing import List

from fastapi import APIRouter, Path, HTTPException, Body
from starlette import status

from ch06_school.error import StudentNotFoundException
from ch06_school.model.student import StudentResponse, Student
from ch06_school.service import student as service

router = APIRouter(prefix="/students")

@router.get("")
def get_all() -> List[StudentResponse]:
    return service.find_all()

@router.get("/{student_id}")
def get_by_id(student_id: int = Path(...)) -> StudentResponse:
    try:
        return service.find_by_id(student_id)
    except StudentNotFoundException as e:
        raise HTTPException(status_code=404, detail=e.msg)

@router.post(path = "", status_code=status.HTTP_201_CREATED)
def create(student : Student = Body(...)):
    return service.create(student)