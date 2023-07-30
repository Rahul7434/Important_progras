a= int(input("Enter Number and Find Factorial Of that Number"))


for j in range(2,a+1):
    f=1
    for i in range(1,j+1):
        f=f*i
    print(f"Factorial Number {j}={f}")
