def cumsum(l0):
    l1 = []
    t = 0
    for x in l0:
        t += x
        l1.append(t)
    return l1    
    
print(cumsum([1,3,5,2]))