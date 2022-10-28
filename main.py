from ast import Break
from datetime import date, datetime
from gc import get_count
from io import TextIOWrapper
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
        act = [action,antal]
        print("KASSA")
        datum = datetime.now()
        nu = datum.strftime("%Y:%m:%d %H:%M:%S")
        print(f"KVITTO {nu}")
        print ("kommandon")
        print ("<productid> <antal>")
        print ("PAY")
        act=[action for action in input ("Kommando: ").split()]
        antal = float

        if act[0] == "PAY":
            save_to_file = "RECEIPT_" +strftime("%Y%m%d") + ".txt"
            with open(str(save_to_file), "a") as utdata:
                utdata.write(strftime("%Y:%m:%d: %H:%M:%S \n"))
                for x in kvitto.GetReceiptRows():
                    utdata.write(f"{x.Get_Name()} {x.Get_Count()} * {x.Get_Price()} = {x.Get_total()}\n")
                utdata.write(f"Total: {kvitto.Get_total()}\n\n")     
            break
        for prod in all_products:
            if prod.get_product_id() == act[0]:
                kvitto.Add(prod.Get_Name(),int(act[1]),prod.Get_Price())

        for x in kvitto.GetReceiptRows():
            print(x.Get_Name(), x.Get_Count(), "*", x.Get_Price(), "=", x.Get_total())
       
        print ("Totalt: ",kvitto.Get_total())


while True:
    sel = Huvud_meny()
    if sel == 1:
        Nytt_kvitto(all_products)
    elif sel == 2:
       break
    else:
        print ("välj mellan 1-2.")
