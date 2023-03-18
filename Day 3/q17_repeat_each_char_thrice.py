def rept_thrice(str):
    newstr=""
    for i in range(0,len(str)):
        newstr=newstr+str[i]*3
    return newstr
print(rept_thrice("134"))