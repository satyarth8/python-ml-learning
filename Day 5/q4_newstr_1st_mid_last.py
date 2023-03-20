#4. wap to create a string made up fo the 1st , middle and last charcter of a given string
s=str(input("Enter the string : "))
newstr=s[0]+s[int(len(s)/2)]+s[len(s)-1]
print("The string having first mid and last characters : ",newstr)