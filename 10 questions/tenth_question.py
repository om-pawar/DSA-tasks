t_a_s=0
h_m_s=0
l_m_s=0
no_m_s_a=0

for i in range(1,13):
    month=int(input("enter the sale in the month no "+ str(i)+ ":"))
    if month>0:
        t_a_s=t_a_s+month
        
        avg_monthly_s=t_a_s/12
        
        if month>100000:
            no_m_s_a=no_m_s_a+1
            p_h_m_s=no_m_s_a/12*100
            
    if i == 1:
                h_m_s = month
                l_m_s = month
    else:
    
         if month > h_m_s:
            h_m_s = month
         if month < l_m_s:
            l_m_s = month


print(t_a_s,"is total annual sale")
print(avg_monthly_s,"is average monthly sale")
print(h_m_s,"is high sale")
print(l_m_s,"is low sale")
print(no_m_s_a,"is sale of month above 100000")
print(p_h_m_s,"percentage of high month sales")