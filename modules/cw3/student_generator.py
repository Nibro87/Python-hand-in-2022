import platform
from string import ascii_letters, ascii_uppercase
from typing import List
import names 
import random
from DataSheet import DataSheet
from Student import Student
from Course import Course
import csv

name_female = ["Tine","Camilla","Mette","Jette"]
name_male = ["Nicholas","Tim","Niels","Martin"]
course_name = ["It sikkerhed","Python","OOA","game devlopment"]
genders = ["male","female"]


def generate_students(num: int):
    students = []
    for i in range(num):
        gender = random.choice(genders)
        if gender is "male":
               name = random.sample(name_male,num)
        elif gender is "female":
            name = random.sample(name_female,num)    
    courses = generate_courses(4)
    img_url = "".join(random.choices(ascii_letters,k=8))
    students.append(Student(name,gender,DataSheet(courses),img_url))
          
    return students


def generate_courses(num: int):
    courses = []
    names = random.sample(course_name,num)
    for name in names:
        classroom = random.randint(101,399)
        teacher = "".join(random.choices(ascii_uppercase,k=2))
        ETCS = random.choice([10,15,20,30])
        grade = random.choice([-3,0,2,4,7,10,12])
        courses.append(Course(name,classroom,teacher,ETCS,grade))

    return courses

def students_to_csv(students):
    
    if platform.system() is "Windows":
            newline = ""
    else:
        newline = None

    with open("students.csv", "w", newline=newline) as file:
        
        writer = csv.writer(file)
        writer.writerow(["stud_name", "course_name", "teacher", "gender", "ects", "classroom", "grade", "img_url"])
        for s in students:
            for c in s.data_sheet.courses:
                writer.writerow([s.name, c.name, c.teacher, s.gender, c.ETCS, c.classroom, c.grade, s.img_url])

if __name__ == "__main__":
    student = generate_students(1)

    students_to_csv(student)
