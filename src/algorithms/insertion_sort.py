def insertion_sort_1(list: list) -> list:

    for index in range(1, len(list)):
        value = list[index]
        i = index - 1
        while i >= 0:
            if value < list[i]:
                list[i+1] = list[i]
                list[i] = value
                i -= 1
            else:
                break
    return list
def insertion_sort_2(list: list) -> list:
    for indice in range(1, len(list)):
        current_value = list[indice]
        current_position = indice

        while current_position > 0 and list[current_position - 1] > current_value:
            list[current_position] = list[current_position - 1]
            current_position -= 1

        list[current_position] = current_value
    return list

print(insertion_sort_1(list=[4, 10, 6, 7, 3]))
print(insertion_sort_2(list=[4, 10, 6, 7, 3]))