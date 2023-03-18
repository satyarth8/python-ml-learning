a="a b c"
dict={'chars':0}
le=0
for i in a:
    if(i.isalpha()==True ):
        le+=1
dict['chars']=le
print("Number of character in the string is ",dict['chars'])