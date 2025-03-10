import math
def Function(x):
    return x**3 - 10.5*x**2 + 34.5*x - 35
def Derivative_Function(x):
    return 3*x**2 - 21*x + 34.5 
def Newton_Raphson(x):
    x1 = Function(x) / Derivative_Function(x)
    while abs(x1) >= 0.0001:
        x1 = Function(x)/Derivative_Function(x)
        x = x - x1
    print("The value of the root is : ", format(x,".2f"))
x0 = int(input())
Newton_Raphson(x0)