import random

choices = ["rock", "paper", "scissor"]

while True:
      user_choice = input("Enter the your choice (rock, paper, scissor): ").lower()
      
      if(user_choice not in choices):
            print("Invaild choice, Try Again!..")

      computer_choice = random.choice(choices)
      print(f"Computer choice: {computer_choice}")

      if(user_choice == computer_choice):
            print("The match will Tie!!..")

      elif (
            (user_choice == "rock" and computer_choice == "scissor") or
            (user_choice == "scissor" and computer_choice == "paper") or
            (user_choice == "paper" and computer_choice == "rock")
      ):
          print("YOU WIN!!")  
      
      else:
            print("Computer Win!")

      play_again = input("Play Again? (yes/no): ").lower()

      if(play_again != "yes"):
            print("Thanks for playing")
            break
