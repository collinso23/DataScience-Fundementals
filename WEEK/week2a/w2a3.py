
name = input("Please enter your name:")
name = name.upper()

if (len(name) > 8):
    name = name[:8]
while (len(name) < 4):
    name = name+'0'
print("HELLO, %s!" %(name))