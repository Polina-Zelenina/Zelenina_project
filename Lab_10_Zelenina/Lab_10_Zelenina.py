# Завдання 1
""" def word_hidden(word, combination):

    for char in combination:
        if word.find(char) == -1:
            return False
    return True


word = input("Введіть слово: ")
combination = input("Введіть комбінацію символів: ")

result = word_hidden(combination, word)

if result:
    print("Yes")
else:
    print("No") """


# Завдання 2
def value_of_birth(date_birthday):
    while True:
        summa_numbers = 0
        for i in range(len(date_birthday)):
            summa_numbers += int(date_birthday[i])
        date_birthday = str(summa_numbers)

        if len(date_birthday) == 1:
            break
    return date_birthday


is_flag = True

while is_flag:
    enter_the_date = input("Enter the your birthday value on format like -> YYYYMMDD: ")
    if not enter_the_date.isdigit() and len(enter_the_date) != 8:
        print("Value error, repeat please")
    else:
        print(value_of_birth(enter_the_date))
        break

# Завдання 3
""" def get_valid_input(prompt, min_value, max_value):
    while True:
        try:
            entered_value = int(input(prompt))
            if min_value <= entered_value and entered_value <= max_value:
                return entered_value
            else:
                print(f"Error: your value not in range({min_value}..{max_value})")
        except ValueError:
            print("Error: wrong input, please enter an integer.")

entered_value = get_valid_input(
    f"Enter a number within the range ({1}..{100}): ", 1, 100)
print(f"You entered: {entered_value}") """
