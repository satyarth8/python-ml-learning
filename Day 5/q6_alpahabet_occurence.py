#6. Wap to count  occurances of all alphabets within a given string
alpha_freq={}
s=str(input("Enter the string : "))
x=0
for i in s:
    alpha_freq[str(i)]=0
for i in s:
    alpha_freq[str(i)]=alpha_freq[str(i)]+1

print("Occurence of all the alphabet is : ")
for a,b in alpha_freq.items():
    print(a,":",b,"times")