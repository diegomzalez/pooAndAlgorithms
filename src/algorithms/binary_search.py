import random
def binary_search(list: list, objective, match=False) -> bool:
  for element in list:
    if element == objective:
      match = True
      break
  return match

def main() -> None:
  list_size = int(input("How long will be the list? "))
  objective = int(input("What number do you want to find? "))
  list = [random.randint(0, 100) for i in range(list_size)]
  isFound = binary_search(list, objective)
  print(list)
  print(f'El elemento {objective} {"esta" if isFound else "no esta"} en la lista')

if __name__ == "__main__":
  main()