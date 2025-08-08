#practice
print("TIm is bitCH".lower())
inp=input("Enter some shit: ").lower()



#actual program
print('Welcome to quiz babes :3')
score=0

playing= input("Wanna play?(y/n) : ")
if playing.lower() != "y":
    quit()                   #terminates the program
print("KKKK let's play :)")

answer=input("What does CPU stand for? ")
if answer.lower()== "central processing unit":
    print('Correct!! :3')
    score+=1
else:
    print("U wrong twin :(")

answer=input("What does RAM stand for? ")
if answer.lower()== "random access memory":
    print('Correct!! :3')
    score+=1
else:
    print("U wrong twin :(")

answer=input("What does GPU stand for?  ").lower()
if answer== "graphics processing unit":
    print('Correct!! :3')
    score+=1
else:
    print("U wrong twin :(")

print(f"Your score is {score}")
print(f"your got {(score/3)*100}% of questions correct")
