from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Course(db.Model):
    __tablename__ = "courses"
    id = db.Column(db.Integer, primary_key=True)
    course_number = db.Column(db.String(10))
    course_title = db.Column(db.String)
    student = db.relationship("RegisteredStudent", backref="courses", lazy=True)


class RegisteredStudent(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    grade = db.Column(db.Integer)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
