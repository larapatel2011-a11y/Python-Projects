import random

score = 0
def wordscramble(word):
    scrambleword = list(word)
    random.shuffle(scrambleword)
    return ("".join(scrambleword))
wordlist = ["python","chair","table","bottle","mirror"]

while True:
    word = random.choice(wordlist)
    scrambleword = wordscramble(word)
    print (scrambleword)


    for i in range(3):
        userguess = input("Guess what the word is: ")
        if userguess == word:
            print("Correct")
            score = score+1
            break
        else:
            hint = input("do you want a hint?: ")
            if hint == "yes":
                print("The word starts with", word[0])
            print ("Guess again")
    else:
        score = score-1
    playagain = input("Do you want to play again?: ")
    if playagain == "yes":
        print("Ok")
    elif playagain == "no":
        break

print("score:", score)