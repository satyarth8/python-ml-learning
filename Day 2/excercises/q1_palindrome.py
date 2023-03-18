def ispalindrome(a): #defined a function which takes and argument 
    a=str(a) #changed the type of argument to string 
    b=a[::-1] #reversed the string 
    if(b==a): # checked whether the reverse is equal
        print(f"{a} is Palindrome")
    else:
        print(f"{a} is NOT a palindrome ")

a="abcdeedcba"
ispalindrome(a)
b="aaaaaaaaab"
ispalindrome(b)
c=11111111
ispalindrome(c)