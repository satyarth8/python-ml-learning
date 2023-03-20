# 10. Wap to create a new string from 2 given string in such a way that the new string should contain 
#    even alphabets from string1 and odd from  string 2
s1=str(input("Enter the first string "))
s2=str(input("Enter the second string "))
newstr=""
for i in range(0,len(s1)-1):
    if(i%2==0):
        newstr+=s1[i]
for i in range(0,len(s2)-1):
    if(i%2!=0):
        newstr+=s2[i]
print("The required string : ",newstr)