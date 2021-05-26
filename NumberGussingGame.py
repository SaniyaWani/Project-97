import random 
chance = 5
randomNum = random.randrange(0, 9)
print(randomNum)

print ("Hi, I am having a number in my mind between 0 t0 9. You have only 5 chance to guess")
numu = int(input("Enter you guess"))
print (numu)
if (chance != 0):
 if (numu > randomNum):
    #chance = chance-1
    print("Your guess was to high. Try to guess a smaller number. You have"+str(chance)+"chance left" )
    print(numu)
   
 elif (numu < randomNum):
    chance = chance-1
    print("Your guess was to low. Try to guess a bigger number. You have"+str(chance)+"chance left")
    print(numu)
 elif (numu == randomNum):
    print("Congratulations! You gussed it right")
elif(chance == 0):
    print("All your guess were wrong")    
