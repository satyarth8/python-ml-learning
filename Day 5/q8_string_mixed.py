#8. Wap to create a string from 2 given string in such a way that the first alphabet 
# of 1st string is followed by the last alphabet of string 2 and so on
#    ex  string 1 - "hello"
#       string 2 - "world"
#        new str ="hdellrloow"
s1=str(input("Enter the first string : "))
s2=str(input("Enter the second string : "))
newstr=""
max_len=len(s1) if len(s1)>len(s2) else len(s2)
print(max_len)
a=0
b=len(s2)-1
for i in range(0,max_len):
        newstr+=s1[a]
        a+=1
        newstr+=s2[b]
        b-=1
print(newstr)
