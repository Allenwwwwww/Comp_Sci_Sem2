import random
retaurant_list=["CPK", "Shark Grill","Starbucks"]
choice = input("Please choose one of the following (CPK, Shark Grill, Starbucks): ")

# CPK
if (choice == 'CPK'):
    print("Thank you for choosing CPK. Here is your menu")
    menu_list=["Pepperoni Pizza ","Pasta ","Soup ","Salad ","Bread"]
    print(menu_list)
    x = random.randrange(5)
    item = menu_list[x]
    print("")
    print("We also reccoment our " + item + ".")

# Shark Grill 
elif (choice == 'Shark Grill'):
    print("Thank you for choosing Shark Grill. Here is your menu")
    menu_list1=["Shark Fillet ","Salmon Fillet ","Mahi Mahi ","Flounder ","Shrimp"]
    print(menu_list1)
    y = random.randrange(5)
    item2 = menu_list1[y]
    print("")
    print("We also suggest our " + item2 + ".")
    
# Starbucks
elif (choice == 'Starbucks'):
    print("Thank you for choosing Starbucks. Here is your menu")
    menu_list2=["Lemon Loaf ","Cold Coffee ","Hot Coffee","Cake Pop ","Chocolate Croissant "]
    print(menu_list2)
    z = random.randrange(5)
    item3 = menu_list2[z]
    print("")
    print("We also suggest our " + item3 + ".")
else:
    print("You have mispelled something please try again.")