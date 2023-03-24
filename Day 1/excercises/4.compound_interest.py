p=int(input("Enter the principle : "))
r=float(input("Enter the rate : "))
t=int(input("Enter the time in yearsd: "))
n=int(input("Enter the no. of times the interest is compounded per year"))

# we calculate the compund interest
a=p*((1+(r/n))**(n*t))

#we display the result
print("The amount : ",a)
