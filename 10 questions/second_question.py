highest=0
second_highest=0

for i in range(5): 
    salaray=int(input("enter salary of employee : "))
    
    if salaray>highest:
        second_highest=highest
        highest=salaray
    elif salaray>second_highest and salaray!=highest:
        second_highest=salaray
        
print(highest,"highest salary")
print(second_highest,"second highest salary")
