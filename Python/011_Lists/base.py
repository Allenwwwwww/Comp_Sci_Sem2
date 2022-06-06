import random
list = ["I went to buy some cargo pants, I coudln't find any.","My name Jeff.","Your mom","Bofa deez nuts","Uno reverse card",]
x = int(random.randrange(5))
if x == 0:
    print(list[0])
elif x == 1:
    print(list[1])
elif x == 2:
    print(list[2])
elif x == 3:
    print(list[3])
else:
    print(list[4])