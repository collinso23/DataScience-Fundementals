total = 0
n=[]
while (n != 0):
    n = (input("Enter an int to sum, 0 to quit:"))
    if not (n.isdigit()):
        print("Please enter an int.")
        continue
    n = int(n)
    total += n
print("Total is", total)
