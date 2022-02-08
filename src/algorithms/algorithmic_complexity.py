import time

def factorial(n):
  response = 1

  while n > 1:
    response *= n
    n -= n

  return response

def r_factorial(n):
  if n == 1:
    return 1

  return n * factorial(n - 1)

def main():
  n = 1000

  start_at = time.time()
  end_at = time.time()
  print(end_at - start_at)

  start_at = time.time
  end_at = time.time()
  print(end_at - start_at)
if __name__ == "__main__":
  main()