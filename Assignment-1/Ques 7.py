cost_of_laptop=int(input())
savings=0
number_of_months=0
while(savings<=cost_of_laptop):
    number_of_months=number_of_months+1 
    savings=savings+(savings*(0.005)+2000)
print("After",number_of_months-1,"months")
print(int(savings-cost_of_laptop))
