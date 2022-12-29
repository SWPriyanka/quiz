print("Welcome To My Quiz!")

playing = input("Do You Want To Play? ")

if playing.lower() != "yes":
    quit()

print("okay! Let's play") 
score=0 
answer= input("What UI stands for? ")
if answer.lower() =="user interface":
    print('Correct,Voila!')
    score += 1
else :
    print('Incorrect')

answer= input("What CSS stands for? ")
if answer.lower() =="cascading style sheet":
    print('Correct,Voila!')
    score += 1
else :
    print('Incorrect')

answer= input("What  HTML stands for? ")
if answer.lower() =="hyper text markup language":
    print('Correct,Voila!')
    score += 1
else :
    print('Incorrect')

answer= input("what is GUI stands for? ")
if answer.lower() =="graphical user interface":
    print('Correct,Voila!')
    score += 1
else :
    print('Incorrect')

print("You got " + str (score) + " questions correct ! ")