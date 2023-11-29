li=[]
for i in range(1,6):
    m=int(input("Enter your sub "+str(i)+" mark : "))
    li.append(m)
total=sum(li)
avg=total/5
for i in range(5):
    ma=li[i]
    if ma>90 and ma<=100:
        print("sub",(i+1),"A grade")
    elif ma>80 and ma<=90:
        print("sub",(i+1),"B grade")
    elif ma>70 and ma<=80:
        print("sub",(i+1),"C grade")
    elif ma>50 and ma<=70:
        print("sub",(i+1),"D grade")
    else:
        print("sub",(i+1),"Fail")
print("Total is :",total)
print("Average percentage is :",avg,"%")