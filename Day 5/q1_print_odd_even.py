#1. WAP to print character persetn at odd and 
#   even index of a given string to two different string
str="hello world"
evenstr=""
oddstr=""
for i in range(0,len(str)):
    if i%2==0:
        evenstr+=str[i]
    else:
        oddstr+=str[i]
print("at odd index :",oddstr)
print("at even index :",evenstr)
