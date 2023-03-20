#7. Wap to count all alphabet , numeric value & special symbol from a given string
s=str(input("Enter the string "))
alpha_ctr=0
number_ctr=0
special_ctr=0
for i in s:
    if(i.isalpha()==True):
        alpha_ctr+=1
    elif(i.isdigit()==True):
        number_ctr+=1
    else:
        special_ctr+=1
print("Alphabet ",alpha_ctr)
print("Number : ",number_ctr)
print("Special symbol : ",special_ctr)