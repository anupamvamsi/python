class Product:
    def __init__(self, product_id, product_name, product_type, product_price):
        self.product_id = product_id
        self.product_name = product_name
        self.product_type = product_type
        self.product_price = product_price

    def apply_discount(self, discount):
        self.product_price -= discount / 100.0 * (self.product_price)
        
        return self.product_price

prod1 = Product(1, 'abc', 'tps', 100)
print(prod1)
print(prod1.apply_discount(10))