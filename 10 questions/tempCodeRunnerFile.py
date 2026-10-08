s_t=0
r_t=0
for i in range(10):
    requests=int(input("enter the amount to be withdrwal: "))
    if requests<20000:
        s_t=s_t+1
        if requests%500==0:
            print("amount is multiple of 500")
            print("it is a succesfull transaction")
        else :
            print("amount is not multiple of 500")  
    else:
        r_t=r_t+1
        print("it is a rejected transaction")
        print("withdrwal limit is 20000 ruppes")
        
print("succesful transactions are :",s_t)
print("rejected transactions are :",r_t)
        
            
            
            