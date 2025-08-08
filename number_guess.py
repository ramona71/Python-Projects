import random
start,end= -21,10             
print(random.randint(start, end))       #include 10
print(random.randrange(start, end))     #doesn't include 10
print(int("25"))                      

#actual code
top_range=input("Type the top range number: ")
if top_range.isdigit():
    top_range=int(top_range)
    if top_range<=0:
        print('Type a number larger than 0') 
        quit()
else:
    print("Type a digit next time hoe")
    quit()

random_no=random.randint(0,top_range)
print(random_no)
guesses=0 

while True:     
    guesses+=1                           # random_no != user_guess
    user_guess=input("Make a guess: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Type a digit greater than 0 next time hoe")
        continue                           # skips everything below ts and goes to next iteration
    
    if user_guess== random_no:
        print("Correct !!")
        break
    elif user_guess > random_no:
        print("You are above the no") 
    else:
        print("You are below the number")

print("You got it in" ,guesses, "guesses")    # ,guesses,  = + guesses +