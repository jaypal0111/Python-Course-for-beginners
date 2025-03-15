
class Human:
    def __init__(self, name, add, bloodGroup):
        self.name =  name
        self.add =  add
        self.bloodGroup = bloodGroup
    
    def getData(self):
        return (self.name, self.add, self.bloodGroup)

# H = Human("Jay","UK","A+")
# H.getData()

class Student(Human):
    def __init__(self,name, add, bloodGroup, marks):
      self.marks = marks
      super().__init__(name, add, bloodGroup)


    def getStudentData(self):

        return(self.marks)

    

S = Student("Urmi","USA","B+","86")

parentData = S.getData()
stuentData = S.getStudentData()

print(parentData, stuentData)

