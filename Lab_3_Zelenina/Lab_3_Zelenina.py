# #Завдання 1
# var = float(input("Enter value for x: "))
# mu = float(input("Enter value for mu: "))
# sigma = float(input("Enter value for sigma: "))
# Pi = 3.14159265359
# e = 2.71828
# Gaussian_function = (1 / (sigma * (2 * Pi)**0.5)) * (e)**(-((var - mu)**2) / (2 * sigma**2))
# print("Функція Гауса = ", Gaussian_function)
#
# #Завдання 2
# john = 3
# mary = 5
# adam = 6
# print(john,mary,adam, sep=", ")
# totalApples = john + mary + adam
# print(totalApples)
# print("Загальна кількість яблук: ", totalApples)
#
# #Завдання 3
# kilometers = 12.25
# miles = 7.38
#
# miles_to_kilometers = miles * 1.61
# kilometers_to_miles = kilometers / 1.61
#
# print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
# print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
#
# #Завдання 4
# x = input("Enter value for x: ")
# x = float(x)
# y = 3 * x**3 - 2 * x**2 + 3**x - 1
# print("y =", y)
#
# #Завдання 5
# # this program computes the number of seconds in a given number of hours
#
# hours = 2
# seconds = 3600
#
# print("Hours: ", hours)
# print("Seconds in Hours: ", hours * seconds)
#
# print("Goodbye")
#
# #Завдання 6
# first_number = float(input("Enter value for first_number: "))
# second_number = float(input("Enter value for second_number: "))
#
# print("first_number + second_number = ", first_number + second_number)
# print("first_number - second_number = ", first_number - second_number)
# print("first_number * second_number = ", first_number * second_number)
# print("first_number / second_number = ", first_number / second_number)
#
# print("\nThat's all, folks!")
#
# #Завдання 7
# x = float(input("Enter value for x: "))
#
# y = 1 / (x + (1 / (x + (1 / (x + (1 / (x + (1 / x))))))))
#
# print("y =", y)
#
# #Завдання 8
# hour = int(input("Starting time (hours): "))
# mins = int(input("Starting time (minutes): "))
# dura = int(input("Event duration (minutes): "))
#
# start_time = hour * 60 + mins
# start_time_of_work = start_time + dura
#
# hours = (start_time_of_work // 60) % 24
# minutes = start_time_of_work % 60
#
# print(hours, minutes, sep = ":")
