from typing import Optional

from pydantic import BaseModel

#생성용 Model
class Department(BaseModel) :
    name : str
    quota : int
    description : Optional[str] = None

#응답용 Model
class DepartmentResponse(Department) :
    id : int

# Student에서 사용
class DepartmentName(BaseModel):
    name : Optional[str]