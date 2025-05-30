# class student:
#     def __init__(self, rollno, name):
#         self.rollno = rollno
#         self.name = name
#     def giveMarks(self):
#         self.sub1 = int(input("Enter subject1 marks"))
#         self.sub2 = int(input("Enter subject2 marks"))
#         self.sub3 = int(input("Enter subject3 marks"))
#     def display(self):
#         print(self.sub1)
#         print (self.sub2)
#         print(self.sub3) 
#     def avgMarks(self):
#         self.avgMarks = (self.sub1 + self.sub2 + self.sub3)/3 
#         print(self.avgMarks)

# std1 = student("1", "student1")
# print("std rollnumber is", std1.rollno)
# print("std name is ", std1.name)
# std1.giveMarks()
# std1.display()
# std1. avgMarks()

class student:
    def __init__(self):
        self. r = int(input("Enter student rollnumber"))
        self.name = input("Enter name")
    def giveMarks(self):
        Marks = input("Enter 3 subject marks")
        self.marks = list(map(int, Marks.split()))
    def display(self):
        print(self.r, self.name, self.marks)
    
s1 = student()
s1. giveMarks()
s1.display()
