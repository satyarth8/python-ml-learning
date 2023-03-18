def same_start(str1,str2,str3):
    a=str1[0]
    if(str2.startswith(a) and str3.startswith(a)):
        return True
    else:
        return False
print(same_start("abc","abcd","acbs"))
print(same_start("can","do","it"))
