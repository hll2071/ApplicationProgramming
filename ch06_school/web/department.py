from starlette import status

from ch06_school.error import Duplicate, Missing
from ch06_school.model.department import Department, DepartmentResponse
from ch06_school.data import department as data

from typing import List

from fastapi import APIRouter, Path, HTTPException, Body

router = APIRouter(prefix="/departments")


# 학과 전체 검색
@router.get("")
def get_all() -> List[DepartmentResponse]:
    return data.find_all()


@router.get("/{dept_id}", status_code=status.HTTP_200_OK)
def get_by_id(dept_id: int = Path(...)) -> DepartmentResponse:
    from ch06_school.error import Missing
    try:
        return data.find_by_id(dept_id)
    except Missing as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

# 학과 생성 ( ai 학과 )
@router.post(path = "", status_code=status.HTTP_201_CREATED)
def create(department : Department = Body(...)):
    try :
        data.create(department)
    except Duplicate as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))

# 업데이트
@router.patch("/{dept_id}", status_code=status.HTTP_200_OK)
def update(dept_id: int = Path(...), department : Department = Body(...)):
    try:
        return data.update(dept_id, department)
    except Missing as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.delete("/{dept_id}")
def delete(dept_id: int = Path(...)):
    try:
        return data.delete(dept_id)
    except Missing as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))