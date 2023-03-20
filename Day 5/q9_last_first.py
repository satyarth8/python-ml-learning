#9.   Wap to check whether the 1st and last item of a given list is same or not
def isfirst_last(n):
    if n[0]==n[len(n)-1]:
        print("First and Last is same ")
    else:
        print("First and last is NOT same")
a=[1,2,3,4,5]
isfirst_last(a)
b=[1,2,3,3,1]
isfirst_last(b)
