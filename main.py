from ast import Break
from datetime import date, datetime
from gc import get_count
from itertools import product
from time import strftime
from Recepit import Recepit,Recepit_row
from product import Product
import os
all_products = []
with open ("products.txt") as file:
    for line in file:
        parts =  line.split(";")
        product = Product(parts[1], float(parts [2]), parts[0])
        all_products.append(product)

def Huvud_meny():
    print ("1. Ny kund")
    print ("2. Avsluta")
    selection = int(input(":"))
    return selection


def Nytt_kvitto(all_products):
    kvitto = Recepit()



    while True:
        action = 0
        antal = 0
        words = [action,antal]
        print("KASSA")
        datum = datetime.now()
        nu = datum.strftime("%Y:%m:%d %H:%M:%S")
        print(f"KVITTO {nu}")
        print ("kommandon")
        print ("<productid> <antal>")
        print ("PAY")
        words=[action for action in input ("Kommando: ").split()]
        antal = float

        if words[0] == "PAY":
            lolz = "RECEIPT_" +strftime("%Y,%m,%d") + ".txt"
            for x in kvitto.GetReceiptRows():  
                with open(str(lolz), "a") as utdata:
                    utdata.write(strftime("%Y:%m:%d: %H:%M:%S \n"))
                    utdata.write(f"{x.Get_Name()} {x.Get_Count()} * {x.Get_Price()} = {x.Get_total()}\n")
                    utdata.write(f"'Totalt:' {kvitto.Get_total()}")
            break
        for prod in all_products:
            if prod.get_product_id() == words[0]:

                kvitto.Add(prod.Get_Name(),int(words[1]),prod.Get_Price())

        for x in kvitto.GetReceiptRows():
            print(x.Get_Name(), x.Get_Count(), "*", x.Get_Price(), "=", x.Get_total())
       
               


        print ("Totalt: ",kvitto.Get_total())





while True:
    sel = Huvud_meny()
    if sel == 1:
        Nytt_kvitto(all_products)
    elif sel == 2:
       break
