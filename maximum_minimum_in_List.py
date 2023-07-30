
l=[1,2,100,5,67]

# Without Using Function
sm=l[0]
lr=l[0]
for i in l:
    if i < sm:
        sm=i
    elif i > lr:
        lr=i
print(f"sm={sm} lr={lr}")


# Using Sort() Function 
l.sort()
print("Smallest=",l[0])
print("Largest=",l[-1])

# Using min() & Max() 
print(min(l))
print(max(l))