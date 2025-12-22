from pydantic import BaseModel
from typing import Optional

class CourseBase(BaseModel):
    name: str
    description: Optional[str] = None

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    id: int

    class Config:
        from_attributes = True

class StudentBase(BaseModel):
    name: str
    email: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int

    class Config:
        from_attributes = True

class EnrollmentBase(BaseModel):
    student_id: int
    course_id: int

class EnrollmentCreate(EnrollmentBase):
    pass

class Enrollment(EnrollmentBase):
    id: int

    class Config:
        from_attributes = True

class PerformanceBase(BaseModel):
    enrollment_id: int
    score: float

class PerformanceCreate(PerformanceBase):
    pass

class Performance(PerformanceBase):
    id: int

    class Config:
        from_attributes = True
