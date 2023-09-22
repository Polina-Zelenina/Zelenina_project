import time

# Завдання 1
""" number = int(input())
print(number >= 100) """

# Завдання 2
""" number_1, number_2 = float(input()), float(input())

if number_1 > number_2:
    print(f"{number_1} bigger than {number_2}")
else:
    print(f"{number_2} bigger than {number_1}") """

# Завдання 3
""" word = input()

if word == 'Spathiphyllum':
    print('Yes - Spathiphyllum is the best plant ever!')
elif word == 'spathiphyllum':
    print('No, I want a big Spathiphyllum!')
else:
    print('Spathiphyllum! Not [input]!') """

# Завдання 4
""" income = float(input("Enter the annual income: "))

if income < 85528:
    impost = (income * 0.18) - 556.2
else:
    impost = ((income - 85528) * 0.32) + 14839.2

if impost < 0:
    print('The tax is: 0.0 thalers')
else:
    print(f'The tax is: {round(impost)}.0 thalers') """

# Завдання 5
""" number_of_year = int(input())

if number_of_year >= 1582:
    if number_of_year % 4 != 0:
        print('Common year')
    elif number_of_year % 100 != 0:
        print('Leap year')
    elif number_of_year % 400 != 0:
        print('Common year')
    else:
        print('Leap year')
else:
    print('Not within the Gregorian calendar period') """

# Завдання 6
""" secret_number = 777

print(
'''
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
''')

attention = 1

while secret_number != attention:
    attention = int(input())

    if attention != secret_number:
        print('Ха-ха! Ви застрягли у моїй петлі!')
    else:
        print('Молодець, магле! Тепер ти вільний') """

# Завдання 7
""" for i in range(1, 6):
    print(f"{i} Mississippi")
    time.sleep(1)
print('Ready or not, here I come!') """

# Завдання 8
""" i = True

while i is True:
    word = input()
    if word == 'chupacabra':
        print('You\'ve successfully left the loop.')
        break """

# Завдання 9
""" user_word = input().upper()

for i in user_word:
    if i in 'AEIOU':
        continue
    print(i) """

# Завдання 10
""" word_without_vowels = ""
user_word = input().upper()

for i in user_word:
    if i in 'AEIOU':
        continue
    word_without_vowels += i
print(word_without_vowels) """

# Завдання 11
""" blocks = int(input())
height = 0

for i in range(1, blocks):
    if blocks >= i:
        blocks -= i
        height += 1

print(f'The height of the pyramid: {height}') """

# Завдання 12
""" my_number = int(input())
steps = 0

while my_number != 1:
    if my_number % 2 == 0:
        my_number /= 2
    else:
        my_number = 3 * my_number + 1
    steps += 1
    print(int(my_number))

print(f"steps = {steps}") """