org_password=input("enter your password  : " )
attempt=1

    
for i in range (3):
    password=input("enter the orginal password : ")
    if password==org_password:
        print("you enter correct pass")
        break;
    elif password!=org_password:
        print("you enter wrong pass")
        attempt=attempt+1
    
if attempt>3 :
    print("you are blocked")