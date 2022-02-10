import random

def merge_sort(list: list) -> list:
  if len(list) > 1:
    list_half = len(list) // 2
    list_left_side = list[:list_half]
    list_right_side = list[list_half:]
    print(list_left_side, "*" * 5, list_right_side)

    # recursive call at each half
    merge_sort(list_left_side)
    merge_sort(list_right_side)

    # Iterators to loop throught both lists
    i = 0
    j = 0

    # Iterator for main list
    k = 0

    while i < len(list_left_side) and j < len(list_right_side):
      if list_left_side[i] < list_right_side[j]:
        list[k] = list_left_side[i]
        i += 1
        print(i)
      else:
        list[k] = list_right_side[j]
        j += 1
        print(k)
      k += 1
      print(k)
    while i < len(list_left_side):
      list[k] = list_left_side[i]
      i += 1
      k += 1
    while j < len(list_right_side):
      list[k] = list_right_side[j]
      j += 1
      k += 1
    print(f'left {list_left_side}, right {list_right_side}')
    print(list)
    print('-' * 58)
  return list
if __name__ == "__main__":
  list_size = int(input('How log will be the list? '))

  list = [random.randint(0, 100) for i in range(list_size)]
  print(list)
  print('-' * 20)

  sorted_list = merge_sort(list)
  print(sorted_list)