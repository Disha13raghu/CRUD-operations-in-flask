from flask import Flask, request, render_template, redirect, url_for
from applications.models import Student, Enrollment, Course
import os
from flask import current_app as app
from applications.database import db
import traceback

@ app.route('/')
def home():
    stud = Student.query.all()
    num = len(stud)
    return render_template("index.html", students=stud, n=num)

@ app.route('/student/create', methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html", n=2)
    else:
        roll = request.form.get("roll")
        fn = request.form.get("f_name")
        ln = request.form.get("l_name") 
        cou = request.form.getlist("courses")

        existing = Student.query.filter_by(roll_no=roll).first()  
        if existing:   
            return render_template("add.html", n=0)  
        else:
            new_student = Student(roll_no=roll, first_name=fn, last_name=ln) 
            db.session.add(new_student)
            db.session.commit()
            nid=new_student.student_id
            for i in cou:
                nenrollment= Enrollment(estudent_id=nid,ecourse_id=i)
                db.session.add(nenrollment)
            db.session.commit()
            return redirect("/")


@ app.route("/student/<int:student_id>/update", methods=["GET","POST"]) 
def update(student_id) :

  stu= Student.query.filter_by(student_id=student_id).first()
  allc= Enrollment.query.filter_by(estudent_id=student_id)
  old_course=[]
  for i in allc:
    old_course.append(i.ecourse_id)


     
  if request.method=="POST":
      fn=request.form.get("f_name")
      ln=request.form.get("l_name")
      courses=request.form.getlist("courses")
      stu.first_name=fn 
      stu.last_name= ln 

      Enrollment.query.filter_by(estudent_id=stu.student_id).delete()

      for c in courses:
  
        ne= Enrollment(estudent_id=stu.student_id, ecourse_id=c)
        db.session.add(ne)
      db.session.commit()    
      return redirect("/")
  return render_template("update.html",st=stu, course_names=old_course)

@ app.route("/student/<int:student_id>/delete", methods=["GET"])
def delete(student_id):
    item=Student.query.filter_by(student_id=student_id).first()
    item_enroll= Enrollment.query.filter_by(estudent_id=student_id).all()
    for i in item_enroll:
        db.session.delete(i)
    db.session.delete(item)
    db.session.commit()
    return(redirect("/"))

@app.route("/student/<int:student_id>", methods=["GET"])
def enroll(student_id):
    # Get all enrollments for the student
    enrolls = Enrollment.query.filter_by(estudent_id=student_id).all()

    # Initialize an empty list for courses
    course = []

    # For each enrollment, fetch the corresponding course
    for enrollment in enrolls:
        course_instance = Course.query.filter_by(course_id=enrollment.ecourse_id).first()
        if course_instance:
            course.append(course_instance)

    # Fetch student details
    stu = Student.query.filter_by(student_id=student_id).first()

    # Return the template with courses and student details
    return render_template("enroll.html", c=course, stu=stu)






