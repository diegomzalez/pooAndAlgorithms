

def binary_conversor(x: int) -> int:
  print(x)
  if x > 2:
    return binary_conversor(x // 2)

def main() -> None:
  print(binary_conversor(25))

if __name__ == "__main__":
  main()