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
	

class ProductCatalog():
	def __init__ (self, last_update, list_of_product):
		self.last_update = last_update
		self.list_of_product = list_of_product
	