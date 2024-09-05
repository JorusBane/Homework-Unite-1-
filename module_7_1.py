from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"
class Shop():
    __file_name = 'products.txt'
    def get_products(self):
        file = open(self.__file_name, 'r')
        helper_att = file.read()
        file.close()
        return helper_att
    def add(self, *products):
        product1 = self.get_products()
        file = open(self.__file_name, 'a')
        for i in products:
            product2 = str(i)
            if product2 not in product1:
                file.write(product2 + "\n")
            else:
                print(f"Продукт {i} уже есть в магазине .")
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())


