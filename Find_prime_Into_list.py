l=[20,30,60,10,70,33,11,47,33]

for i in l:
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c=c+1
    if c==2:
        print(f"Prime Number{i}")

