number_to_guess = 6

guess = int (input ("Please guess a number between 1 and 10: "))

while (guess != number_to_guess):    
    print ("Wrong!")
    if (guess < 6):
        print ("Too low")
        
    elif (guess > 6):
        print ("Too high")        

    guess = int (input ("Please guess another number between 1 and 10: "))

print (f"Correct, the number was {number_to_guess}")
