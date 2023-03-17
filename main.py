#13/03/2023
#Eliza smith (21206@rangiorahigh.school.nz)
#Phython basics quiz for year 9's
score=0
correctAns= iter(["no","python","output","1","true"])
questions= iter(["Was python named after a snake?","Which language is older python or java ","What is the opposite of input","1. a loop is a proccess which will repate 2. a loop dose not repete", "Python is one of the most popular languages True of false"])

print('''Hello, this is a quiz for year 9's with an interest in computer science. 
The quiz will assess your level of knowledge regarding Python 3.\n''')

userName=input("First of all, what is your name? \n")
print("Thank you",userName+",")

yearLvl=input("one last question before we begin the test are you a year 9? (yes or no) ")
yearLvlLower= yearLvl.lower()
if yearLvlLower==("yes"):
  print("good")
else:
  print("You are not the correct demograthic for this quiz")
  exit()


    
#for amount in questions:
  #x = next(questions)
  #answer=input(x)
  #if answer== correctAns[1]:
  #  print("correct")
   # score+1
  #else:
  #  print("incorrect")
  

