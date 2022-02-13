def bag(bag_size: int, weight: list, values: list, n: int):
  if (n == 0) or (bag_size == 0): 
    return 0
  if (weight[(n - 1)] > bag_size):
    return bag(bag_size, weight, values, (n - 1))

  return max(values[(n - 1)] + bag(bag_size - weight[(n -1)], weight, values, (n - 1)),
            bag(bag_size, weight, values, n - 1))

def main() -> None:
  print(bag(5, [10, 20, 30], [60, 100, 120], len([60, 100, 120])))

if __name__ == "__main__":
  main()