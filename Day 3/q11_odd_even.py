def odev(n1,n2):
    if(n1%2==0 and n2%2==0):
        if(n1<n2):
            return n1
        else:
            return n2
    elif(n1%2!=0 or n2%2!=0):
        if(n1>n2):
            return n1
        else:
            return n2  
print(odev(1,2))