a=[1,2,1,3,4,2,1,2,1,3,4,5,3,6,7,6,8,6,]
reoccur=[]
for i in a:  
    if(a.count(i))>=2 and  (a.count(i))%2!=0:
        if( i not in reoccur):
            reoccur.append(i)
print(reoccur)