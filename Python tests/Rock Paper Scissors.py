import random

def get_computer_choice():
  """Generates a random choice for the computer."""
  choices = ["rock", "paper", "scissors"]
  return random.choice(choices)

def get_user_choice():
  """Gets the user's choice."""
  while True:
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    if user_choice in ["rock", "paper", "scissors"]:
      return user_choice
    else:
      print("Invalid choice. Please enter rock, paper, or scissors.")

def determine_winner(user_choice, computer_choice):
  """Determines the winner of the game."""
  if user_choice == computer_choice:
    return "It's a tie!"
  elif (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "paper" and computer_choice == "rock") or \
       (user_choice == "scissors" and computer_choice == "paper"):
    return "You win!"
  else:
    return "Computer wins!"

def play_game():
  """Plays a single round of Rock, Paper, Scissors."""
  computer_choice = get_computer_choice()
  user_choice = get_user_choice()
  result = determine_winner(user_choice, computer_choice)
  print(f"You chose: {user_choice}")
  print(f"Computer chose: {computer_choice}")
  print(result)

if __name__ == "__main__":
  play_game()