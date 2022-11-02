import random
NUMOF_RANDOM_NUMBERS = 6
MINIMUM = 1
MAXIMUM = 46

numof_quick_picks = int(input("Number of quick picks"))
numbers = [1]

for i in range(numof_quick_picks):
    numbers = [1]
    for j in range(NUMOF_RANDOM_NUMBERS):
        number = random.randint(MINIMUM, MAXIMUM)
        while number in numbers:
            number = random.randint(1, 46)
        numbers.append(number)
    print(" ". join(f"{number:2}" for number in numbers))