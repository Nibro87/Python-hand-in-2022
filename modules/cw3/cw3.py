import random
import string 

class Student():
    def __init__(self,name,gender,imgUrl,datasheet):
        self.name = name
        self.gender = gender
        self.imgUrl = imgUrl
        self.datasheet = datasheet

    def get_avg_grade(self):
        grades = []
        for value in self.datasheet.courses:
            grades.append((value.grade))
  
        return sum(grades)/len(grades)


    def student_generator(chars = string.ascii_letters + string.punctuation, N=10):
         return ''.join(random.choices(chars) for _ in range(N))

        


class Course():
    def __init__(self,name,classroom,teacher,ETCS,grade):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS
        self.grade = grade



class DataSheet():
    def __init__(self, courses):
        self.courses = courses


    def get_grades_as_list(self):
        grades = []
        for value in self.courses:
            grades.append((value.name, value.grade))
        return grades


if __name__ == '__main__':

    firstCourse = Course("python",105,"Thomas",15,12);
    secondCourse = Course("it sikkerhed",105,"Daniel",15,7);
    datasheet = DataSheet([firstCourse,secondCourse]);
    student = Student("Nicholas","Man","URL",datasheet)
  
    print(student.get_avg_grade())
    
    print(student.datasheet.get_grades_as_list())

    print(student.student_generator())

     

