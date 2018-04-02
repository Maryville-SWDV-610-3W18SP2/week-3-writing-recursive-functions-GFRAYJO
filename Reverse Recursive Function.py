def reverseList(r):
    if r == []:
        return []
    else:
        return reverseList(r[1:]) + r[:1]
    
print(reverseList([2,10,8,4,6]))