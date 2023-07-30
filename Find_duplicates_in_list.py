# Using Function 
def finddublicates(l):
    return list(dict.fromkeys(l))

list1=finddublicates([1,2,3,4,5,1,76,54,3,44,2,88,99])
print(list1)



list2=[1,4,2,3,4,5,6,7,6,8,99]

list3=list(dict.fromkeys(list2))

print(list3)