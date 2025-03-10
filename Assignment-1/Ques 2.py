x=int(input("Enter Initial Units : "))
chairs=0
tables=0
maximum_profit=0
while (8*tables+2*chairs)<=400 and (2*tables+chairs)<=120:
    chair_profit=0
    table_profit=0
    if chairs<=x:
        chair_profit=25*chairs
    else:
        chair_profit=(25*x) + 30*(chairs-x)
        
    if tables<=x:
        table_profit=90*tables
    else:
        table_profit= (90*x) + 100*(tables-x)

    if (chair_profit+table_profit>maximum_profit):
        maximum_profit=chair_profit+table_profit
    chairs=chairs+1
    tables=tables+1
    
print("Maximum number of tables is :",tables-1)
print("Maximum number of chairs is :",chairs-1)
print("Maximum profit is : ₹",maximum_profit)