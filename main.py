from ast import Break
from itertools import product
from Recepit import Recepit,Recepit_row
from product import Product

all_products = []
with open ("products.txt") as file:
    for line in file:
        parts =  line.split(";")
        product = Product(parts[1], float (parts [2]), parts[0])
        all_products.append(product)

print (all_products[0].Get_Name())

def Huvud_meny():
    print ("1. Ny kund")
    print ("2. Avsluta")
    selection = int(input(":"))
    return selection

def Nytt_kvitto(all_products):
    kvitto = Recepit()
    kvitto.Add("Bannaner",3,12.50)
    kvitto.Add("Äpplen",4,10.50)

    while True:
        print("KASSA")
        datum = "2022-10-05-13-34-5"
        print("KVITTO{datum}")
        print ("kommandon")
        print ("<productid> <antal>")
        print ("PAY")
        action = input ("Kommando: ")
        if action == "PAY":
            break

while True:
    sel = Huvud_meny()
    if sel == 2:
        Break
    elif sel == 1:
        Nytt_kvitto(all_products)