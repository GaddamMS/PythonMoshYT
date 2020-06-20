# find largest number in a list
import random
numbers = []

for number in range(10, 47):
    numbers. append(random.randrange(5,80))

max_number = numbers[0]
for number in numbers:
    if max_number < number:
        max_number = number
print(max_number)

print(max_number == max(numbers))