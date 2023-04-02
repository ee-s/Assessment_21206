'''
27/03/23
Eliza smith (21206@rangiorahigh.school.nz)
Python basics quiz for year 9's
'''

#Imports
import time 

#Variables
#All variables are loop dependent (are defined and changed within a loop)

#Constants
TIME_CONT = 0.5 

def year_level_func():
  """
  This function ensures input is a string of either yes or no also known as sanitising the input, 
  the function will resend the same output until input requirements are met and score specific output is given or game is ended.
  
  """
  year_level=""
  while year_level != "yes" and year_level != "no":
        year_level = input(
    "One last question before we begin the test are you a year 9? (yes or no) \n").lower()
        if year_level == ("no"):
         print("Game Over, goodbye",user_name)
         exit() 
        if year_level == ("yes"):
          print("Great!")
        
    
def get_vaild_answer(question_reprint): 
  """
  This function ensures input is an integer between 1 and 4 also known as sanitising the input, 
  and will resend the same output until input requirements are met.
  
  """
  valid_input = False # A boolean which will loop until a condition is met
  while not valid_input:
    try: # This lets the program test code for errors without breaking
      new_user_answer = int(input(question_reprint)) 
      if new_user_answer > 0 and new_user_answer < 5:
        valid_input = True
    except ValueError:
      print("Enter a number between 1 and 4 in answer(eg. 3) try again \n")
  return new_user_answer


def play_again_func(user_name,score):
  """
  This function ensures input is a string of either yes or no also known as sanitising the input, 
  the function will resend the same output until input requirements are met and score specific output is given or game is ended.
  
  """
  user_play_again=""
  while user_play_again != "yes" and user_play_again != "no":
      user_play_again=input("Would you like to play again? (Yes or No) \n").lower()
      if user_play_again == ("no"):
        print("Game Over, goodbye",user_name)
        return False
      if user_play_again == ("yes"):
        if score >3:
          print("Very well",user_name,"with your high score i'm sure you'll do well!")   
          return True
        if score <4:
          print("A good choice considering your score",user_name,"... \n")    
          return True

#A list of the correct answers to quiz questions
answer_list = ([1, 2, 4, 1, 3, 3])
#A list of the quiz's questions
question_list = ([
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

#User information including name and age demographic.
print('''Hello, this is a quiz for year 9's with an interest in computer science. 
The quiz will assess your level of knowledge regarding Python \n''')
time.sleep (TIME_CONT)

user_name = str(input("First of all, what is your name? \n"))
print("Thank you", user_name + ", \n")
time.sleep (TIME_CONT)

#Ensures user is within a chosen demographic
year_level_func()

#Main quiz code, this iterates through question_list comparing answers against answer_list items in the same index as the question_list item until users input has been given on all items
play_quiz=True 
while play_quiz==True:
  question_number = 0
  score=0
  while question_number < len(question_list):
    user_answer = get_vaild_answer(question_list[question_number])
    if user_answer == answer_list[question_number]:
      print("correct")
      score += 1
      print("score: [",score,"]\n")
    else:
      print("incorrect")
      print("score: [",score,"]")
    question_number += 1

#Final results output including percentages and score and a play again option through the #play_again_func function
  percent_correct= int(score/question_number *100)
  if score >3:
      print("Well done you have completed the test, your score is",score,"out of",question_number,"questions. Resulting in",percent_correct,"% of the test being answered correctly. \n")
      play_quiz=play_again_func(user_name,score)      
        
  if score <4:
      print("You have completed the test, it is advised to attempt this again due to your low score, your score is",score,"out of",question_number,"questions. Resulting in",percent_correct,"% of the test being answered correctly. \n")
      play_quiz=play_again_func(user_name,score)