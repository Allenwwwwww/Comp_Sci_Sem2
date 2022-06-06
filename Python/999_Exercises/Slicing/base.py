x = input("Please enter your first and last name: ")
j=1
for l in range(0,len(x)):
    y=x[l:j]
    j=j+1
    print(y)

name = input("What is your Name?: ")
space = 1
for z in range(0, len(name)):
    if(name[z:z+1] == " "):
        space = z
    print(name[z:z+1])
print(" ")
for m in range(0,space):
    print(name[m:m+1])
    