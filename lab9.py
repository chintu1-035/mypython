'''f=open("C:\\Users\\Administrator\\Documents\\083\\python\\uppi.txt")
print("file object is opened")
print(f)
data=f.read()
print(data)'''

'''file_path="C:\\Users\\Administrator\\Documents\\083\\python\\uppi.txt"
with open(file_path,"w")as file:
          file.write("Hello,World\n")
          file.write("this is a sample txt")
          print("content written to",file_path)'''

'''f=open("C:\\Users\\Administrator\\Documents\\083\\python\\uppi.txt","r")
data=f.read()
print("total available characters in a given file is:",len(data))'''

'''f=open("C:\\Users\\Administrator\\Documents\\083\\python\\uppi.txt",'r')
data=f.read()
lw=data.split()
print("total no.of words in a given file is:",len(lw))
print("available words are:",lw)'''

'''f=open("C:\\Users\\Administrator\\Documents\\083\\python\\uppi.txt")
print("the file pointer is at byte:",f.tell())
content=f.read()
print("after reading the file pointer is at:",f.tell())'''

'''f=open("C:\\Users\\Administrator\\Documents\\083\\python\\uppi.txt",'r')
data=f.read()
lw=data.split()
d={}
for word in lw:
    if word not in d:
        d[word]=1
    else:
        d[word]=d[word+1]
print(d)'''

'''f=open("C:\\Users\\Administrator\\Documents\\083\\python\\uppi.txt",'r')
print("the file pointer is at byte:",f.tell())
f.seek(10)
print("after reading the file pointer is at:",f.tell())'''
    
