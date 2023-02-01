

class Product:
	def __init__(self, name : str, price : int):
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

class User:

	numbers_of_user = 0

	def __init__(self, id : str, name : str , phone : str):
		self.id = id
		self.name = name
		self.phone = phone
		User.numbers_of_user +=1

	#---------getter-----------
	
	def id_getter(self):
		return (self.id)
	
	def name_getter(self):
		return (self.name)

	def phone_getter(self):
		return (self.phone)

	#--------Setter------------

	def id_setter(self,new_id):
		self.id = new_id
	
	def name_setter(self,new_name):
		self.name = new_name

	def phone_setter(self,new_phone):
		self.phone = new_phone

	
class Payment:
	def __init__ (self, payment_id: str, status : str, user_bank : str, payment_time : str):
		self.status = "Pending" #Pending / Confirm / Cancel
		self.payment_id = payment_id
		self.user_bank = user_bank
		self.payment_time = payment_time

	
class Cart:

	def __init__ (self):
		self.quanity = 0
		self.total = 0
		self.items = {}		#{Product obj : Quanity}
	
	def addToCart(self,new_item : Product, numbers_of_item : int): 
		self.quanity += numbers_of_item
		self.total += new_item.price_getter()							# Maybe  try type cast new_item as Product  
		self.items.update({new_item.name: numbers_of_item})	

	def	displayCart(self);
		print(self.items)
		print(self.quanity)
		print(self.total)

		
class Promotion:
	pass


if __name__ == "__main__":
	lips = Product("Lips",2500)
	eye_liner = Product("Eye_Liner",3000)

	cart = Cart()

	cart.addToCart(lips,1)
	cart.addToCart(eye_liner,2)
	cart.displayCart()

