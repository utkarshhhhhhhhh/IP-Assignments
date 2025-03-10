def factorial(n):
    prod=1 
    while n>0:
        prod=prod*n 
        n=n-1
    return prod
 
def angle(x):
    x=x*(3.14/180)
    return x
 
def Sum(x,n):
    Sum=0
    for i in range(0,n+1,1):
        Sum=Sum+((-1)**(i))*x**(2*i)/factorial(2*i)
    return Sum
    
x=int(input("Enter The Angle(in degrees): "))
base=int(input("Enter The Distance To The Base Of The Pole: "))
x=angle(x)
n=21
hypotenuse=base/Sum(x,n)
print(format(hypotenuse,".2f"))
height_of_pole=((hypotenuse)**2-(base)**2)**0.5
print(format(height_of_pole,".2f"))