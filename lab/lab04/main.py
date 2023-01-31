

class Product:
	def __init__(self, name, price):
		self.name = name
		self.price = price

	def name_setter(self, name):
		self.name = name

	def name_getter(self):
		return self.name

	def price_setter(self, price):
		self.price = price

	def price_getter(self):
		return self.price

	def displayProduct(self):
		print(f"Product: {self.name},Price:{self.price}")

class Package(Product):
	Product.__init__()


if __name__ == "__main__":
	p1 = Product("Lips",2500)

	p1.displayProduct()