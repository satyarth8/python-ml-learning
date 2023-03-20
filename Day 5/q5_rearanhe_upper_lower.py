#5. wap to arrange a given string in such a way that all lowercase character come first followed by uppercase characters
s=str(input("Enter the string  : "))
for i in s:
    if i.isupper()==True:
        print(i,end="")
for i in s:
    if i.islower()==True:
        print(i,end="")