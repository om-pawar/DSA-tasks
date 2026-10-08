h_s=0
l_s=100

for i in range(1,7):
    p_score=int(input("enter the peformance score of employee "+str(i) +":"))
    if p_score>=90:
        print("exellent")
    elif p_score>=70 :
        print("good")
    elif p_score>=50 :
        print("average")
    else:
        print("poor")
    if p_score>=h_s:
        h_s=p_score
    if p_score<=l_s:
        l_s=p_score
             
print(h_s,"is the higher score")
print(l_s,"is the lower score")