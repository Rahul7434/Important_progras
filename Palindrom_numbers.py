"""a=int(input("Enter Numbers ANd Check Number is Palindrom or Not :-"))
temp=a
rev=0
rem=0
while temp>0:
    rem=temp%10
    rev=rev*10+rem
    temp=temp//10

if rev==a:
    print("Number is Palindrom Number")
else:
    print("Number is Not Plindrom")
"""

# 10 To 1000  Find palindrom Numbers 
for i in range(11,1001):
    temp=i
    rev=0
    rem=0
    while temp>0:
        rem=temp%10
        rev=rev*10+rem
        temp=temp//10
    if i==rev:
        print(f"{rev} Is Palindrom Numbers")
    


    