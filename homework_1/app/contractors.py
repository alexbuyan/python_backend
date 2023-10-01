from pydantic import BaseModel


class Student(BaseModel):
    """Class to save student's information."""

    student_id: int | None = None
    name: str
    email: str
