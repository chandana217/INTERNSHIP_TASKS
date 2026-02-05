
# Parent class
class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    def display_product(self):
        print("Product Name:", self.product_name)
        print("Price:", self.price)


# Child class
class ElectronicProduct(Product):
    def __init__(self, product_name, price, brand, warranty):
        Product.__init__(self, product_name, price)
        self.brand = brand
        self.warranty = warranty

    def display_electronic_product(self):
        print("Brand:", self.brand)
        print("Warranty:", self.warranty)


# Grandchild class
class MobilePhone(ElectronicProduct):
    def __init__(self, product_name, price, brand, warranty, ram, storage):
        ElectronicProduct.__init__(self, product_name, price, brand, warranty)
        self.ram = ram
        self.storage = storage

    def display_mobile_details(self):
        print("RAM:", self.ram)
        print("Storage:", self.storage)


# Creating object of MobilePhone
mobile = MobilePhone(
    "Smartphone",
    20000,
    "Redmi",
    "2 Year",
    "6 GB",
    "128 GB"
)

# Displaying all details
mobile.display_product()
mobile.display_electronic_product()
mobile.display_mobile_details()
