'''d1={10:"python",20:"java"}
d2={30:"c",40:"ruby"}
d3=d1,d2
print(d3)
print(type(d3))'''

'''d={'apple':5,'banana':10,'orange':8}
for k in d:
    print(k)
for v in d.values():
    print(v)
for k,v in d.items():
    print(k,"----->",k)'''

'''fruits={'apple','banana','orange'}
fruits_dict={fruit:index for index,fruit in enumerate(fruits)}
print(fruits_dict)'''

'''d={'apple':5,'banana':10,'orange':8,'mango':15}
kd=['apple','banana']
for k in kd:
    if k in d:
        del d[k]
print(d)'''

'''d1={'sub1':80,'sub2':90,'sub3':70,'sub4':80}
print(d1)
s=sum(d1.values())
print(s)
mx=max(d1.values())
print(mx)
mn=min(d1.values())
print(mn)
cnt=len(d1.values())
print(cnt)'''
