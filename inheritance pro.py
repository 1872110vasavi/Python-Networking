#inheritance
class product():
    def __init__(self,name,price,dealprice,rating):
        self.name=name
        self.price=price
        self.dealprice=dealprice
        self.rating=rating
    def displayproductdetails(self):
        print("name={}".format(self.name))
        print("price={}".format(self.price))
        print("dealprice={}".format(self.dealprice))
        print("rating={}".format(self.rating))
class electronicitems():
    def __init__(self,warranty):
        self.warranty = warranty
    def getwarranty(self):
        print("warranty= {}".format(self.warranty))

class order():
    def __init__(self,orderType,orderAddress):
        self.items= []
        self.orderType=orderType
        self.orderAddress=orderAddress

    def add_item(self,product,quantity):
        self.items.append(product,quantity)

    def display_order_details(self):
        for product,quantity in self.items:
            product.display_product_details()
            print("quantity:{}".format(quantity))
    def display_total_bill(self):
        total_bill=0
        for product,quantity in self.items:
            price=product.get_dealprice()*quantity
            total_bill+=price
            print("totalbill:{}".format(total_bill))
class groceryitems():
    def __init__(self,name,price,dealprice,rating,packagedate,expirydate):
        product.__init__(self,name,price,dealprice,rating)
        self.packagedate=packagedate
        self.expirydate=expirydate
    def get_expirydate(self):
        print("expirydate={}".format(self.expirydate))
        print("packagedate={}".format(self.packagedate))
myProduct=product("icecream",80,40,5)
myProduct.displayproductdetails()
warr=electronicitems("1 year")
warr.getwarranty()
grocery=groceryitems("maggie",30,28,10,"15/10/2022","16/11/2022")
grocery.get_expirydate()


















