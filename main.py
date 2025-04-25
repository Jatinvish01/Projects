import random

'''
1 for snake
-2 for water
0 for gun
'''

computer  = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {"s" : 1, "w" : -1, "g" : 0}
reverDict = {1 : "Snake", -1 : "Water", 0 : "Gun"}

you = youDict[youstr]

print(f"You choose {reverDict[you]}\nComputer choose: {reverDict[computer]}")

if(computer == you):
      print("Its a Draw")
else:
      if(computer ==-1 and you ==-1):
            print("You won!")
      elif(computer ==-1 and you ==0):
            print("Your lose!")
      elif(computer ==1 and you ==-1):
            print("You lose!")
      elif(computer ==1 and you == 0):
            print("You win!")
      elif(computer ==0 and you ==-1):
            print("You lose!")
      elif(computer ==0 and ypu ==1):
            print("You lose!")
      else:
            print("Somthing wan't wrong!!")