

class Student():

    


    def __init__ (self,name,gender,data_sheet,img_url):
        self.name = name
        self.gender = gender
        self.img_url = img_url
        self.data_sheet = data_sheet
        

    
    def get_avg_grade(self):
        grades = []
        for g in self.data_sheet.courses:
            grades.append((g.grade))
         
        return sum(grades)/len(grades)
        
         