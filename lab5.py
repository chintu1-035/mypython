'''def fibonacci(number):
    if(number==0):
        return 0
    elif number==1:
        return 1
    else:
        return fibonacci(number-2)+fibonacci(number-1)
number=int(input("please enter the fibonacci number range="))
sum=0
for num in range (number):
        print(fibonacci(num),end=' ')
        sum=sum+fibonacci(num)
print("\n the sum of fibonacci series numbers=%d%",sum)'''

'''def factorial(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("enter any number:"))
print("factorial value of 1,n,is:",factorial(n))'''

'''def pal(s):
    s=s.lower()
    if len(s)<=1:
        return True
    elif s[0]!=s[-1]:
        return False
    else:
        return pal(s[1:-1])
my_input=input("enter a string:")
if pal(my_input):
    print(f"{my_input} is a palindrome")
else:
    print(f"{my_input} is a not polindrome")'''

'''def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
x=input("enter the first integer:")
y=input("enter the second integer:")
if x. isdigit() and y. isdigit():
    a=int(x)
    b=int(y)
    result=gcd(a,b)
    print(f"the gcd of {a} and {b} is:",result)
else:
    print(f"please enter valid integers")'''
