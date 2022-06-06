int1 = int(input("How many items are you buying? :"))
sum = 0
for a in range(0,int1):
    item = input("What is the item that you're purchasing? :")
    cost = float(input("How much is the item? :"))
    print("Thanks for buying " + item)
    print("________________________________________________")
    sum = sum + cost
print("For " + str(int1) + " item(s) your total is " + str(sum))
print("Thank you come again!")