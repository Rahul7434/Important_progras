# Swap First And Last Element inList
l=[12,44,55,2,89,1,8,34]
size=len(l)
temp=l[0]
l[0]=l[size-1]
l[size-1]=temp
print(l)

# Swap Any Teo Element In List
l=[1,3,5,6,7,8,9]
l[0],l[3]=l[3],l[0]
print(l)


