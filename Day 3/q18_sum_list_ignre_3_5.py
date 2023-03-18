def sum_except_3_5(nums):
    total = 0
    for i in nums:
        s=""
        s=str(i)
        if(s[0]=='3'):
            continue
        if(i%10==5):
            continue
        total+=i
    return total
       
a=[3,5,6,6,65,39]
print(sum_except_3_5(a))