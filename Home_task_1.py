import random

numbers = list(range(1001))
list_100_random_numbers = random.sample(numbers, 100)

# print(list_100_random_numbers)


for i in range(len(list_100_random_numbers)):
    for j in range(0, len(list_100_random_numbers) - i - 1):
        if list_100_random_numbers[j] > list_100_random_numbers[j + 1]:
            list_100_random_numbers[j], list_100_random_numbers[j + 1] = list_100_random_numbers[j + 1], list_100_random_numbers[j]

# print(list_100_random_numbers)

# Separate even and odd numbers
even_numbers = [num for num in list_100_random_numbers if num % 2 == 0]
odd_numbers = [num for num in list_100_random_numbers if num % 2 != 0]

# Calculate average for even numbers
if even_numbers:
    even_average = sum(even_numbers) / len(even_numbers)
else:
    even_average = 0  # Handle case when there are no even numbers

if odd_numbers:
    odd_average = sum(odd_numbers) / len(odd_numbers)
else:
    odd_average = 0

# Print the results
# print(f"Even numbers: {even_numbers}")
# print(f"Odd numbers: {odd_numbers}")
print(f"Average of even numbers: {even_average}")
print(f"Average of odd numbers: {odd_average}")


x = 9 ** 19 - int(float(9**19))

print (x)

name = input()
print ('Hello ', name )
