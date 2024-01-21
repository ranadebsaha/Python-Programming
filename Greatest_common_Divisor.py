def gcd(a,b):

    if(a>b): 

        for i in range(1,b+1):

            if(a%i==0 and b%i==0):

                m=i

                continue

        return m

    else: 

        for j in range(1,a+1):

            if(a%j==0 and b%j==0):

                n=j

                continue

        return n





print("Enter two numbers: ",end=' ')

a,b=[int(x) for x in input().split()]

print("The Greatest Common Divisor of this two number is: ",gcd(a,b)
