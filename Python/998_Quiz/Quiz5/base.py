# PART ONE
favnum = input("What is your favorite number? (Ex. My favorite number is 42): ")
# PART TWO
Age = input("How old are you?: ")
# PART THREE
for i in range(0,len(favnum)):
    if(favnum[i:i+1] == "7"):
        print("7")
# PART FOUR
for i in range(0,len(Age)):
    if(Age[i:i+2] == (Age)):
        print(Age)
# PART FIVE
total = 7 * int(Age)
print(str(total))
        
