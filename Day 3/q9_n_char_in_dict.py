a="a b c"
dict={'chars':0}
le=0
for i in a:
    if(i.isalpha()==True ):
        le+=1
dict['chars']=le
print(f"Number of character in the string {dict['chars']}")