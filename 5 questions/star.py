#to do palindrome of string
name=input("enter your name: ")
reverse=[]
print(name[0])

for i in range(len(name)-1,-1,-1):
    reverse.append(name[i])
    
print(reverse)