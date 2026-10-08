#reverse a list without using sort function

marks=[10,20,30,40,50]
reverse_makrs=[]
for i in range(len(marks)-1,-1,-1):
    reverse_makrs.append(marks[i])
print(reverse_makrs)