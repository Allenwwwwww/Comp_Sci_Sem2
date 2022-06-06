num = [6,9,32,28,15,22,3,18]



# Average
sum = 0
for i in range(0,len(num)):
    sum = sum + num[i]
avg = sum/len(num)
print(avg)

# So my thinking is I would need a for loop to check how many variables the list has. And then store that 
# value into an integer and all all the numbers of the list together(the amount that the list has).
# Then I would need to divide the sum of the numbers by the amount there are, and that's how you get the average.

# Maximum
max = 0
for i in range(0,len(num)):
    if(max < num[i]):
        max = num[i]
print(max)
# So my thinking is I would need a for loop to check how many variables the list has. And then store that 
# value into an integer and somehow check for the maximum number.



# Minimum
min = max
for i in range(0,len(num)):
    if(min > num[i]):
        min = num[i]
print(min)
# So my thinking is I would need a for loop to check how many variables the list has. And then store that 
# value into an integer and somehow check for the minimum number.
