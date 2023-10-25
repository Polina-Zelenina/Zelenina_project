# Завдання 1
""" from random import randint as r_int

list_to_tuple = tuple([r_int(1, 100) for _ in range(10)])

number = int(input())

list_to_lower_numbers = [list_to_tuple[i] for i in range(len(list_to_tuple)) if list_to_tuple[i] < number]

print(list_to_lower_numbers) """

# Завдання 2
""" tuple_of_strings = tuple([input() for _ in range(3)])

print(', '.join(tuple_of_strings)) """

# Завдання 3
""" dict_of_books = {
    'Гаррі Поттер': {
        'Автор': 'Дж. К. Роулінг',
        'Рік видання': 1997,
        'Кількість сторінок': 451
        },
    'Алісині пригоди у Дивокраї': {
        'Автор': 'Льюїс Керролл',
        'Рік видання': 1865,
        'Кількість сторінок': 144
        },
    'Маленький принц': {
        'Автор': 'Антуан де Сент-Екзюпері',
        'Рік видання': 1943,
        'Кількість сторінок': 96
        },
    'Тореадори з Васюківки': {
        'Автор': 'Всеволод Нестайко',
        'Рік видання': 1973,
        'Кількість сторінок': 544
        },
    'Пригоди Олівера Твіста': {
        'Автор': 'Чарлз Діккенс',
        'Рік видання': 1838,
        'Кількість сторінок': 379
        },
    }
name_author = input()
for i in dict_of_books:
    isFlag = None
    if name_author == i:
        for j in dict_of_books[i]:
            print(f"{j}: {dict_of_books[i][j]}")
        isFlag = True
        break

if not isFlag:
    print("Не змогли знайти Вашу книгу") """

# Завдання 4
""" students_list = [
    ['Jace', 197, 84, 'Kt-81'],
    ['Olgerd', 174, 55, 'Pga-99'],
    ['Mario', 131, 40, 'Yt-1-1'],
    ['Viktor', 198, 96, 'Mpt-56'],
    ['Jinx', 164, 44, 'Ap-33'],
]

dict_values = {i[0]: (i[1], i[2], i[3]) for i in students_list}
name_student = input()

for i in dict_values:
    if i == name_student:
        print(f"Height: {dict_values[i][0]}, Weight: {dict_values[i][1]}, Group: {dict_values[i][2]}")
        break """

# Завдання 5
def add_new_contact(list_contacts, name, number):
    list_contacts.append([name, number])
    return list_contacts

def find_contacts(list_numbers):
    dict_numbers = {}
    for i in list_numbers:
        if i[0] not in dict_numbers:
            dict_numbers[i[0]] = [i[1]]
        else:
            dict_numbers[i[0]].append(i[1])
    return dict_numbers

list_contacts = [
    ['Jace', '0967131242'],
    ['Carol', '03921389421132'],
    ['Viktor', '31283712848'],
    ['Mario', '0673781256817'],
    ['Jinx', '37216784617825421673512371']
]

add_new_contact(list_contacts, 'Viktor Belford', '+3872184627821')
dict_contacts = find_contacts(list_contacts)
print(dict_contacts)