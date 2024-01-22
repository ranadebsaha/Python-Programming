def palindrome(a):

    r=0

    e=a

    while(a!=0):

        b=a%10

        r=r*10+b

        a=a//10

    if(e==r):

        print("This is a Palindrome Number.")

    else:

        print("This is not a Palindrome Number.")


a=int(input("Enter a number: "))

palindrome(a)  
