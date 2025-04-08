# 클래스 정의
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class User(BaseModel) :
    id : int
    name : str
    age: int
    email : str

class Product(BaseModel) :
    name : str = Field(..., min_length=4, max_length=10)
    price : float = Field(..., gt=10,le=100)
    stock : Optional[int] = 10

class Event(BaseModel) :
    name : str
    start_time : datetime

class AdminUser(User) :
    role : str = "admin"

if __name__ == '__main__':
    user1  = User(id = 1, name="hong", age=46,email="hong@bssm.hs.kr")
    print(user1)

    p1 = Product(name="맥북프로", price=100)
    print(p1)

    e1 = Event(name ="Algorithm Competition", start_time="2025-06-25")
    print(e1)

    Admin = AdminUser(id = 2, name = "hwang", age=7, email="24.062@bssm.hs.kr")
    print(Admin)