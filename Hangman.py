import random

alphabet = "abcdefghijklmnopqrstuvwxyz"
aList = ['strawberry','date','grape','raisin','coconut','banana','orange','mango','apple','watermelon','lemon','kiwi','pineapple','avacado','grapefruit','pear','peach','cherry','cranberry','blueberry']
spaces = []
mysteryword = random.choice(aList) 
lengthofword = len(mysteryword)
correctguesses = []



def game():

    for character in mysteryword: 
        spaces.append("-")

    print("The category of the game is Fruits!")

    print(spaces)

def guessing():


        wrongguesses = 1

        while wrongguesses < 7:


            guess = input("Pick a letter:   ").lower()

            if guess in correctguesses: 
                print("You already guessed that")
            else: 

                correctguesses.append(guess)
                if guess in mysteryword:
                    print("You guessed correctly!")
                    for x in range(0, lengthofword):
                        if mysteryword[x] == guess:
                            spaces[x] = guess
                            print(spaces)




                
                if guess in mysteryword:
                    print("You guessed correctly!")
                    

                    if not '-' in spaces:
                        print("You won!")
                        
                else:
                    print("nope, try again!")
                    wrongguesses += 1

                    if wrongguesses == 2:
                        print("---|")
                        print("   O")

                    if wrongguesses == 3:
                        print(" ---|")
                        print("    O")
                        print("    | ")
                        print("    | ")
                        

                    if wrongguesses == 4:
                        print(" ---|")
                        print("    O")
                        print("   /| ")
                        print("    | ")
                        
                    if wrongguesses == 5:
                        print(" ---|")
                        print("    O")
                        print("   /|\ ")
                        print("    | ")

                    if wrongguesses == 6:
                        print(" ---|")
                        print("    O")
                        print("   /|\ ")
                        print("    | ")
                        print("   /  ")

                    if wrongguesses == 7:
                        print(" ---|")
                        print("    O")
                        print("   /|\ ")
                        print("    | ")
                        print("   / \ ") 
                        print(" You ran out of tries! You lost!! The correct word was",mysteryword)
                        print("HELLLLLLP MEEEEEEEEEEEEE!")




game()
guessing()
