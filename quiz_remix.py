#global variables 11/5/22
import random
right_answer = []
option_1 = []
option_2 = []
question = 0
correct = 0
score = 0
quizlength = 0
list_start = 0
list_end = 50
english = ['cat','dog','sheep','pig','cow','horse','chicken','rabbit','pen','pencil','book','scissors','paper','eraser','ruler','book','computer','oven','door','window','cupboard','chair','table','fan','family','parents','father','mother','child','son','daughter','brother of a female','younger brother of a male','older brother of a male','eldest brother/sister','older sister of a female','younger sister of a female','sister of a male','grandparents','grandfather','grandmother','red','green','blue','yellow','white','pink','purple','black','orange']
right_answer = ['ngeru','kuri','hipi','poaka','kau','hooiho','heihei','raapeti','pene','peneraakau','pukapuka','kutikuti','pepa','uukui','raakauine','pukapuka','rorohiko','oumu','tatau','wini','kaapata','tuuru','papa-kai','kooheuheu','whaamere','maatua','matua','maamaa','tamaiti','tama','tamaahine','tungaane','tiana','tuaakana','kauaemua','tuaakana','teina','kaikuahine','tuupuna','tupuna taane','tipuna wahine','whero','kakariki','kikorangi','kowhai','ma','mawhero','waiporoporo','mangu','karaka']
option_2 = ['ngeru','kuri','hipi','poaka','kau','hooiho','heihei','raapeti','pene','peneraakau','pukapuka','kutikuti','pepa','uukui','raakauine','pukapuka','rorohiko','oomu','tatau','wini','kaapata','nohoanga','paparahua','koowhiuwhiu','whanau','maatua','paapara','whaea','tamaiti','tama','tamaahine','tungaane','teina','tuaakana','kauaemua','tuaakana','teina','kaikuahine','tuupuna','tupuna taane','tupuna wahine','whero','kakariki','kikorangi','kowhai','ma','mawhero','tawa','mangumangu','karaka']
option_1 = ['ngeru','kuri','hipi','poaka','kau','hooiho','heihei','raapeti','pene','peneraakau','pukapuka','kutikuti','pepa','uukui','raakauine','pukapuka','rorohiko','oomu','tatau','wini','kaapata','nohoanga','paparahua','koowhiuwhiu','whanau','maatua','paapara','whaea','tamaiti','tama','tamaahine','tungaane','teina','tuaakana','kauaemua','tuaakana','teina','kaikuahine','tuupuna','tupuna taane','tupuna wahine','whero','kakariki','kikorangi','kowhai','ma','mawhero','tawa','mangumangu','karaka']
#this text is to inform the user of what the quiz is about 11/5/22
print("Kia ora welcome to the Te Reo quiz, this quiz is designed to test your Te Reo Skills")
print("choose the category you want to practice")
#the current number of quizes is not set there might not acctually be 5 options by the end 11/5/22
print("A animals,B objects,C family members,D colours or E all of the above")
#define a function to generate a question

english = "placeholder"
def generate_question(english,right_answer,option_1,option_2):
  global score
  global quizlength
  if right_answer == "placeholder":
    print("you have answerd all of the questions your final score was",str(score)+"/"+str(quizlength),"or",(score/(quizlength))*100,"%")
    score = 0
    quizlength = 0
    print("A animals,B objects,C family members,D colours or E all of the above")
    quiz_choicer()
  print("what is a correct translation for",english,"in maori")
  #generate a random number to demine the sequence of questions
  random_sequence = random.randint(0,2)
  #seperate print statements for readability
  if (random_sequence == 0):
    print("A", option_1)
    print("B", option_2)
    print("C", right_answer)
    answer = input().lower()
    if answer == "c":
      score +=1
      print("great job")
    else:
      print("sorry but the answer was:",right_answer)
  elif (random_sequence == 1):
    print("A", option_2)
    print("B", right_answer)
    print("C", option_1)
    answer = input().lower()
    if answer == "b":
      score +=1
      print("well done")
    else:
      print("sorry but the answer was:",right_answer)
  elif (random_sequence == 2):
    print("A", right_answer)
    print("B", option_2)
    print("C", option_1)
    answer = input().lower()
    if answer == "a":
      score +=1
      print("congrats")
    else:
      print("sorry but the answer was:",right_answer)


#quiz_choicer is def so that I can call it at any time its purpose is to personalise thier quiz questions 11/5/22
def quiz_choicer():
  quiz_choicer_answer = input().lower()
  global right_answer
  global option_1
  global score
  global quizlength
  global option_2
  global list_end
  global list_start
  if score > (quizlength/2):
    print("congrats your score was",score/"/",quizlength,"or",(score/7)*100,"%")
  if quiz_choicer_answer == "a":
    print("you have selected animals")
    list_start = 0
    list_end = 7
    #four lists are reqired because there can be multiple incorrect translations
  elif quiz_choicer_answer == "b":
    print("you have selected objects")
    print("A:household objects or B: school objects?")
    ab = input().lower()
    if ab == "a":
      print("you have selected A:household objects")
      list_start = 8
      list_end = 15
    elif ab == "b":
      print("you have selected B: school objects")
      list_start = 16
      list_end = 22
    else:
      print("answer A/B/C/D/E/F or anwser quit to quit")
      quiz_choicer()
  elif quiz_choicer_answer == "c":
    print("you have selected family members")
  elif quiz_choicer_answer == "d":
    print("you have selected colours")
  elif quiz_choicer_answer == "e":
    print("you have selected all of the above, 50 questions")
    list_start = 0
    list_start = 50
  elif quiz_choicer_answer == "quit":
    quit()
  else: 
    print("answer A/B/C/D/E/F or answer quit to quit")
    quiz_choicer()
  for i in range (list_start,list_end):
    generate_question(english[i],right_answer[i],option_1[i],option_2[i])
quiz_choicer()