#13/03/2023
#Eliza smith (21206@rangiorahigh.school.nz)
#Phython basics quiz for year 9's
score = 0
import time 
TIME_CONT = 0.1 
question_number = 0
play_quiz=True 

def get_answer(question_reprint): 
  """defines function to ensure all answers are intergers between 1 and 4"""
  valid_input = False # A boolean which will loop until our condistion is met
  while not valid_input:
    try: # this lets us test code for errors without breaking
      user_answer = int(input(question_reprint)) 
      if user_answer > 0 and user_answer < 5:
        valid_input = True
    except ValueError:
      print("Enter a number between 1 and 4 in answer(eg. 3) try again \n")
  return user_answer

def play_again_func(user_name,score):
  user_play_again=""
  while user_play_again != "yes" and user_play_again != "no":
      user_play_again=input("Would you like to play again? (Yes or No) \n".lower())
      if user_play_again == ("no"):
        print("Game Over, goodbye",user_name)
        return False
      if user_play_again== ("yes"):
        if score >3:
          print("Very well",user_name,"...")   
        if score <4:
          print("A good choice considering your score",user_name,"... \n")    
        return True

answer_list = ([1, 2, 4, 1, 3, 3])
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

print(
  '''Hello, this is a quiz for year 9's with an interest in computer science. 
The quiz will assess your level of knowledge regarding Python \n''')
time.sleep (TIME_CONT)

user_name = str(input("First of all, what is your name? \n"))

print("Thank you", user_name + ", \n")
time.sleep (TIME_CONT)
year_level = input(
  "One last question before we begin the test are you a year 9? (yes or no) \n").lower()

while play_quiz==True:  
  
  while year_level != "yes" and year_level != "no":
    year_level = input("Please answer with either Yes or No, are you a year 9? \n").lower()
    if year_level == ("yes"):
      print("good")
    
    if year_level == ("no"):
      print("You are not the correct demograthic for this quiz \n")
      exit()
  

  while question_number < len(question_list):
    user_answer = get_answer(question_list[question_number])
    if user_answer == answer_list[question_number]:
      print("correct")
      score += 1
      print("score: [",score,"]\n")
  
    else:
      print("incorrect")
      print("score: [",score,"]")
    question_number += 1

  percent_correct= int(score/question_number *100)
  if score >3:
      print("Well done you have completed the test, your score is",score,"out of",question_number,"questions. Resulting in",percent_correct,"% of the test being answered correctly. \n")
    
      play_quiz=play_again_func(user_name,score)      
        
  if score <4:
      print("You have completed the test it is advised to attempt this again due to you low score, your score is",score,"out of",question_number,"questions. Resulting in",percent_correct,"% of the test being answered correctly. \n")
      
      play_quiz=play_again_func(user_name,score)    