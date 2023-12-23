a=int(input("Enter a Year: "))
if(a%100==0 and a%400==0):
    print("This is a Leap Year.")
elif(a%100!=0 and a%4==0):
    print("This is a Leap Year.")
else:
    print("This is not a Leap Year.")
