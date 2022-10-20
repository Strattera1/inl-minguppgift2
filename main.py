from ast import Break
from datetime import datetime
from itertools import product
from subprocess import call
from time import strftime
from Recepit import Recepit,Recepit_row
from product import Product

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
    kvitto.Add("Bannaner",3,4.50)
    kvitto.Add("Kaffe",4,12.50)
    

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
            break
        for prod in all_products:
            if prod.get_product_id() == words[0]:
                item = prod.Get_Price() * antal(words[1])
                print(prod.Get_Name(), antal(words[1]), "*", prod.Get_Price(), "=", item)
                kvitto.append(Recepit)

while True:
    sel = Huvud_meny()
    if sel == 1:
        Nytt_kvitto(all_products)
    elif sel == 2:
       break
