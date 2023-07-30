a=int(input("Enter Number To Find 1 To 100 Prime Numbers:-"))

for i in range(1,a+1):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c=c+1
    if c==2:
        print(f"Prime:={j}")
    



