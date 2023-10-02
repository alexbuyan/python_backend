import pytest
from app.main import app
from app.routers import fake_child_db, fake_parent_db
from fastapi.testclient import TestClient

client = TestClient(app)


def test_read_main():
    """Simple integration test example."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


@pytest.mark.parametrize(
    "p_id, expected_result",
    [(1, (200, fake_parent_db[1])), (56, (404, {"detail": "No parent with such id"}))],
)
def test_get_parent(p_id, expected_result):
    """Integration test for endpoint /parents/{p_id}."""
    response = client.get(f"/parents/{p_id}")
    assert response.status_code == expected_result[0]
    if response.status_code == 200:
        assert response.json() == vars(expected_result[1])
    else:
        assert response.json() == expected_result[1]


@pytest.mark.parametrize(
    "c_id, expected_result",
    [(1, (200, fake_child_db[1])), (105, (404, {"detail": "No child with such id"}))],
)
def test_get_child(c_id, expected_result):
    """Integration test for endpoint /children/{c_id}."""
    response = client.get(f"/children/{c_id}")
    assert response.status_code == expected_result[0]
    if response.status_code == 200:
        assert response.json() == vars(expected_result[1])
    else:
        assert response.json() == expected_result[1]


@pytest.mark.parametrize(
    "parent_info, expected_result",
    [
        (
            {"p_id": 56, "name": "Henry", "phone": "+79219000990"},
            (
                200,
                {
                    "p_id": 56,
                    "name": "Henry",
                    "phone": "+79219000990",
                    "children": [],
                },
            ),
        ),
        (
            {"p_id": 1, "name": "Henry", "phone": "+79219000990"},
            (400, {"detail": "Parent with this id already exists"}),
        ),
    ],
)
def test_post_parent(parent_info, expected_result):
    """Integration test for endpoint /parents/."""
    params = {
        "p_id": parent_info["p_id"],
        "name": parent_info["name"],
        "phone": parent_info["phone"],
    }
    response = client.post("/parents/", params=params)
    assert response.status_code == expected_result[0]
    assert response.json() == expected_result[1]


@pytest.mark.parametrize(
    "child_info, expected_result",
    [
        (
            {"c_id": 31, "name": "Horward", "age": 17},
            (
                200,
                {
                    "c_id": 31,
                    "name": "Horward",
                    "age": 17,
                    "interests": [],
                },
            ),
        ),
        (
            {"c_id": 1, "name": "Henry", "age": 3},
            (400, {"detail": "Child with this id already exists"}),
        ),
    ],
)
def test_post_child(child_info, expected_result):
    """Integration test for endpoint /children/."""
    params = {
        "c_id": child_info["c_id"],
        "name": child_info["name"],
        "age": child_info["age"],
    }
    response = client.post("/children/", params=params)
    assert response.status_code == expected_result[0]
    assert response.json() == expected_result[1]
