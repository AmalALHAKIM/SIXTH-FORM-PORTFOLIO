import random
import time   #These will be downloaded, which will let the games later on work as intended

#This puts all allowed usernames and passwords in one, to make it easier to edit is needed and to take up less space
validUsers = {
    "HelloWorld": "beginnerCoder",
    "RaspberryPi": "3.14159",
    "Amal": "tryingtosurvive",
    "1":"1"
}
print("Hello! Welcome to the Sixth Form Portfolio Game! To begin, please enter your chosen username. ")

loggedIn = False
while not loggedIn:
    username = input("Enter Username:   ")
    
    if username in validUsers:  #Checks if the inputted username exists
        password = input("""Welcome! Please enter your password.
Password: """)
        
        if password == validUsers[username]:  #Checks the inputted password
            print("Identity verified. Hello,", username)
            loggedIn = True
        else:
            print("Wrong password, try again!")
    else:
        print("Whoops, I don't have that in my records! Try one of the usernames given.")

print("""


Here are your game options!
1. Amal's Super Complicated Number Guessing GameTM
2. Amal's Super Unique 'High Card, Low Card' GameTM
3. Amal's Super Reaction Time Tester GameTM
    (Despite her attempts, if you would like to play these again you will have to restart the entire code :D)
""")

gameChoice = int(input("Please enter the number of the game you'd like to play:  "))
#This next section of code only runs if the user has typed 1
if gameChoice == 1:
    randomNumber1 = random.randint(1, 10)
    print("""Access to Guessing Game: Verified.

    Amal's Super Complicated Number Guessing GameTM

    I have a number between 1 and 10. You have to guess what it is!""")

    attempts = 0 #counts how many tries the user takes
    while True:
        try:
            guess = int(input("Guess: "))
            attempts += 1 #adds 1 to the attempts number
        except ValueError: #if the user inputs a character that isn't an integer value
            print("Sorry! That's not a number. Try again.")
            continue

        if guess > randomNumber1:
            print("Nope! Go lower!")
        elif guess < randomNumber1:
            print("Nope! Go higher!")

        else:
            print("Good job! You guessed it in", attempts, "tries!") 
            break


if gameChoice == 2:
#This next section of code only runs if the user has typed 2
    print("""Access to Card Game: Verified
    
    High Card, Low Card (As seen on Animal Crossing)
    
    I'm going to give you a card, which has a number on it. You need to guess if the second card I have has a number that's higher or lower than the first one.""")
    cardOne = random.randint(1,10)
    print(f"""
    
    Card One:
     _____
    |     |
    |  {cardOne}  |
    |     |
     ----- """)

    cardTwo = random.randint(1,10) #this part checks to see if their answer aligns with the correct answer
    answer = input("So! Is the second card higher or lower than this first one?  ")
    if answer.lower() == "higher" and cardOne < cardTwo:
        print("Yes, that's right!")
    elif answer.lower() == "lower" and cardOne > cardTwo:
        print("Yes, that's right!")
    elif answer.lower() == "higher" and cardOne > cardTwo:
        print("Ooooh, tough luck! That wasn't right.")
    elif answer.lower() == "lower" and cardOne < cardTwo:
        print("Ooooh, tough luck! That wasn't right.")
    elif cardOne == cardTwo:
        print("Yeah, so... this was a trick question, the numbers are equal.")
    else:
        print("Sorry! I've been coded by a 16 year old, so I didn't understand that.")
    print(f"""Here's the second card:
    
     -----
    |     |
    |  {cardTwo}  |
    |     |
     -----""")

if gameChoice == 3:
#This next section of code only runs if the user has typed 2
    print("""    
Amal's Super Reaction Time Tester GameTM 
The moment you see the word 'GO', press Enter as fast as possible.
When you're pready, Press Enter...
""")
    input()
    waitTime = random.uniform(2,5) #This picks a random time between 2 and 5 seconds
    print("Get ready...")
    time.sleep(waitTime) #Then it implements the time chosen

    print("GO!")
    startTime = time.time()
    input() #Inputs are used here to record the Enter the user puts in
    endTime = time.time()

    reactionTime = endTime - startTime 
    print(f"Your reaction time was {reactionTime:.3f} seconds") #This puts the reaction time to 3 significant figures
    if reactionTime < 0.1:
        print(" Okay now you're just cheating...")
    elif reactionTime < 0.2:
        print(" Lightning fast!")
    elif reactionTime < 0.4:
        print(" Great reflexes!")
    elif reactionTime < 0.6:
        print(" Not bad!")
    elif reactionTime < 2:
        print(" Remember to blink *before* you start...")
    elif reactionTime < 4:
        print(" Maybe lay off on the spicy juice a bit next time, yeah?")
    else:
        print(" Try again, a bit slow!")


#This code has been made using references found online, adjusted to suit the game I wanted to make and the level of experience I have.
