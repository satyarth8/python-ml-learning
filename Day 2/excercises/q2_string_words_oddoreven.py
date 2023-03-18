#we take as string 
#print the words which have odd no of letters and even no. of letters separately
odd_words=[]
even_words=[]
a="my name is satyarth prakash and i am feeling happy"
str=a.split()# split each word in to list
for i in str:
    if (len(i))%2==0:
        #the word is even
        even_words.append(i)
    else:
        #the word is odd
        odd_words.append(i)
print("the Odd words are :",odd_words)
print("the even words are :",even_words)