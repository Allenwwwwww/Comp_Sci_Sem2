import random
rand_list = []
x = int(input("How many random numbers would you like?: "))
for i in range(0,x):
    y = random.randrange(10)
    print(y)
