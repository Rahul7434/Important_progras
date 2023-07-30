l=[1,2,3,4,5,3,2]

#Using 1.slicing 2.extend() 3.list() 4.copy() 5.list comprehension
l1=[]
l1=l[:]
print("Using Slising Operator:-",l1)

l2=[]
l2.extend(l)
print("Using Extent() FUnction:-",l2)

l3=[]
l3=list(l)
print("Using List FUnction:-",l3)

l4=[]
l4=l.copy()
print("Using Copy function:-",l4)

l5=[]
l5=[x for x in l]
print("Using Comprehension:-",l5)
