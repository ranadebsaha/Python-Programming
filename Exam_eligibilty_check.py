a=int(input("Enter Number of classes conducted by the Teacher: "))
b=int(input("Enter Number of classes attended by a Student: "))
c=(b/a)*100
if(c>=60):
    print("Student is Eligible for Final Semester.")
else:
    print("Student is Not Eligible for Final Semester.")
