#to find factorial using recursion
#factorial(n)=n*factorial(n-1)
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
n=int(input("Enter a number: "))
print("factorial of",n,"is:",factorial(n))

 #count
def count(n):
    if n==0:
        return 
    count(n-1)
    print(f"total count #{n}")
n=int(input("enter a number: "))
count(n)