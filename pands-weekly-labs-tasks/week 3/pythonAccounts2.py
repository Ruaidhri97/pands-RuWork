#Program that delivers a 4 digit identifier for online shoppers based on their full bank number
#Author: FARO-P
Banknumber = str (input("Please enter an 10 digit account number: "))
Final4 = (Banknumber[-4:])
Hidden = 'X' * (len(Banknumber) - 4) + Final4
print (Hidden)