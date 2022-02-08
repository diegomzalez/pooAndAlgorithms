# def funcion_decoradora(funcion):
# 	def wrapper():
# 		print("Este es el último mensaje...")
# 		funcion()
# 		print("Este es el primer mensaje ;)")
# 	return wrapper

# def zumbido():
# 	print("Buzzzzzz")

# zumbido = funcion_decoradora(zumbido)

class Millas:
	def __init__(self):
		self._distancia = 0

	# Función para obtener el valor de _distancia
	# Usando el decorador property
	@property
	def obtener_distancia(self):
		print("Llamada al método getter")
		return self._distancia

	# Función para definir el valor de _distancia
	@obtener_distancia.setter
	def definir_distancia(self, valor):
		if valor < 0:
			raise ValueError("No es posible convertir distancias menores a 0.")
		print("Llamada al método setter")
		self._distancia = valor