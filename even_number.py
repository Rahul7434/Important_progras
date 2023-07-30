"""n=int(input("Enter Number And Find even Number "))

if n%2==0:
    print("Number is Even",n)
else:
    print("Number is Odd")
"""

# Find n Number Even 


n=int(input("Enter Number to find n number even odd "))

for i in range(1,n+1):
    if i%2==0:
        print(f"Even={i}",end='\n')
    else:
        print(f"Odd={i}",end='\n')
