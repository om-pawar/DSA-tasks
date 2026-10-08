for i in range(1,51):
    factors=0
    for j in range(1,i+1):
        if i%j==0:
            factors=factors+1
    if factors==2:
        print(i)
             
   
       