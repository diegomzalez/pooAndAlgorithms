def fibonnacci(n: int) -> int:
  if n == 0 or n == 1:
    return 1
  return fibonnacci(n - 1) + fibonnacci(n - 2)

def main() -> None:
  n = int(input("Enter the value of n: "))
  print(fibonnacci(n))
if __name__ == "__main__":
  main()