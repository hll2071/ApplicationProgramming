

from ch02.model import Champion, RoleEnum

_champions : list[Champion] = [
    Champion(
        id=1,
        name="베인",
        release_date = "2010-05-11",
        role = RoleEnum.TANK
    ),
    Champion(
        id=2,
        name="블리츠크랭크",
        release_date = "2009-09-02",
        role=RoleEnum.MARKSMAN
    )
]
def get_champions() -> list[Champion]:
    return _champions