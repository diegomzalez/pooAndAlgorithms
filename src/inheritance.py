class Rectangle:
  def __init__(self, base: int, height: int) -> None:
      self.base = base
      self.height = height

  def area(self):
    return self.base * self.height


class Square(Rectangle):

  def __init__(self, side: int) -> None:
      super().__init__(side, side)


def main() -> None:
  rectangle = Rectangle(10, 57)
  print(rectangle.area())
  square = Square(10)
  print(square.area())

if __name__ == "__main__":
  main()