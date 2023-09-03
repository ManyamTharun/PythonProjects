import random
import math
# Taking input range from user
LowerBound = int(input("Enter the Lower Bound: "))
UpperBound = int(input("Enter the Upper Bound: "))
# Generating random number1
ran_no = random.randint(LowerBound, UpperBound)
# Generating no of guesses based on upper and lower boundaries
NoOfGuesses = round(math.log(UpperBound - LowerBound + 1, 2))
print("You have only {} guesses".format(NoOfGuesses))
count = 0
for i in range(1, NoOfGuesses + 1):
    Guess = int(input("Guess a number: "))
    count += 1
    if Guess == ran_no:
        print("You guess is correct!")
        print("You guessed at {}th guess".format(count))
        break
    elif Guess > ran_no:
        print("Your guess in high")
    else:
        print("Your guess is low")
if count > ran_no:
    print("You chances of guessing is completed")
