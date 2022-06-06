print("We're drawing a box")
char = input("What symbol would you like to use: ")
height = int(input("Please enter the height: "))
width = int(input("Please enter the with: "))
i = 0
for x in range(0,width):
    for y in range(0,height):
        print(char,end = "")
    print("")