

class Product:
	def __init__(self, name, price):
		self.name = name
		self.price = price

	def displayProduct(self):
		print(f"Product: {self.name},Price:{self.price}")
		return (self.name,self.price)



if __name__ == "__main__":
	p1 = Product("Lips",2500)

	ret1,ret2 = p1.displayProduct()
	print(ret1)
	print(ret2)