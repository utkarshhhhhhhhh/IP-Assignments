import math
def ln_demand(p):
    Dp=(10-1.05*p)
    return Dp 
def ln_supply(p):
    Sp=(1+1.06*p)
    return Sp
    
a=10
b=1.05
c=1
d=1.06
p=1.0
while p>0:
    if -0.3<ln_demand(p)-ln_supply(p)<0.3:
        print ("Equilibrium Price: ₹",p)
        break
    p+=0.05*p
print("Demand at Equilibrium Price: ₹",math.exp(ln_demand(p)))
print("Supply at Equilibrium Price: ₹",math.exp(ln_supply(p)))