#27/6/22 Lincoln James Edward Kirkby learning globals and questions list
import random #importing the random library
score = 0
question = 0
english = ['cat','dog','sheep','pig','cow','horse','chicken','rabbit','pen','pencil','book','scissors','paper','eraser','ruler','book','computer','oven','door','window','cupboard','chair','table','fan','family','parents','father','mother','child','son','daughter','brother of a female','younger brother of a male','older brother of a male','eldest brother/sister','older sister of a female','younger sister of a female','sister of a male','grandparents','grandfather','grandmother','red','green','blue','yellow','white','pink','purple','black','orange']#yes there are 50 questions
right_answer =['ngeru','kuri','hipi','poaka','kau','hooiho','heihei','raapeti','pene','peneraakau','pukapuka','kutikuti','pepa','uukui','ruuri','pukapuka','rorohiko','oomu','tatau','wini','kaapata','nohoanga','paparahua','koowhiuwhiu','whanau','maatua','paapaa','maamaa','taitamaiti','tama','tamaahine','tungaane','teina','tuaakana','kauaemua','tuaakana','teina','kaikuahine','tuupuna','tupuna taane','tupuna wahine','whero','kakariki','kikorangi','kowhai','ma','mawhero','tawa','pangu','karaka']
option_2 = ['kat','kuro','hipo','pork','kaueue','hooi','heikena','petipeti','peni','raakaupenepene','puka','kuikui','peipa','erakui','ruukuia','peparaakau','komputa','umin','puua','winpo','kuupoata','rokapa','taapapui','whanuu','whamuu','pawhateneii','whaawha','maawha','rowhatama','tema','tamerewha','turakuane','teeii','raahapuu','mekomi','hatii','ngewuwii','kite','wheheeu','tupuna tutee','tupuna taarewii','ketiwhe','pooku','turowa','teengi','paawhuhi','ponetu','kuhu','ninuukaa','kupungi']
option_1 = ['kakariki','kikorangi','kowhai','ma','mawhero','tawa','mangumangu','karaka','ngeru','kuri','hipi','poaka','tama','tamaahine','tungaane','teina','tuaakana','kauaemua','tuaakana','teina','kaikuahine','tuupuna','tupuna taane','tupuna wahine','whero','kutikuti','pepa','uukui','kau','hooiho','heihei','raapeti','pene','penipeniraakau','pukapuka','whaea','tamaiti','raakauine','pukakuia','rorohiko','oomu','tatau','wini','kaapata','nohoanga','paparahua','koowhiuwhiu','whanau','maatua','paapara']
def generate_question(english,right_answer,option_1,option_2): #define a function to generate a question
  global score
  global question
  question += 1
  print("*------------------------------------------------------------------------*\n"+"      question:",question,"\n*------------------------------------------------------------------------*\n"+"which one is a possible translation for",english,"in maaori")
  #Multi choice Quiz
  random_sequence = random.randint(0,2)#generate a random number to demine the sequence of answers
  if (random_sequence == 0):
    print("A",option_1,"\nB",option_2,"\nC",right_answer)
    answer = input("answer with a, b or c:").lower()
    if answer == "c":
      score +=1
      print("great job!")
    else: print("sorry but the answer was C:",right_answer)
  elif (random_sequence == 1):
    print("A",option_2,"\nB",right_answer,"\nC",option_1)
    answer = input("answer with a, b or c:").lower()
    if answer == "b":
      score +=1
      print("great job!")
    else: print("sorry but the answer was B:",right_answer)
  else:
    print("A",right_answer,"\nB",option_1,"\nC",option_2)
    answer = input("answer with a, b or c:").lower()
    if answer == "a":
      score +=1
      print("great job!")
    else: print("sorry but the answer was A:",right_answer)
#NUMBER
print("Welcome to the te reo quiz!\nthe questions maximum is 50 and the default is 10; answer questions by typing a b or c.")
num_of_questions=input("how many questions do you want?:") #How many questions do you want:
if not num_of_questions.isdigit(): num_of_questions = 10 #if input isn't a valid number sets the number to 10 by default
num_of_questions = int(num_of_questions)
if num_of_questions >= 50: num_of_questions = 50 #if input is larger than 50 set to 50 as the lists only have 50 questions
print("*------------------------------------------------------------------------*\n"+"                       starting quiz",num_of_questions,"questions\n")
for i in range (0,num_of_questions):# generate 3 questions pulling possible answers form lists
  i = random.randint(0,49-i)
  generate_question(english[i],right_answer[i],option_1[i],option_2[i])
  english.pop(i)
  right_answer.pop(i)
  option_2.pop(i)
  option_1.pop(i)
#SCORE
print("***************************************************************************\n"+"                                RESULTS")
if score == num_of_questions: #print the score at the end of the quiz
  print("\n-wow you are truly amazing, you got 100% or",num_of_questions,"/",num_of_questions,)
elif score >= num_of_questions*0.75:#checking for 75%
  print("\n-great job you did very well, you even got",score,"/",num_of_questions,"or",int((score/(num_of_questions))*100),"%")
elif score >=num_of_questions/2:#checking for 50%
  print("you did quite well, over 50% in fact")
else: print("\n-you did poorly, mabie you will get better results next time")
print("***************************************************************************")