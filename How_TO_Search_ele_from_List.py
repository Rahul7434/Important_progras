l=[12,56,4,2,5,8,9,2]
e=5
c=0
for i in l:
    if i==e:
        print(f"Element Fount in List")
        c=1
        break

if c==0:
    print("Element Not Fount")
    