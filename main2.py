#its python project






n=int(input("Enter a Number : "))
fact=1;
if n==0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,n+1):
        fact*=i
    print("the factorial of ",n," is ",fact)
