from ast import Add
from datetime import datetime
from fileinput import filename
from gc import get_count
from time import strftime
import os


class Recepit_row:
    def __init__(self, name,count,price):
        self.__ProductName = name
        self.__Count = count
        self.__PerPrice = price
    def Get_Name(self):
        return self.__ProductName

    def Get_Count(self):
        return self.__Count
    def Get_Price(self):
        return self.__PerPrice
    def Get_total(self):
        return self.__Count * self.__PerPrice



class Recepit:
    def GetReceiptRows(self):
        return self.__Recepit_row
    def __init__(self):
        self.__Datum = datetime.now()
        self.__Recepit_row = []
    def Get_total(self):
        sum = 0
        for row in self.__Recepit_row:
            sum = sum + row.Get_total()
        return sum
    def Add(self,ProductName:str,count:int,PerPrice:float):
        r = Recepit_row(ProductName,count,PerPrice)
        self.__Recepit_row.append(r)
    def Save_To_File(self):
        y = Recepit_row
        file = datetime.now()
        with open (file.strftime("%Y,%m,%d") +".txt","a") as file:
            file.write(f"{y}\n")
