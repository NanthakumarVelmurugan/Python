'''
rows=5
for i in range(1,rows+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
'''
num=int(input("enter your number : "))
if num%2: 
    print(num,"is odd number")
    a=num-1
    b=num+1
    num=num
    total=a+b+num
    print("Total :",total)
else:
    print(num,"is even number")
    a1=num-1
    a2=num+1
    num=num
    total1=a1+num+a2
    print("Total :",total1)


