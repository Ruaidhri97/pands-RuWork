number_to_guess = 9

guess = int (input ("Please guess a number between 1 and 10: "))

while (guess != number_to_guess):
    print ("Wrong!")
    guess = int (input ("Please guess another number between 1 and 10: "))

print (f"Correct, the number was {number_to_guess}")

