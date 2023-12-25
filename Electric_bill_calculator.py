Write a program to input electricity unit charges and calculate total electricity bill according to the given condition:
For first 50 units Rs. 0.50/unit
For next 100 units Rs. 0.75/unit
For next 100 units Rs. 1.20/unit
For unit above 250 Rs. 1.50/unit
An additional surcharge of 20% is added to the bill
Input:--
a=int(input("Enter Electricity unit: "))
if(a<=50):
    b=a*0.5
elif(a<=150):
    b=(50*0.5)+(a-50)*0.75
elif(a<=250):
    b=(50*0.5)+(100*0.75)+(a-150)*1.2
else:
    b=(50*0.5)+(100*0.75)+(100*1.20)+(a-250)*1.5
s=(b*20)/100
t=b+s
print("Total Bill= ",t)
