from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal, engine, Base
import app.models  # IMPORTANT: this registers the models
from app import crud, schemas

app = FastAPI(title="Course Tracker API")

# Create database tables
Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"status": "running"}

# Course routes
@app.post("/courses/", response_model=schemas.Course)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    return crud.create_course(db=db, course=course)

@app.get("/courses/", response_model=List[schemas.Course])
def read_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    courses = crud.get_courses(db, skip=skip, limit=limit)
    return courses

@app.get("/courses/{course_id}", response_model=schemas.Course)
def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course

@app.put("/courses/{course_id}", response_model=schemas.Course)
def update_course(course_id: int, course: schemas.CourseCreate, db: Session = Depends(get_db)):
    db_course = crud.update_course(db, course_id=course_id, course=course)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course

@app.delete("/courses/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.delete_course(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return {"message": "Course deleted"}

# Student routes
@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db=db, student=student)

@app.get("/students/", response_model=List[schemas.Student])
def read_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = crud.get_students(db, skip=skip, limit=limit)
    return students

@app.get("/students/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@app.put("/students/{student_id}", response_model=schemas.Student)
def update_student(student_id: int, student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = crud.update_student(db, student_id=student_id, student=student)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.delete_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted"}

# Enrollment routes
@app.post("/enrollments/", response_model=schemas.Enrollment)
def create_enrollment(enrollment: schemas.EnrollmentCreate, db: Session = Depends(get_db)):
    return crud.create_enrollment(db=db, enrollment=enrollment)

@app.get("/enrollments/", response_model=List[schemas.Enrollment])
def read_enrollments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    enrollments = crud.get_enrollments(db, skip=skip, limit=limit)
    return enrollments

@app.get("/enrollments/{enrollment_id}", response_model=schemas.Enrollment)
def read_enrollment(enrollment_id: int, db: Session = Depends(get_db)):
    db_enrollment = crud.get_enrollment(db, enrollment_id=enrollment_id)
    if db_enrollment is None:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return db_enrollment

@app.put("/enrollments/{enrollment_id}", response_model=schemas.Enrollment)
def update_enrollment(enrollment_id: int, enrollment: schemas.EnrollmentCreate, db: Session = Depends(get_db)):
    db_enrollment = crud.update_enrollment(db, enrollment_id=enrollment_id, enrollment=enrollment)
    if db_enrollment is None:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return db_enrollment

@app.delete("/enrollments/{enrollment_id}")
def delete_enrollment(enrollment_id: int, db: Session = Depends(get_db)):
    db_enrollment = crud.delete_enrollment(db, enrollment_id=enrollment_id)
    if db_enrollment is None:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return {"message": "Enrollment deleted"}

# Performance routes
@app.post("/performances/", response_model=schemas.Performance)
def create_performance(performance: schemas.PerformanceCreate, db: Session = Depends(get_db)):
    return crud.create_performance(db=db, performance=performance)

@app.get("/performances/", response_model=List[schemas.Performance])
def read_performances(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    performances = crud.get_performances(db, skip=skip, limit=limit)
    return performances

@app.get("/performances/{performance_id}", response_model=schemas.Performance)
def read_performance(performance_id: int, db: Session = Depends(get_db)):
    db_performance = crud.get_performance(db, performance_id=performance_id)
    if db_performance is None:
        raise HTTPException(status_code=404, detail="Performance not found")
    return db_performance

@app.put("/performances/{performance_id}", response_model=schemas.Performance)
def update_performance(performance_id: int, performance: schemas.PerformanceCreate, db: Session = Depends(get_db)):
    db_performance = crud.update_performance(db, performance_id=performance_id, performance=performance)
    if db_performance is None:
        raise HTTPException(status_code=404, detail="Performance not found")
    return db_performance

@app.delete("/performances/{performance_id}")
def delete_performance(performance_id: int, db: Session = Depends(get_db)):
    db_performance = crud.delete_performance(db, performance_id=performance_id)
    if db_performance is None:
        raise HTTPException(status_code=404, detail="Performance not found")
    return {"message": "Performance deleted"}
