# Завдання 1
""" hat_list = [1, 2, 3, 4, 5]

hat_list[2] = int(input())
del hat_list[-1]
print(len(hat_list))

print(hat_list) """

# Завдання 2
""" sort_list = [63, 80, 62, 69, 71, 37, 12, 90, 19, 67]

for i in range(len(sort_list)-1):
    for j in range(len(sort_list)-i-1):
        if sort_list[j] > sort_list[j+1]:
            sort_list[j], sort_list[j+1] = sort_list[j+1], sort_list[j]
 
print(sort_list) """

# Завдання 3
""" my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []

for i in my_list:
    if i not in new_list:
        new_list.append(i)
        
print("The list with unique elements only:")
print(new_list) """

# Завдання 4
""" chess = [["♖" if (i == 0 or i == 7) and (j == 0 or j == 7) else "_" for j in range(8)] for i in range(8)]

for i in chess:
    print(*i) """