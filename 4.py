'''
size=int(input("enter your size : "))
cut=(size//2)+1
star="*"
for row in range(1,size+1):
    for col in range(1,size+1):
        if row==1 or row==size:
            print(star,end=" ")
        elif col==cut:
            print(star,end=" ")
        else:
            print(" ",end=" ")
    print()
'''
size=int(input("enter your value : "))
cut=(size//2)+1
for row in range(1,size+1):
    for col in range(1,size+1):
        if col==1 or col==size:
            print("*")