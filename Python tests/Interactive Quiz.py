import random

def quiz_game():
  """Plays a quiz game with interactive input."""

  questions = [
    "What is the capital of France?",
    "Who painted the Mona Lisa?",
    "What is the largest planet in our solar system?",
    "What is the chemical symbol for gold?",
    "In what year did World War II end?"
  ]

  answers = [
    "Paris",
    "Leonardo da Vinci",
    "Jupiter",
    "Au",
    "1945"
  ]

  score = 0
  i = 0

  while i < len(questions):
    print(questions[i])
    user_answer = input("Your answer: ")

    if user_answer.lower() == answers[i].lower():
      print("Correct!")
      score += 1
    else:
      print("Incorrect. The correct answer is:", answers[i])

    i += 1

  print("Your final score is:", score, "out of", len(questions))

if __name__ == "__main__":
  quiz_game()