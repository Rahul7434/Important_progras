a=int(input("Enter Number And Check number is Palindrom or not"))
c=0
for i in range(1,a+1):
    if a%i==0:
        c=c+1

if c==2:
    print(f"{a}Number is Prime NUmber")
else:
    print("Number is Not Prime")



