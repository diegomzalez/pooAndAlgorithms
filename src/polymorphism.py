class Person:
  def __init__(self, name) -> None:
      self.name = name

  def get_moving(self) -> None:
    print('I am walking')

class Cyclist(Person):
  def __init__(self, name) -> None:
      super().__init__(name)

  def get_moving(self) -> None:
      print('I am moving on my bike')

def main():
  person = Person("Diego")
  person.get_moving()
  cyclist = Cyclist("Jorge")
  cyclist.get_moving()

if __name__ == "__main__":
  main()