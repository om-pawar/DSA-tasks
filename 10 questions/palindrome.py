number=int(input("enter the number: "))

org_number=number

reverse=0

while number>0:
    digit=number%10
    
    reverse=reverse*10+digit
    
    number=number//10
    
if org_number==reverse:
    print("number is palindrome")
else:
    print("number is not palindrome")