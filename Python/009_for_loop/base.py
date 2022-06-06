print("We're drawing a line!")
length = int(input("Please enter the length: "))
vh = input("Would you like a vertical or horizontal line? (V, H): ")
if vh == "V":
    for length in range(0,length):
        print("*")
elif vh == "H":
    for length in range(0,length):
        print("*",end="")
else:
    print("Try Again.")
