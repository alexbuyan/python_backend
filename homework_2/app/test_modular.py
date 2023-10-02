import pytest
from app.contractors import (
    Child,
    Parent,
    get_child_group,
    get_family_status,
    validate_parent_phone,
)


@pytest.fixture
def child():
    """Fixture for child."""
    return Child(0, "Alexander", 0)


@pytest.fixture
def parent():
    """Fixture for parent."""
    return Parent(0, "Ivan", "+79999999999")


@pytest.mark.parametrize(
    "age, expected_result",
    [
        (3, "Дошкольная группа"),
        (10, "Младшая школа"),
        (12, "Средняя школа"),
        (15, "Старшая школа"),
        (18, "Выпускник"),
    ],
)
def test_get_child_group(child, age, expected_result):
    """Test for function get_child_group()."""
    child.age = age
    result = get_child_group(child)
    assert result == expected_result


@pytest.mark.parametrize(
    "phone, expected_result",
    [
        ("+79211234567", (True, "Телефон корректный")),
        ("89211234567", (False, "Телефон должен начинаться с +7")),
        ("+7903920390390239029302", (False, "Телефон должен состоять из 12 знаков")),
    ],
)
def test_validate_parent_phone(parent, phone, expected_result):
    """Test for function get_child_group()."""
    parent.phone = phone
    result = validate_parent_phone(parent)
    assert result == expected_result


@pytest.mark.parametrize(
    "children, expected_result",
    [
        ([], "Молодая семья"),
        ([Child(0, "Alex", 5)] * 2, "Обычная семья"),
        ([Child(0, "Alex", 5)] * 4, "Многодетная семья"),
    ],
)
def test_get_family_status(parent, children, expected_result):
    """Test for function get_family_status()."""
    parent.children = children
    result = get_family_status(parent)
    assert result == expected_result
