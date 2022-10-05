from ast import Add
from datetime import datetime


class Recepit_row:
    def __init__(self):
        self._ProductName = ""
        self._Count = 0
        self._PerPrice = 0
    def Get_total(self):
        return self.__Count * self.__Price

class Recepit:
    def __init__(self):
        self._Datum = datetime.now()
        self.__Recepit_row = []
    def Get_total(self):
        sum = 0
        for row in self.__Recepit_row:
            sum = sum + row.Get_total()
        return sum
    def Add(self,ProductName:str,count:int,PerPrice:float):
        Recepit_row = Recepit_row()
        self.__Recepit_row.append(Recepit_row)