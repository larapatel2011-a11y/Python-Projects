import random
words = ["table", "house", "mirror", "brush"]
score = 0
def game():
  global score
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
          score = score + 1
          break

while True:
  again = input("Do you want to play again?")
  if again == "yes":
    game()
  else:
    print ("Game over. The score is" , score)
    break