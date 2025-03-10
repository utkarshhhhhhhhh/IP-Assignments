import math
def velocity(temp):
    v=(2000)*(math.log((140000)/(140000-2100*temp)))-(9.8)*(temp)
    return v 
a=int(input())
b=int(input())
temp=a
dist=0
while temp<b:
    c=velocity(temp)
    d=velocity(temp+0.25)
    avg1=(c+d)/2
    dist+=(avg1)*(0.25)
    temp+=0.25 
print(dist)