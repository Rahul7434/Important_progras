s=input("ENter String And Check is palindrom or not :-")

# Using slicing  
temp=s
l=s[::-1]
if l==s:
    print("palindrom String:-",l)
else:
    print("Not palindrom",l)
 



