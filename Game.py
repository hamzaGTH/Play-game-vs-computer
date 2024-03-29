import random
while True:
 choices = ['rock','paper','scissors']
 y = random.choice(choices)
 user = None

 while user not in choices:
   user = input("rock,paper,scissor: ").lower()
 if user==y: 
  print("user: ",user)
  print("computer: ",y)
  print("Game tied!")
 elif user =="rock":
    if y =="paper":
        print("user: ",user)
        print("computer: ",y)
        print("You lose!")
    if y=="scissors":
        print("user: ",user)
        print("computer: ",y)
        print("You lose!")
 elif user =="paper":
    if y =="rock":
        print("user: ",user)
        print("computer: ",y)
        print("You won!")
    if y=="scissors":
        print("user: ",user)
        print("computer: ",y)
        print("You lose!")
 elif user =="scissors":
    if y =="rock":
        print("user: ",user)
        print("computer: ",y)
        print("You won!")
    if y=="paper":
        print("user: ",user)
        print("computer: ",y)
        print("You won!")
 tell = input("You want to play again yes/no? ".lower())
 if tell!="yes":
    break
print("Bye!!!!")