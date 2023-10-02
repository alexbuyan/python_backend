from typing import List


class Child:
    """Class to store child information."""

    c_id: int
    name: str
    age: int
    interests: List[str]

    def __init__(self, c_id, name, age, interests=None):
        """Returns the entity of class Child.

        Args:
            c_id (int): child's id in the database
            name (str): name of the child
            age (int): child's age
            interests (List[str], optional): interests of this child. Defaults to [].
        """
        self.c_id = c_id
        self.name = name
        self.age = age
        self.interests = interests if interests else []


def get_child_group(child: Child):
    """Returns the child's group.

    Args:
        child (Child): child's information

    Returns:
        str: The group of the child
    """
    age = child.age
    if age < 6:
        return "Дошкольная группа"
    elif 6 <= age and age < 11:
        return "Младшая школа"
    elif 11 <= age and age < 13:
        return "Средняя школа"
    elif 13 <= age and age < 17:
        return "Старшая школа"
    else:
        return "Выпускник"


class Parent:
    """Class to store parent information."""

    p_id: int
    name: str
    phone: str
    children: List[Child]

    def __init__(self, p_id, name, phone, children=None):
        """Returns the entity of class Parent.

        Args:
            p_id (int): parent's id in the database
            name (str): name of the parent
            phone (str): parent's phone number
            children (List[Child], optional): children of this parent. Defaults to [].
        """
        self.p_id = p_id
        self.name = name
        self.phone = phone
        self.children = children if children else []


def validate_parent_phone(parent: Parent):
    """Returns True if parent's phone is valid.

    Args:
        parent (Parent): parent's information

    Returns:
        str: phone validation result and the validation message
    """
    parent_phone = parent.phone
    if not parent_phone.startswith("+7"):
        return (False, "Телефон должен начинаться с +7")
    if not len(parent_phone) == 12:
        return (False, "Телефон должен состоять из 12 знаков")
    return (True, "Телефон корректный")


def get_family_status(parent: Parent):
    """Returns family status.

    Args:
        parent (Parent): parent's information

    Returns:
        str: family status
    """
    childrens = len(parent.children)
    if childrens == 0:
        return "Молодая семья"
    elif 1 <= childrens and childrens < 3:
        return "Обычная семья"
    else:
        return "Многодетная семья"
