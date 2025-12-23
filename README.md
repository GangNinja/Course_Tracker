# Course_Tracker
A full-stack Course Tracker application developed with FastAPI and SQLAlchemy, featuring complete CRUD operations for courses, enrollments, and student performance. Includes an interactive Dash-based analytics dashboard for real-time insights and performance visualization.




Arrange the file in this directory order

course_tracker/
│

├── app/

│   ├── __init__.py

│   ├── main.py

│   ├── database.py

│   ├── models.py

│   ├── schemas.py

│   └── crud.py

│
├── dashboard/

│  | └── dashboard.py

│
├── requirements.txt

├── sample_data.py

└── README.md

then after opening the Course_tracker file 
go to the terminal in vscode and create a virtual environment
-----------------------------------------------------------------------------
steps to create virtual environment

run this command in vs code terminal

python -m venv .venv    
#this will create the virtual environment

.\.venv\Scripts\Activate.ps1 

#this will activate the virtual environment

pip install -r requirements.txt
#this will install the required libraries for virtual environment

----------------------------------------------------------------------------


Now go to the file sample_data.py and run it or run this in terminal "python sample_data.py"

Now go to the dashboard.py and run it you will see Dash is running on http://127.0.0.1:8050/

Now create new terminal in vscode and run "python -m uvicorn app.main:app" this in terminal then you will see Uvicorn running on http://127.0.0.1:8000


----------------------------------------------------------------------------


this means your code is working properly

Go to http://127.0.0.1:8000/docs for API Documentation after running the above mentioned steps



----------------------------------------------------------------------------

## Objectives

- To design and implement a RESTful backend using FastAPI
- To manage academic data using a relational database
- To perform CRUD operations on courses, students, and enrollments
- To analyze student performance using interactive dashboards
- To demonstrate advanced programming and database concepts


## Technology Stack

- Backend Framework: FastAPI
- Programming Language: Python
- Database: SQLite (easily extendable to PostgreSQL)
- ORM: SQLAlchemy
- Dashboard & Visualization: Dash, Plotly
- API Documentation: Swagger UI


## Features

### Backend Features
- Create, read, update, and delete courses
- Manage student enrollments
- Track individual student performance
- RESTful API architecture
- Automatic API documentation (Swagger)

### Dashboard Features
- Course-wise performance visualization
- Student progress tracking
- Interactive charts and analytics
- Real-time data reflection




## Project Architecture

- FastAPI handles backend logic and API endpoints
- SQLAlchemy manages database interactions
- Dash reads data and renders interactive dashboards
- SQLite stores all academic records
- Modular structure ensures maintainability and scalability


