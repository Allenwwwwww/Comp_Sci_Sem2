# sentence = "whale hello there. Don't we all love whales? I absolutely love whales! whales are so huge!!!"
# for i in range(0,len(sentence)):
#     x = sentence[i:i+5]
#     if x == 'whale':
#         print("Here a Whale")




count = 0
with open('moby.txt') as f:
    for line in f:
        sentence = line.strip()
        for i in range(0,len(sentence)):
            x = sentence[i:i+5].lower()
            if x == 'whale':
                count = count + 1
                print("Here a Whale")
print("The word whale is said " + str(count) + " times.")
f.close()
