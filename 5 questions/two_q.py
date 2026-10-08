#find the 2nd largest number in list
high=0
shigh=0
numbers=[1,20,3,42,10]

for i in numbers:
    if i>high:
        shigh=high
        high=i
    if i>shigh and i!=high:
        shigh=i
        
print(shigh)
print("the second highest number is ",shigh)