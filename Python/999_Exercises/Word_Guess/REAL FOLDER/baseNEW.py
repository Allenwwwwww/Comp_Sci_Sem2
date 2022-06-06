import random
list_words = []
with open('allow_words.txt') as f:
    for line in f:
        l = line.strip()
        list_words.append(l)
a = 0
b = 0
        
num = random.randrange(12972)
answer = list_words[num]

for i in range(0,6):
    guess = input("Please guess a random word: ")
    if (guess == answer):
        print("Wow, you guessed the correct answer!")
        b = 1
        break
    else:
        for words in list_words:
            if(guess == words):
                a = 1 
        if(a == 1):
            print("That's not it. Try again:)")                
        else:
            print("Invalid entry, guess again!")
if(b==0):
    print("You've ran out of tries the word was "+(l)+".")

f.close()
