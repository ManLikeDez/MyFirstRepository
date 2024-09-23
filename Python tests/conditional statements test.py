test_score = int(input("Enter the assigned test score out of 100"))

if test_score > 80:
        print("Congratulations, you got an A !")
elif test_score > 70:
        print("Congratulations, you got a B !")
elif test_score < 70:
        print("Sorry you have failed HAHAHA.")


# Connectintg to business departments
def route_to_department():
  """Routes users to the correct department based on their query."""

  query = input("Please enter your query: ")

  if "sales" in query.lower():
    print("Please contact the Sales department.")
  elif "customer service" in query.lower():
    print("Please contact the Customer Service department.")
  elif "technical support" in query.lower():
    print("Please contact the Technical Support department.")
  elif "human resources" in query.lower():
    print("Please contact the Human Resources department.")
  elif "accounting" in query.lower():
    print("Please contact the Accounting department.")
  else:
    print("Your query doesn't match any of our departments. Please try again or contact our general information line.")

if __name__ == "__main__":
  route_to_department()
