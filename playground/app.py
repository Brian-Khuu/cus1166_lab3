import sys
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import *

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


@app.route('/', methods=['GET'])
def index():
    courses = Course.query.all()
    return render_template('index.html', title='Index', courses=courses)


@app.route('/add_course', methods=['POST'])
def course():
    number = request.form.get("course_number")
    name = request.form.get("course_title")
    addCourse = Course(course_number=number, course_title=name)
    db.session.add(addCourse)
    db.session.commit()
    courses = Course.query.all()
    return render_template('index.html', number=number, name=name, courses=courses)


@app.route('/register_student/<int:course_id>', methods=['GET', 'POST'])
def register_student(course_id):
    course = Course.query.get(course_id)
    if request.method == "POST":
        studentName = request.form.get("student_name")
        studentGrade = request.form.get("student_grade")
        addStudent = RegisteredStudent(name=studentName, grade=studentGrade, course_id=course_id)
        db.session.add(addStudent)
        db.session.commit()

    students = course.student
    return render_template('course_details.html', students=students, course=course, course_id=course_id)


def main():
    if len(sys.argv) == 2:
        print(sys.argv)
        if sys.argv[1] == 'createdb':
            db.create_all()
    else:
        print("Run app using 'flask run'")
        print("To create a database use 'python app.py createdb")


if __name__ == "__main__":
    with app.app_context():
        main()
