
class DataSheet():

    def __init__(self,courses):
        self.courses = courses



    def get_grades_as_list(self):
        grades =[]

        for g in self.courses:
            grades.append((g.name,g.grade))

            return grades    

            