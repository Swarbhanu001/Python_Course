my_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
for i in range(0, len(my_list)):
    for j in range(i+1, len(my_list)):
        if my_list[i][1] > my_list[j][1]:
            my_list[i], my_list[j] = my_list[j], my_list[i]
print(my_list)