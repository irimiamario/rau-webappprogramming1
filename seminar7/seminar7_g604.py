class Product:
    def __init__(self, name=None, description=None, price=None):
        self.name = name
        self.description = description
        self.price = price

    def edit(self, name=None, description=None, price=None):
        if name is not None:
            self.name = name
        if description is not None and description.strip() != "":
            self.description = description
        if price is not None and price > 0:
            self.price = price 

    def edit_name(self, name):
        if name.strip() != "":
            self.name = name 
        else:
            raise Exception("Invalid name")

    def edit_description(self, description):
        if description.strip() != "":
            self.description = description
        else:
            raise Exception("Invalid description")

    def edit_price(self, price):
        if price > 0:
            self.price = price
        else:
            raise Exception("Invalid price")

    def display(self):
        return f"Product name: {self.name}; Product description: {self.description}; Product price: {self.price}"


class ProductList:
    def __init__(self, products=None):
        if products is None:
            self.products = []
        else:
            self.products = products

    def add_product(self, product):
        self.products.append(product)

    def display(self):
        if len(self.products) == 0:
            print("No products available.")
            return 

        for product in self.products:
            print(product.display())

    def delete_product_by_name(self, product_name):
        product_to_delete = None 
        for product in self.products:
            if product.name == product_name:
                product_to_delete = product
                break 
        self.products.remove(product_to_delete) 

    def delete_all(self):
        self.products = [] 


if __name__ == "__main__":
    product1 = Product("product1", "prod desc 1", 10)
    product2 = Product("product2", "prod desc 2", 23.12)
    product3 = Product("product3", "prod desc 3", 66.10)

    product1.edit(price=12.34)

    product_list = ProductList()
    product_list.add_product(product1)
    product_list.add_product(product2)
    product_list.add_product(product3)

    print("Available products:")
    product_list.display()

    print("..Deleting product1")
    product_list.delete_product_by_name("product1")
    product_list.display()
    
    print("..Deleting all products")
    product_list.delete_all()
    product_list.display()