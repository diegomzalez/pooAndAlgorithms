import random

def binary_search(list: list, start: int, end: int, objective: int, i=0) -> bool:
  i = i + 1
  if (start > end):
    return False, i
  middle = (start + end) // 2
  if list[middle] == objective:
    return True, i
  elif list[middle] < objective:
    return binary_search(list, middle + 1, end, objective)
  else:
    return binary_search(list, start, middle - 1, objective)

def main() -> None:
  list_size = int(input("How long will be the list?"))
  objective = int(input("What number do you want to find?"))
  list = sorted([random.randint(0, 100) for i in range(list_size)])
  isFound = binary_search(list, 0, len(list), objective)
  print(f'The element {objective} {"is" if isFound else "isnt"} in the list')
  print(isFound)
if __name__ == "__main__":
  main()