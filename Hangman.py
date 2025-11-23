import random
words = ["table", "house", "mirror", "brush"]
keyword = random.choice (words)
len(keyword)
underscores = ["_"]*len (keyword)


hangman_stages = [
'''
    |
    |
    |
    |
    |
''',
'''
---------
|
|
|
|
|
''',
'''
    ---------
      |.   |
      |    
      |   
      |   
      |
      ''',
      '''
    ---------
      |.   |
      |    O
      |   
      |   
      |
      ''',
      '''
    ---------
      |.   |
      |    O
      |    |
      |   
      |
      ''',
'''
    ---------
      |.   |
      |    O
      |   \\|
      |   
      |
      ''',
      '''
    ---------
      |.   |
      |    O
      |   \\|/
      |   
      |
      ''',
      '''
    ---------
      |.   |
      |    O
      |   \\|/
      |   / 
      |
      ''',
      '''
    ---------
      |.   |
      |    O
      |   \\|/
      |   / \\
      |
      '''

]

counter = -1

while True:
    print (" ".join(underscores))

    letter = input("Guess a letter: ")

    if letter in keyword:
        for i in range(len(keyword)):
            if letter == keyword [i]:
                underscores[i] = letter
    else:
        counter = counter + 1
        if counter == 9:
            print("You have no more guesses")
            break
        print (hangman_stages [counter])
    if "_" not in underscores:
        print("You have guessed the word")
        break