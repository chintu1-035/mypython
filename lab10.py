'''try:
    x=10/0
except Exception as e:
    print("an errror occure:",str(e))'''

'''try:
    num=int(input("enter a number:"))
    result=10/num
    print("result:",result)
except valueerror:
    print("error:invali input!please enter a valid number:")
except zeroDivisionError:
    print("error:division by zero!")'''

'''try:
    num=int(input("enter a number:"))
    result=10/num
except valueerror:
    print("error:invalid input!please enter a valid number")
except zeroDivisionerror:
    print("error:division by zero!")
else:
    print("result:",result)'''

'''try:
    file=open("myfile.txt",'r')
except IOerror:
    print("error :unable to read the file!")
finally:
    file.close()'''

'''try:
    x=int(input("enter a number upto 100:"))
    if x>100:
        raise valuEerror(x)
except valueError:
    print(x,"is out of the range")
else:
    print(x,"is within the allowed range")'''
    


