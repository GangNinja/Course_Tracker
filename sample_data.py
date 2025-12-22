from app.database import SessionLocal, engine, Base
import app.models  # IMPORTANT: this registers the models
from app import crud, schemas

# Create database tables
Base.metadata.create_all(bind=engine)

def create_sample_data():
    db = SessionLocal()
    try:
        # Create sample courses
        courses = [
            ("Mathematics", "Basic Math Course"),
            ("Physics", "Introduction to Physics"),
            ("Computer Science", "Programming Fundamentals"),
            ("Chemistry", "General Chemistry"),
            ("Biology", "Introduction to Biology"),
            ("History", "World History"),
            ("English Literature", "Classic Literature"),
            ("Statistics", "Applied Statistics"),
            ("Economics", "Micro and Macro Economics"),
            ("Psychology", "Introduction to Psychology"),
            ("Art History", "Western Art History"),
            ("Music Theory", "Fundamentals of Music Theory")
        ]

        created_courses = []
        for name, desc in courses:
            course = crud.create_course(db, schemas.CourseCreate(name=name, description=desc))
            created_courses.append(course)

        # Create sample students
        students_data = [
            ("Alice Johnson", "alice@example.com"),
            ("Bob Smith", "bob@example.com"),
            ("Charlie Brown", "charlie@example.com"),
            ("Diana Prince", "diana@example.com"),
            ("Edward Norton", "edward@example.com"),
            ("Fiona Green", "fiona@example.com"),
            ("George Wilson", "george@example.com"),
            ("Helen Troy", "helen@example.com"),
            ("Ian McGregor", "ian@example.com"),
            ("Julia Roberts", "julia@example.com"),
            ("Kevin Hart", "kevin@example.com"),
            ("Laura Palmer", "laura@example.com"),
            ("Michael Scott", "michael@example.com"),
            ("Nancy Drew", "nancy@example.com"),
            ("Oliver Twist", "oliver@example.com"),
            ("Pam Beesly", "pam@example.com"),
            ("Quincy Jones", "quincy@example.com"),
            ("Rachel Green", "rachel@example.com")
        ]

        created_students = []
        for name, email in students_data:
            student = crud.create_student(db, schemas.StudentCreate(name=name, email=email))
            created_students.append(student)

        # Create sample enrollments (more varied enrollments)
        enrollments = []
        enrollment_data = [
            (0, 0), (0, 1), (0, 2), (0, 3),  # Alice in Math, Physics, CS, Chemistry
            (1, 1), (1, 2), (1, 4),           # Bob in Physics, CS, Biology
            (2, 2), (2, 5), (2, 6),           # Charlie in CS, History, English
            (3, 3), (3, 4), (3, 7),           # Diana in Chemistry, Biology, Statistics
            (4, 0), (4, 1), (4, 7),           # Edward in Math, Physics, Statistics
            (5, 5), (5, 6), (5, 8),           # Fiona in History, English, Economics
            (6, 2), (6, 7), (6, 9),           # George in CS, Statistics, Psychology
            (7, 8), (7, 9), (7, 10),          # Helen in Economics, Psychology, Art History
            (8, 0), (8, 3), (8, 4),           # Ian in Math, Chemistry, Biology
            (9, 1), (9, 2), (9, 5),           # Julia in Physics, CS, History
            (10, 6), (10, 8), (10, 11),       # Kevin in English, Economics, Music Theory
            (11, 7), (11, 9), (11, 10),       # Laura in Statistics, Psychology, Art History
            (12, 0), (12, 2), (12, 4),        # Michael in Math, CS, Biology
            (13, 1), (13, 3), (13, 6),        # Nancy in Physics, Chemistry, English
            (14, 5), (14, 7), (14, 8),        # Oliver in History, Statistics, Economics
            (15, 9), (15, 10), (15, 11),      # Pam in Psychology, Art History, Music Theory
            (16, 0), (16, 1), (16, 2),        # Quincy in Math, Physics, CS
            (17, 3), (17, 4), (17, 5)         # Rachel in Chemistry, Biology, History
        ]

        for student_idx, course_idx in enrollment_data:
            enrollment = crud.create_enrollment(db, schemas.EnrollmentCreate(
                student_id=created_students[student_idx].id,
                course_id=created_courses[course_idx].id
            ))
            enrollments.append(enrollment)

        # Create sample performances with varied scores
        performance_scores = [
            85.0, 92.0, 78.0, 88.0,  # Original scores
            95.5, 87.2, 91.8, 76.4, 83.9, 89.1,  # More scores
            94.3, 82.7, 90.6, 79.8, 86.5, 93.2,
            81.4, 88.9, 96.1, 84.6, 87.8, 92.4,
            80.2, 89.7, 91.3, 85.9, 94.8, 77.5,
            90.4, 86.1, 93.7, 82.3, 88.6, 95.2,
            79.9, 87.4, 92.8, 84.1, 89.3, 91.7,
            86.8, 93.5, 81.6, 88.2, 90.9, 85.7,
            94.6, 83.4, 87.9, 92.1, 80.8, 89.5,
            91.2, 86.3, 88.7, 93.9, 82.9, 90.1,
            87.6, 94.4, 81.9, 89.8, 92.6, 85.3,
            90.8, 86.7, 93.1, 84.5, 88.4, 91.5,
            79.6, 87.1, 92.9, 83.8, 89.2, 90.7,
            86.9, 93.6, 82.1, 88.3, 91.4, 85.8,
            94.7, 84.2, 87.5, 92.3, 81.7, 89.6,
            90.5, 86.4, 88.8, 93.8, 83.2, 91.6,
            87.7, 94.5, 82.5, 89.9, 92.7, 85.4,
            90.3, 86.2, 93.4, 84.7, 88.5, 91.9,
            80.1, 87.3, 92.5, 84.3, 89.4, 91.8
        ]

        for i, enrollment in enumerate(enrollments):
            if i < len(performance_scores):
                crud.create_performance(db, schemas.PerformanceCreate(
                    enrollment_id=enrollment.id,
                    score=performance_scores[i]
                ))

        print(f"Sample data created successfully! Created {len(created_courses)} courses, {len(created_students)} students, {len(enrollments)} enrollments, and {len(performance_scores)} performances.")
    finally:
        db.close()

if __name__ == "__main__":
    create_sample_data()
