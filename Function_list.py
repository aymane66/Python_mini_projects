def under_ten_list(list_of_numbers):
    filtered_list = []
    for i in list_of_numbers:
        if i < 10:
            filtered_list.append(i)
    print(filtered_list)


under_ten_list([1, 81, 45, 3, 9, 35, 44, 6])
