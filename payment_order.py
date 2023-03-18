class Payment() :
    def __init__(self,  payment_id, total_amount, payment_status, order):
        self.payment_id = payment_id
        self.total_amount = total_amount
        self.payment_status = payment_status
        self.order = order




class PaymentStatus(enum) :
    PENDING, CONFIRMED, CANCELED = 0, 1, 2




class Order () :
    def __init__(self, user_id, total_quantity, order_time, bought_items, items_amount, delivery_fee, total_amount, tracking_nnumber):
        self.user_id = user_id
        self.total_quantity = total_quantity
        self.order_time = order_time
        self.bought_items = []  #list of product with choice
        self.items_amount = items_amount
        self.delivery_fee = delivery_fee
        self.total_amount = total_amount
        self.tracking_number = tracking_nnumber





class OrderHistory () :
    def __init__(self, order_history) :
        self.order_history = []  #order
