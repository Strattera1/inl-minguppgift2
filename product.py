
class Product:
    def __init__(self, name:str, price:float,productid:str):
        self.__Name = name
        self.__Price = price
        self.__ProductId = productid
        self.__PriceType = ""
    def get_product_id(self):
        return self.__ProductId
    def Get_Name(self):
        return self.__Name
    def Get_Price(self):
        return self.__Price
    def Get_PriceType(self):
        return self.Get_PriceType