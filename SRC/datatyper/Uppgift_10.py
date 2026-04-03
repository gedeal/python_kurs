import os
import subprocess

def clear_console():
    cmd = "cls" if os.name == "nt" else "clear"
    subprocess.call(cmd, shell=True)

clear_console()

## ---------------------------------------------------

#1.Skapa en lista min_lista = [1, 2] och försök använda den som nyckel i en ordbok d = {min_lista: "fel"} . Förklara felet.

min_lista = [1, 2]

#d = {min_lista: "fel"}

'''
Dictionary (Ordbok) måsta vara i par (nyckel_värde)
ex: "namn": "Sara",
min_lista har 2 värde

'''
da = {min_lista[0]: "fel"}
db = {min_lista[1]: "OK"}

print (da)
print (db)



#2. Skapa en tupel min_tupel = (1, 2) och använd den som nyckel i en ordbok d2 = {min_tupel: "rätt"} . Förklara varför detta fungerar, men listan inte.

min_tupel = (1, 2)

d2 = {min_tupel: "rätt"}

print (d2)
'''
Tupeln används som en nyckel
'''