def Calculate_Current_pop(pop_temp,growth):
    for i in range(len(pop_temp)):
        pop_temp[i]=round((pop_temp[i]+pop_temp[i]*(growth/100)),2)
        growth=growth-0.4
    return pop_temp
    
def Calculate_Total_pop(pop_temp):
    Total_pop=0
    for val in pop_temp:
        Total_pop+=val
    return round(Total_pop,2)
    
pop = [50, 1450, 1400, 1700, 1500, 600, 1200]
growth=2.5
years=0
populations={}
populations[0]=Calculate_Total_pop(pop)
while True:
    Calculate_Current_pop(pop,growth)
    years+=1
    populations[years]=Calculate_Total_pop(pop)
    if populations[years]<=populations[years-1]:
        del populations[years]
        years-=1
        break

    growth=round((growth-.1),2)


print("The years after which the maximum population will be reached - ",years,"years")
print("The value of the maximum population - ",populations[years],"millions")