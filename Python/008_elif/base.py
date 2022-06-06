sum = 0
int1 = int(input("Enter your first number: "))
int2 = int(input("Enter your second number: "))
opr = str(input("Enter your operation please (Ex. +, -, *, /): "))
if opr == "+":
    print (str(int1)+ "+" +str(int2)+"="+str(int1+int2))
elif opr == "-":
     print (str(int1)+ "-" +str(int2)+"="+str(int1-int2))
elif opr == "*":
        print (str(int1)+ "*" +str(int2)+"="+str(int1*int2))
elif opr == "/":
       print (str(int1)+ "/" +str(int2)+"="+str(int1/int2))
else:
    print("You have not chose any of the provided operations try again...")



    