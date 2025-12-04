import random

def get_temp():
    a= random.randint(10,40)
    return a

def average(x):
    top=0
    for i in range (0,len(x)):
        top=top+x[i]
    b= top/len(x)
    return b

def maximum(x):
    maxdata=0
    for i in range (0,len(x)):
        if maxdata < x[i]:
            maxdata=x[i]
    return(maxdata)
def minimum(x):
    mindata=0
    for i in range (0,len(x)):
        if mindata > x[i]:
            mindata=x[i]
    return(mindata)


temp_list=[]
for i in range (0,30):
    temp_list.append(get_temp())
a=0
for temp in temp_list:
    a=a+temp
y=average(temp_list)
t=maximum(temp_list)
r=minimum(temp_list)

print("total temp is ",a)
print("average temp is ",y)
print("minimum temp is ",r)
print("maximum temp is ",t)