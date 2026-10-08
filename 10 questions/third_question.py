h_r=0
m_r=0
l_r=0

for i in range(10):
    transactions=int(input("enter the amount: "))
    if transactions>0:
        if transactions>9000:
            h_r=h_r+1
        elif transactions<5000:
            m_r=m_r+1
        else:
            l_r=l_r+1
    else:
        print("you enter wrong amount")

print("in high risk are",h_r)
print("in medium risk are",m_r)
print("in low risk are",l_r)