""" 
Write a program to input basic salary of an employee and calculate its Gross salary (Basic Salary + HRA + DA) according to following:
Basic Salary <= 10000 : HRA = 20%, DA = 80%
Basic Salary <= 20000 : HRA = 25%, DA = 90%
Basic Salary > 20000 : HRA = 30%, DA = 95%
"""
a=int(input("Enter a Basic Salary: "))
if(a<=10000):
    HRA=(a*20)/100
    DA=(a*80)/100
elif(a<=20000):
    HRA=(a*25)/100
    DA=(a*90)/100
else:
    HRA=(a*30)/100
    DA=(a*95)/100
T=a+HRA+DA
print("Gross Salary:",T)
