print("enter your attendace in P for present and A for absent ")
attendance=input("attendance=").lower()

t_d=len(attendance)  
p_d=0
a_d=0
 
for i in attendance:
    
        if i=="p":
            p_d=p_d+1
            
        elif i=="a":
            a_d=a_d+1

print("Total working days are :",t_d)                   
print("Total present days are :",p_d)
print("Total absent days are :",a_d)

atten_percentage=p_d/t_d*100

print("The attendacne percentage is :",atten_percentage,"%")

if atten_percentage>=75:
    print("CONGRATULATION YOU ARE ELIGIBLE FOR BONUS")
else:
    print("OOPSS YOU ARE NOT ELIGIBLE FOR BONUS")