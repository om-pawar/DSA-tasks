total_sps=0
t_amount_sps=0

for i in range(8):
    trans=int(input("enter your amount of transaction : "))
    if trans>100000:
        t_amount_sps=t_amount_sps+trans
        total_sps=total_sps+1
        
print("the total number of suspicious transactions are :"total_sps)
print("the total amount of suspicious transactions are "t_amount_sps)