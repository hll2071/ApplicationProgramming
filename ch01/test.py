from typing import List, Tuple, Dict, Optional, Union


def add(a: int, b: int) -> int:
    return a+b

# 입력 받은 리스트 값들을 순회하면서 2를 곱한 결과를 리턴
def process_numbers(numbers: List[int]) -> List[int]:
    return [n*2 for n in numbers]

# 튜플 (자료형,자료형)
def get_person_info() -> Tuple[str,int]:
    return ("hwang",18)

# 딕셔너리
def get_student_score() -> Dict[str,float]:
    return {"hwang": 10,"kim":1}

#
def find_user(user_id: int) -> Optional[str] :
    users = {1:"choi",2:"kim",3:"hwang"}
    return users.get(user_id)

def union_test(value: Union[int,str]) ->int:
    if isinstance(value,int):
        return value ** 2
    return len(value)


if __name__ == '__main__':
    result1 = add(1,2)
    result2 = add("1","2")
    print(result1)
    print(result2)
    print(process_numbers([1,2,3]))
    print(get_person_info())
    print(get_student_score())
    print(find_user(1))
    print(union_test("hello world"))
    print(union_test(3))