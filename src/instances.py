class Coordinate:

  def __init__(self, x: int, y: int) -> None:
      self.x = x
      self.y = y

  def distance(self, another_coordinate: int) -> float:
    x_diff = (self.x - another_coordinate.x)**2
    y_diff = (self.y - another_coordinate.y)**2
    return ((x_diff + y_diff)**0.5)

def main():
  coord_1 = Coordinate(3, 30)
  coord_2 = Coordinate(4, 8)
  print(f"The distance is: {coord_1.distance(coord_2)}")
  print(f"coord_2 is istance of Coordinate ?: {isinstance(coord_2, Coordinate)}")
if __name__ == "__main__":
  main()