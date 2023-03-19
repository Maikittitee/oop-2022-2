#Todo : Relation and Method

class Product():
	def __init__(self, product_id, serial_id, name, price, rating, small_detail, full_detail, detail_img, preview_img, stock):
		self.product_id = product_id
		self.serial_id = serial_id
		self.name = name
		self.price = price
		self.rating = rating
		self.small_detail = small_detail
		self.full_detail = full_detail
		self.detail_img = detail_img
		self.preview_img = preview_img 
		self.stock = stock
	def	request_product(self):
		pass
	
	def	select_type(self):
		pass

	def get_product_detail(self):
		pass

	def view_product(self):
		pass
	

class ProductCatalog():
	def __init__ (self, last_update, list_of_product):
		self.last_update = last_update
		self.list_of_product = list_of_product

	def get_each_product():
		pass

	def search_product_by_type(self, search_input):
		pass

	def search_product_by_name(self, search_input):
		pass	

class ProductWithChoice(Product):
	def __init__ (self, choice):
		self.choice = choice

class Promotion(ProductWithChoice):
	def __init__ (self, time_start, time_end, percent_discount):
		self.time_start = time_start
		self.time_end = time_end
		self.percent_discount = percent_discount

class DisplayProduct(Promotion):
	def __init__ (self, price_after_discount, feed_type):
		self.price_after_discount = price_after_discount
		self.feed_type = feed_type

class Favorite():
	def __init__ (self):
		pass

