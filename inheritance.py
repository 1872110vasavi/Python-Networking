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

class groceryitems():
    def __init__(self,name,price,dealprice,rating,packagedate,expirydate):
        super().__init__(name,price,dealprice,rating)
        self.packagedate=packagedate
        self.expirydate=expirydate
    def expirydate(self):
        super().displayproductdetails()
        print("expirydate {}".format(self.expirydate))
        print("packagedate {}".format(self.packagedate))
myProduct=product("icecream","80","40","5")
myProduct.displayproductdetails()
warr=electronicitems("1 year")
warr.getwarranty()
grocery=groceryitems("maggie",30,28,10,"15/10/2022","16/11/2022")
grocery.expirydate()

















