import random

def bubble_sort(list: list) -> list:
  n = len(list)
  for i in range(n):
    for j in range(0, n - i - 1):
      if (list[j] > list[j + 1]):
        list[j], list[j + 1] = list[j + 1], list[j ]
  return list
def main() -> None:
  list_size = int(input('How long will be the list? '))

  list = [random.randint(0, 100) for i in range(list_size)]
  print(list)

  sorted_list = bubble_sort(list)
  print(sorted_list)

if __name__ == "__main__":
  main()