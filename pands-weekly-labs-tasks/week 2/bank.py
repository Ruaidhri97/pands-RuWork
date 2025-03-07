#Prompt the user and read in two money amounts (in cent)
#Add the two amounts
#Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
Number1 = int(input("Enter your sum in cents: "))
Number2 = int(input("Enter your sum in cents: "))
Output = float((Number1 + Number2) / 100)
print ("Your summary balance is {}".format(Output))
