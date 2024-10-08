def add_and_multiply(num1, num2, num3):
    result =  (num1 + num2) * num3
    return result 

print(add_and_multiply(3, 5, 6))

#Greeting fuction

def greet():
    name = input("Please enter your name")
    print(f"Hello {name} !")

 
greet()

#Increment Counter
def increment_counter(current_count):
    return current_count + 1

count = 4
counter = increment_counter(count)
print(counter)

#Calculate Total
def calculate_total(prices):
    total = 0
    for price in prices:
        total += price
    return total

games_prices = [45, 34, 23, 45, 12]
total_cost =  calculate_total(games_prices)
print(f"The total cost of the games comes to £{total_cost}.")
