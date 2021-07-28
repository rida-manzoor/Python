# We choose a number and then user guess it. There is limited number of guesses.

GNumber = 18
print("Guess the Number")
#number = int(input())
x = 1
while x < 6 :
    number = int(input())
    if number > GNumber:
        print("Number is smaller than entered number.")
    elif number < GNumber:
        print("Number is greater than entered number.")
    elif number == GNumber:
        print("You won the game.")
        break
    print(5-x, "Number of guesses left.")
    x += 1

if x > 5:
    print("Oop! Game Over.\n Better Luck Next Time.")
