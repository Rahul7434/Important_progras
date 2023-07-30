import re
s="Raahu2a&@kakhd*ksf()_kdjkjh@s:^$#lkcl!"
s1="Rahul"
l=re.compile('[@_!&*%$#^)()"]')

if l.search(s)==None:
    print("There are No Special Character Present in String")
else:
    print("String COntain Special Character")