import random                        # always import on top



#acutal code
user_win=0
computer_win=0

options=['rock','paper','scissors']

while True:
    user_guess=input("Enter Rock/ Paper/ Scissors or Q to quit: ").lower()
    if user_guess=='q':
        break
    computer_guess= options[random.randint(0,2)]
    print(user_guess)
    print(computer_guess)

    if user_guess=='rock' and computer_guess=="scissors":
        print("You won!")
        user_win+=1
    elif user_guess=='paper' and computer_guess=="rock":
        print("You won!")
        user_win+=1
    elif user_guess=='scissors' and computer_guess=="paper":
        print("You won!")
        user_win+=1
    else:
        print("You lost :(")
        computer_win+=1
print(f" Your wins are {user_win} and computer wins are {computer_win} ")