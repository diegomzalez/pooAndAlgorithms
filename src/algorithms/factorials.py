def factorial(n: int) -> int:
  """Calculates the factorial of n

  Args:
      n (int): n > 0

  Returns:
      int: factorial of n
  """
  print(n)
  if n == 1:
    return 1
  return n * factorial((n - 1))

def main() -> None:
  n = int(input("Write an int number: "))
  print(factorial(n))

if __name__ == "__main__":
  main()