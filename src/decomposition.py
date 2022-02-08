class Car:

  def __init__(self, model: str, brand: str, color: str) -> None:

      self.model = model
      self.brand = brand
      self.color = color
      self._state = 'resting'
      self._motor = Motor(cylinders=4)

  def acelerate(self, type='slowly'):

    if type == 'fast':
      self._motor.inject_gasoline(10)
    else:
      self._motor.inject_gasoline(3)

    self._state('in moving')

class Motor:

  def __init__(self, cylinders: int, type='gasoline') -> None:

      self.cylinders = cylinders
      self.type = type
      self_temperature = 0

  def inject_gasoline(self, amount: int):
    self.amount = amount

class Seats:

  def __init__(self, brand: str, amount: int, cloth: str, color: str, forward=50, back=50, up=50, down= 50) -> None:
      self.brand = brand
      self.amount = amount
      self.cloth = cloth
      self.color: color
      self.forward = forward
      self.back = back
      self.up = up
      self.down = down


  def adjust_seat(self, amount_up=0, amount_down=0, amount_forward=0,amount_back=0) -> None:
    self.forward += amount_forward
    self.back += amount_back
    self.up += amount_up
    self.down += amount_down

ferrari = Seats("ferrari", 4, "love", "black")
