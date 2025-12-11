import random

print ( "This is the guessing game" )

number = random.randint(1,10)
print ("I have already guessed a number")
print("You have 3 guesses")
guesses_used = 0
while True:
    usernum = int(input("Take a guess:"))
 
    guesses_used = guesses_used+1
 
    if usernum < number:
        print ("number is low")

    elif usernum > number:
        print ("number is high")
    
    else:
        print ("Perfect mate, you found the number")

        break
    
    if guesses_used >= 3:
        print ("attempts exceeded")
        break