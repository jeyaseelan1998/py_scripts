class Product:
    # Class attribute
    rupee_sign = '\u20B9'
    def __init__(self, name, price, deal_price, rating):
        # Instance attribute
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.saving = price - deal_price
        self.rating = rating
    
    def get_deal_price(self):
        return self.deal_price
    
    # Instance method
    def display_product_details(self):
        print("Name: {}".format(self.name))
        print("Price: {}{}".format(Product.rupee_sign,self.price))
        print("Deal Price: {}{}".format(Product.rupee_sign, self.deal_price))
        print("You will save: {}{}".format(Product.rupee_sign, self.saving))
        print("Rating: {} / 5".format(self.rating))

class ElectronicItem(Product):
    # Method overriding
    def __init__(self, name, price, deal_price, rating, warranty_in_months):
        super().__init__(name, price, deal_price, rating)
        self.warranty_in_months = warranty_in_months

    # Method overriding
    def display_product_details(self):
        super().display_product_details()
        print("Warranty: {} months".format(self.warranty_in_months))

class Laptop(ElectronicItem):
    # Method overriding
    def __init__(self, name, price, deal_price, rating, warranty_in_months, os, ram, rom, processor, display):
        super().__init__(name, price, deal_price, rating, warranty_in_months)
        self.os = os
        self.ram = ram
        self.rom = rom
        self.processor = processor
        self.display = display
    
    # Method overriding
    def display_product_details(self):
        super().display_product_details()
        print("OS: {}".format(self.os))
        print("RAM: {}".format(self.ram))
        print("ROM: {}".format(self.rom))
        print("Processor: {}".format(self.processor))
        print("Display: {}".format(self.display))

class GroceryItem(Product):
    # Method overriding
    def __init__(self, name, price, deal_price, rating, net_qty, mfg_date, expiry_date):
        super().__init__(name, price, deal_price, rating)
        self.net_qty = net_qty
        self.expiry_date = expiry_date
        self.mfg_date = mfg_date

    # Method overriding
    def display_product_details(self):
        super().display_product_details()
        print("Net weight: {}".format(self.net_qty))
        print("MFG date: {}".format(self.mfg_date))
        print("Expiry date:-{}".format(self.expiry_date))

# Composite
class Order:
    # Class attribute
    delivery_charges = {'prime_delivery': 0, 'normal_delivery': 45}
    def __init__(self, delivery_type, delivery_address):
        self.cart_items = []    # list of (product, qty)
        self.delivery_type = delivery_type
        self.delivery_address = delivery_address

    def add_item(self, product, qty):
        item = (product, qty)
        self.cart_items.append(item)

    def get_cart_item_details(self):
        print('Delivery Type: {}'.format(self.delivery_type))
        print('Delivery Address: {}'.format(self.delivery_address))
        print('---------------------------------')
        for product, qty in self.cart_items:
            product.display_product_details()
            print('Quantity: {}\n'.format(qty))
        print('---------------------------------')
        total_bill = self.get_total_bill()
        print('Total Bill amount: {}'.format(total_bill))
        
    def get_total_bill(self):
        total_bill = 0
        for product, qty in self.cart_items:
            total_bill += product.get_deal_price() * qty

        delivery_chardges = Order.delivery_charges[self.delivery_type]
        total_bill += delivery_chardges
        return total_bill

# Objects
sony_tv = ElectronicItem("Sony TV", 14000, 13000, 4.7, 36)
lenovo_laptop = Laptop("Lenovo B490", 15000, 12000, 4.1, 24, 'Windows 11 pro','16GB', '1TB', 'i7 10th Gen', '2k LCD IPS')
dell_laptop = Laptop("Dell Latitude 5570", 25000, 20000, 4.1, 24, 'Linux Ubuntu 20.2', '16GB', '250GB', 'i7 8th Gen', '2k LCD IPS')
milk = GroceryItem("Hutsan Milk", 20, 18, 4.5, '250ml', '28/04/2023', '30/04/2023')
weat_flour = GroceryItem("Ashiwath Weat Flour", 35, 32, 4.5, '500g', '28/04/2023', '30/10/2023')

my_order = Order('prime_delivery', 'Jeyaseelan R, Coiembatore - 635 281, contact - 93892 89182')

# Purchasing
my_order.add_item(dell_laptop, 1)
my_order.add_item(weat_flour, 4)
my_order.add_item(milk, 3)

my_order.get_cart_item_details()