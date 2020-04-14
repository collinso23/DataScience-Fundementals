wo = input("Enter a word: ")
le = input("Enter a letter to search: ")
wo=wo.upper()
le = le.upper()
total = 0
for c in wo:
    if (c == le):
        total+=1
print("There are %d occurances of %s in %s" %(total, le, wo) )