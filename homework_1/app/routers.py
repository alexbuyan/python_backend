from app.contractors import Student
from fastapi import APIRouter

router = APIRouter()

students = []


@router.get("/")
async def read_root():
    """Endpoint for Hello World."""
    return {"Hello": "World"}


@router.get("/students/{student_id}")
async def read_student_info(student_id: int, include_email: bool | None = True):
    """Endpoint to get student's information.

    Args:
        student_id (int): student_id in the database
        include_email (bool | None, optional): Whether to include email in the output.
                                               Defaults to True.

    Returns:
        Students info
    """
    if student_id >= len(students):
        return {"error": "No user with such id"}
    student_info = students[student_id]
    name = student_info["name"]
    email = student_info["email"]
    if not include_email:
        return {"name": name}
    return {"name": name, "email": email}


@router.post("/students/")
async def register_student(student: Student):
    """Endpoint to register student to the database.

    Args:
        student (Student): student's information for registration

    Returns:
        Registered student's information
    """
    student_dict = student.model_dump()
    if not student.id:
        student_dict.update({"id": len(students)})
        students.append(student_dict)
    return student_dict
