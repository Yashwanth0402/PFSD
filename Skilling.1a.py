#Chiluka yashwanth
#id number 190030311
#KL University
class Students:
    count=0
    def __init__ (self, sid, firstname, lastname,course,year, gpa, university, mobile):
        self.sid = sid
        self.firstname=firstname
        self.lastname = lastname
        self.course = course
        self.year = year
        self.gpa = gpa
        self.university = university
        #self.email= firstname+ lastname + '@gmail.com'
        self.mobile = mobile
        Students.count+=1
        
    def email(self):
        return (self.firstname + self.lastname+ '@gmail.com')
        
student_1 = Students(190032421,'yashwanth','chiluka','CSE',2019,9.4,'KLU',8309999999)
student_2 = Students(190031825,'sasuke','uchiha','ECE',2019,9.6,'KLU',8674858487)
student_3 = Students(190030322,'Naruto','Uzumaki','CSE',2019,10,'KLU',9649538390)

print(student_1.sid)
print(student_1.firstname , student_1.lastname)
print(student_1.course)
print( student_1.year)
print(student_1.gpa)
print(student_1.university)
print(student_1.mobile)
print(student_1.email()+'\n'+'')


print(student_2.sid)
print(student_2.firstname , student_1.lastname)
print(student_2.course)
print( student_2.year)
print(student_2.gpa)
print(student_2.university)
print(student_2.mobile)
print(student_2.email()+'\n'+'')

print(student_3.sid)
print(student_3.firstname , student_1.lastname)
print(student_3.course)
print(student_3.year)
print(student_3.gpa)
print(student_3.university)
print(student_3.mobile)
print(student_3.email()+'\n'+'')

print('the total number of instance=',Students.count)
