a="helloworld"
print(a[2:8:2])#prints hello
print(a[6:])#hello satyarth
#============================array[start:stop:step]================================================
print(a[-8:-3])
for x in range(len(a)):
    print(x,"   ",end="")  
print("")  
for x in range(len(a)):
    print(a[x],"   ",end="")
print("")
for x in reversed(range(len(a))):
    print(-1*x,"  ",end="")        
#reverse a string
print()