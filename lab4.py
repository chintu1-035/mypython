'''def gcd(a,b):
    while b!=0:
        a,b=b,a%b
        return a
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
result=gcd(num1,num2)
print("the gcd of",num1,"and",num2,"is",result)'''

'''def check_even_odd(number):
    if number%2==0:
        return"even"
    else:
        return"odd"
num=int(input("enter a number:"))
result=check_even_odd(num)
print("the number is",result)'''

'''def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
for i in range(1,11):
        result = factorial(i)
        print("factorial of", i , "is",result)'''

'''def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("enter a number:"))
result=factorial(num)
print("the factorial of",num,"is",result)'''

'''def calculate_sum(numbers):
    total=0
    for num in numbers:
        total +=num
    return total
list=[]
n=int(input("enter the number of elements in the list:"))
for i in range(n):
    num=eval(input("enter element{}:".format(i+1)))
    list.append(num)
    result=calculate_sum(list)
print("the sum of the list is:",result)'''

'''def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiplicity(x,y):
    return x*y
def divide(x,y):
    return x/y
num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
print("addition:",add(num1,num2))
print("subtraction:",subtract(num1,num2))
print("multiplication:",multiplicity(num1,num2))
print("division:",divide(num1,num2))'''
