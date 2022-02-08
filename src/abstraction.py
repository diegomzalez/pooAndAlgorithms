class Washer:

  def __init__(self) -> None:
      pass

  def wash(self, temperature="hot"):
    self._fill_water_tank(temperature)
    self._add_soup()
    self._wash()
    self._centrifuge()

  def _fill_water_tank(self, temperature: str):
    print(f"Filling water tank with water {temperature}")

  def _add_soup(self):
    print("Adding soap")

  def _wash(self):
    print("Washing clothes")

  def _centrifuge(self):
    print("centrifuging clothes")

def main():
  washer = Washer()
  washer.wash()


if __name__ == "__main__":
  main()