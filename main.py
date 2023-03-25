#13/03/2023
#Eliza smith (21206@rangiorahigh.school.nz)
#Phython basics quiz for year 9's
score = 0

import time 
t=1 


def getAnswer(question): 
  """defines function to ensure all answers are intergers between 1 and 4"""
  validInput = False # A boolean which will loop until our condistion is met
  while not validInput:
    try: # this lets us test code for errors without breaking
      answer = int(input(question)) 
      if answer > 0 and answer < 5:
        validInput = True
    except ValueError:
      print("Enter a number between 1 and 4 in answer(eg. 3) try again ")
  return answer


def finalTryAgain(userName):
  playAgain=""
  while playAgain != "yes" and playAgain != "no":
      playAgain=input("Would you like to play again? (Yes or No) ".lower())
      if playAgain == ("no"):
        print("Game Over, goodbye",userName)
        return False
      if playAgain== ("yes"):
        print("Okay",userName,"...")   
        return True


correctAns = ([1, 2, 4, 1, 3, 3])
questions = ([
'''
Q1. Was python named after a snake? 
1. No 
2. Yes 
3. Indirectly 
4. It was named after a board game 
''',
  
'''
Q2. Which language is older python or java?  
1. Java is older
2. Python is older
3. They are the exact same age
4. This information is unknown
''', 
  
'''
Q3. What is the opposite of input? 
1. Intake 
2. Outtake 
3. Putout 
4. Output
''', 

'''
Q4. What is a loop? 
1. A process which repeats
2. A function that can draw a circle
3. A process which does not repeats
4. It is not used in python
''',
  
'''
Q5. Is Python one of the most popular languages used?
1. No it is a low level language
2. No it is very difficult to learn
3. Yes, it's easy to learn
4. It is not known
''', 
  
'''
Q6. Is Python indentation specific?
1. No, although this is present in all other languages
2. Yes, it is the only language which has this
3. Yes, it is also present in many other languages
4. Nope this is not a thing
'''
])

print(
  '''Hello, this is a quiz for year 9's with an interest in computer science. 
The quiz will assess your level of knowledge regarding Python 3.\n''')
time.sleep (t)

userName = str(input("First of all, what is your name? \n"))

print("Thank you", userName + ",")
time.sleep (t)
yearLvl = input(
  "One last question before we begin the test are you a year 9? (yes or no) ").lower()

play=True 
while play==True:
  score = 0
  
  while yearLvl != "yes" and yearLvl != "no":
    yearLvl = input("Please answer with either Yes or No, are you a year 9? ").lower()
    if yearLvl == ("yes"):
      print("good")
    
    if yearLvl == ("no"):
      print("You are not the correct demograthic for this quiz")
      exit()
  
  listQuestion = 0
  while listQuestion < len(questions):
    answer = getAnswer(questions[listQuestion])
    if answer == correctAns[listQuestion]:
      print("correct")
      score += 1
      print("score: [",score,"]")
  
    else:
      print("incorrect")
      print("score: [",score,"]")
    listQuestion += 1

  percent= int(score/listQuestion *100)
  if score >3:
      print("Well done you have completed the test, your score is",score,"out of",listQuestion,"questions. Resulting in",percent,"% of the test being answered correctly.")
     
    
      playAgain=input("Would you like to play again? (Yes or No) ".lower())
      if playAgain == ("no"):
        print("Game Over, goodbye",userName)
        play=False
      if playAgain == ("yes"):
        print("Very well",userName)

      play=finalTryAgain(userName)
              

        
  if score <4:
      print("You have completed the test it is advised to attempt this again due to you low score, your score is",score,"out of",listQuestion,"questions. Resulting in",percent,"% of the test being answered correctly.")
      
      playAgain=input("Would you like to play again? (Yes or No) ".lower())
      if playAgain == ("no"):
        print("Game Over, goodbye",userName)
        play=False
      if playAgain == ("yes"):
        print("A good choice considering you score",userName,"...")
      
      play=finalTryAgain(userName)
      
 
                
              