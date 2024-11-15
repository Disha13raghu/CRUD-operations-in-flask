from .database import db

class Student(db.Model):
    __tablename__ = 'student'
    student_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    roll_no= db.Column(db.String, nullable=False, unique= True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    
    enrollments = db.relationship('Enrollment', back_populates='student')

class Enrollment(db.Model):
    __tablename__ = 'enrollments'
    enrollment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    estudent_id = db.Column(db.Integer,db.ForeignKey("student.student_id", ondelete='CASCADE'), nullable=False)
    ecourse_id = db.Column(db.Integer,db.ForeignKey("course.course_id", ondelete='CASCADE'), nullable=False)
     
    student = db.relationship('Student', back_populates='enrollments')
    course = db.relationship('Course', back_populates='enrollments')

    
    

class Course(db.Model):
    __tablename__ = 'course'
    course_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_name = db.Column(db.String, nullable=False)
    course_description = db.Column(db.String)
    course_code = db.Column(db.String, nullable=False, unique=True)
     
   
    enrollments = db.relationship('Enrollment', back_populates='course')



