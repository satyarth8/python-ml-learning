def reverse_words(a):
    asplit=a.split()
    newstr=""
    for a in asplit:
        newstr=newstr+a[::-1]+" "
    return newstr

a="my name is satyarth"
print("The string in reverse is : "+reverse_words(a))