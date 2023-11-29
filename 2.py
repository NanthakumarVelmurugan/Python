'''
s1=int(input("Enter your mark1 : "))
s2=int(input("Enter your mark2 : "))
s3=int(input("Enter your mark3 : "))
s4=int(input("Enter your mark4 : "))
s5=int(input("Enter your mark5 : "))

if ((s1>=35) and (s2>=35) and (s3>=35) and (s4>=35) and (s5>=35)) and ((s1<=100) and (s2<=100) and (s3<=100) and (s4<=100) and (s4<=100)):
    total=s1+s2+s3+s4+s5
    avg=total/5
    print("you are pass")
    print("your total is :",total)
    print("your average percentage is :",avg,"%")
else:
    print("you are fail")
'''

password=["1110","0000","1233","9087","8907"]
user=input("User Name : ")
user_pw=input("Password : ")
if  user=="Nantha" and (user_pw in password):
    print("log in successfully")
else:
    print("wrong password")
