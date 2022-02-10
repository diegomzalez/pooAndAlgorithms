import random
def linear_search(list: list, objective: int, match=False, i=0) -> bool:
  for element in list:
    i += 1
    if element == objective:
      match = True
      break
  print(i)
  return match

def main() -> None:
  # O (n)
  list_size = int(input("How long will be the list? "))
  objective = int(input("What number do you want to find? "))
  list = [random.randint(0, 100) for i in range(list_size)]
  isFound = linear_search(list, objective)
  print(list)
  print(f'The {objective} element {"is" if isFound else "isnt"} in the list')

if __name__ == "__main__":
  main()