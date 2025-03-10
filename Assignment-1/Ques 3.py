def Move_North(Dist):
    global D,yF
    yF+=Dist
    D=D+Dist
def Move_South(Dist):
    global D, yF
    yF-=Dist
    D=D+Dist
def Move_East(Dist):
    global D, xF
    xF+=Dist
    D=D+Dist
def Move_West(Dist):
    global D, xF
    xF-=Dist
    D=D+Dist
def StraightLine_Distance(xF,yF):
    D=((xF-xI)**2+(yF-yI)**2)**0.5
    return D
xI=int(input("Enter initial x-coordinates: "))
yI=int(input("Enter initial y-coordinates: "))
D=0
xF=xI
yF=yI
while True:
    Dist=int(input("Enter The Distance To Move:"))
    if Dist<=0:
        break
    else:
        if 0<Dist<=25:
            Move_North(Dist)
        elif 26<=Dist<=50:
            Move_South(Dist)
        elif 51<=Dist<=75:
            Move_East(Dist)
        else:
            Move_West(Dist)
            
print("Coordinates: ",(xF,yF))
print("Distance Travelled: ",D)
print("Straight Line Distance between initial and final coordinates: ",StraightLine_Distance(xF,yF)) 