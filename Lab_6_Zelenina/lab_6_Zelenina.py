# Завдання 1
""" def is_year_leap(year) -> bool:
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed") """

# Завдання 2
""" def is_year_leap(year) -> bool|None:
    if type(year) == float:
        return None
    if type(year) == str:
        return None

    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year: int, month: int) -> int|bool:
    if is_year_leap(year) == None:
        return None
    if type(month) == float:
        return None
    if type(month) == str:
        return None
    if 12 < month or month < 1:
        return None

    if is_year_leap(year):
        if month == 2:
            return 29
    else:
        if month == 2:
            return 28
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    if month in [4, 6, 9, 11]:
        return 30


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed") """

# Завдання 3
""" def is_year_leap(year):
    if type(year) == float:
        return None
    if type(year) == str:
        return None

    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if type(month) == float:
        return None
    if type(month) == str:
        return None
    if is_year_leap(year) == None:
        return None
    if 12 < month or month < 1:
        return None

    if is_year_leap(year):
        if month == 2:
            return 29
    else:
        if month == 2:
            return 28
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    if month in [4, 6, 9, 11]:
        return 30

def day_of_year(year, month, day):
    if type(day) == float:
        return None
    if days_in_month(year, month) is None:
        return None
    if 31 < day or day < 1:
        return None

    total_days = day
    for day in range(1, month):
        total_days += days_in_month(year, day)
    return total_days

print(day_of_year(1999, 12, 31)) """

# Завдання 4
""" def is_prime(number):
    total = 0
    for i in range(2, number + 1):
        if number % i == 0:
            total += 1
        if total == 2:
            break
    if total == 2:
        return False
    else:
        return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ") """

# Завдання 5
""" def liters_100km_to_miles_gallon(liters):
    return (100 / liters) / 1.609344 * 3.785411784

def miles_gallon_to_liters_100km(miles):
    return (100 / miles) / 1.609344 * 3.785411784

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5)) """

# Завдання 6
""" def is_a_triangle(siteA, siteB, siteC):
    total = 0

    if siteA + siteB > siteC:
        total += 1
    if siteA < siteB + siteC:
        total += 1
    if siteA + siteC > siteB:
        total += 1

    if total == 3:
        return True

    return False
print(is_a_triangle(3, 5, 6)) """


# Завдання 7
def is_a_right_triangle(siteA, siteB, siteC):
    isFlag = False

    if siteA > siteB and siteA > siteC and siteA ** 2 == siteB ** 2 + siteC ** 2:
        isFlag = True
    if siteB > siteA and siteB > siteC and siteB ** 2 == siteA ** 2 + siteC ** 2:
        isFlag = True
    if siteC > siteB and siteC > siteA and siteC ** 2 == siteA ** 2 + siteB ** 2:
        isFlag = True

    return isFlag


print(is_a_right_triangle(6, 8, 10))
