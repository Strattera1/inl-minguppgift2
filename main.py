from ast import Break
from datetime import datetime
from itertools import product
from time import strftime
from Recepit import Recepit,Recepit_row
from product import Product

all_products = []
with open ("products.txt") as file:
    for line in file:
        parts =  line.split(";")
        product = Product(parts[1], float(parts [2]), parts[0])
        all_products.append(product)

print (all_products[0].Get_Name())

def Huvud_meny():
    print ("1. Ny kund")
    print ("2. Avsluta")
    selection = int(input(":"))
    return selection

def Nytt_kvitto(all_products):
    kvitto = Recepit()
    kvitto.Add("Bannaner",3,4.50)
    kvitto.Add("Kaffe",4,12.50)
    

    while True:
        print("KASSA")
        datum = datetime.now()
        nu = datum.strftime("%Y:%m:%d %H:%M:%S")
        print(f"KVITTO {nu}")
        print ("kommandon")
        print ("<productid> <antal>")
        print ("PAY")
        action = input ("Kommando: ")
        if action == "PAY":
            break
        elif action == "300":
            for prod in all_products:
                if prod.get_product_id() == "300":
                    print(prod.Get_Name())
        elif action == "400":
            for prod in all_products:
                if prod.get_product_id() == "400":
                    print(prod.Get_Name())
        elif action == "100":
            for prod in all_products:
                if prod.get_product_id() == "100":
                    print(prod.Get_Name())
          
while True:
    sel = Huvud_meny()
    if sel == 1:
        Nytt_kvitto(all_products)
    elif sel == 2:
       break
