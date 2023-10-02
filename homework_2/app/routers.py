import random

from app.contractors import Child, Parent
from fastapi import APIRouter, HTTPException

router = APIRouter()

fake_child_db = {
    1: Child(1, "Alex", 5),
    2: Child(2, "Ivan", 7),
    3: Child(3, "Anya", 9),
    4: Child(4, "Dima", 11),
    5: Child(5, "Andrey", 13),
}


def generate_phone():
    """Function returns random phone number."""
    ten_numbers = [random.randint(0, 9) for _ in range(10)]
    return "+7{}{}{}{}{}{}{}{}{}{}".format(*ten_numbers)


fake_parent_db = {
    1: Parent(1, "Alexey", generate_phone()),
    2: Parent(2, "Alena", generate_phone(), [fake_child_db[1], fake_child_db[2]]),
    3: Parent(3, "Anastasia", generate_phone(), [fake_child_db[5]]),
    4: Parent(4, "Elena", generate_phone(), [fake_child_db[3]]),
    5: Parent(5, "Petr", generate_phone(), [fake_child_db[4]]),
}


@router.get("/")
async def read_root():
    """Endpoint for Hello World."""
    return {"Hello": "World"}


@router.get("/parents/{p_id}")
async def get_parent(p_id: int):
    """Returns parent's info from the database.

    Args:
        p_id (int): id of the parent in the database
    """
    if p_id not in fake_parent_db:
        raise HTTPException(status_code=404, detail="No parent with such id")
    return fake_parent_db.get(p_id)


@router.get("/children/{c_id}")
async def get_child(c_id: int):
    """Returns child's info from the database.

    Args:
        c_id (int): id of the child in the database
    """
    if c_id not in fake_child_db:
        raise HTTPException(status_code=404, detail="No child with such id")
    return fake_child_db.get(c_id)


@router.post("/parents/")
async def post_parent(p_id: int, name: str, phone: str):
    """Adds the parent to the database.

    Args:
        parent (Parent): parent's info
    """
    if p_id in fake_parent_db:
        raise HTTPException(
            status_code=400, detail="Parent with this id already exists"
        )
    parent = Parent(p_id, name, phone)
    fake_parent_db[p_id] = parent
    return parent


@router.post("/children/")
async def post_child(c_id: int, name: str, age: int):
    """Adds the child to the database.

    Args:
        child (Child): child's info
    """
    if c_id in fake_child_db:
        raise HTTPException(status_code=400, detail="Child with this id already exists")
    child = Child(c_id, name, age)
    fake_child_db[c_id] = child
    return child
