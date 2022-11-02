
from unicodedata import digit


k,j,d,l=0,0,0,0
email=input("Please Enter Your Email Account:")
if len(email)>=6:
    if email[0].isalpha():
        if ("@"in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue

                    elif i=="_"  or i=="." or i=="@":
                         d=1
                    elif len(email)>=25:
                        l=1   
                        continue 
                    

                

                
                if k==1 or j==1 or d==1 or l==1:
                    print("Error Occured(5): Wrong Email")
               
               
            else:
                print(" Error Occured(4): Wrong Email")
        else:
            print(" Error Occured(3): Wrong Email")
    else:
        print(" Error Occured(2) : First letter should be alphabet")
else:
    print(" Error Occured: Not valid Email")