#Praticing Sets
x = [2, 3,4, 5, 6]

y = [7, 8, 9, 10, 11, 6]

y.reverse()

print (y)

#Staircase

steps = 5 
for step in range(1, steps + 1):
    print(' ' * (steps - step) + '*' * step)


#Looping

numbers = [1, 2, 3, 4, 5]

total_sum = 0

for number in numbers:
    print(number)
    total_sum += number

#Print the total:
print(f"The total sum is: {total_sum}")
