sentence=str(input("enter the sentence : "))
letter=input("enter the letter the word starts with : ")
for i in (sentence.split()):
    if(i.startswith(letter)):
        print(i,end="\t")
    else:
        pass
