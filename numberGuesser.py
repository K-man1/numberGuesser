import random
try:
  lowNum = int(input("What is the lowest number you want the answer to be?\n"))
except ValueError:
  print("Error: Please enter a valid integer.")
  exit()
try:
  highNum = int(input("What is the highest number you want the answer to be?\n"))
except ValueError:
  print("Error: Please enter a valid integer.")
  exit()
if lowNum >= highNum:
    print("Either you are here to test my code, or you are just studpid, but please enter a valid number.")
    exit()
compInput= random.randint(lowNum, highNum)
userInput = ""
while userInput != str(compInput):
    userInput = input("Guess a number between " + str(lowNum) + " and " + str(highNum) + " or type 'give up' to give up.\n")
    if userInput == "give up":
        print("Oh no!😢 Well, the answer was "+ str(compInput)+".")
        exit()
    try:
        userInput = int(userInput)
    except ValueError:
            print("Error: Please enter a valid integer or write")
            exit()
    if  userInput < lowNum or userInput > highNum:
        print("Error: The number you have guessed is not inside of the vaules you have given.")
        exit()
    if userInput > compInput:
        print("Too high!")
    elif userInput < compInput:
        print("Too low!")
    else:
        print("Great job! You win!😁")