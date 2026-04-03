import os
import subprocess

def clear_console():
    cmd = "cls" if os.name == "nt" else "clear"
    subprocess.call(cmd, shell=True)

clear_console()

## ---------------------------------------------------

#1. Skapa tupeln 
koordinater = (15, 30)
print ('koordinater = ',koordinater)
print(type(koordinater)) 


#2. Försök (genom att kommentera ut koden som ger fel) att ändra värdet 15 till 100 .Förklara varför det misslyckas.

#koordinater[0] = 99
##    koordinater[0] = 99
##    ~~~~~~~~~~~^^^
##TypeError: 'tuple' object does not support item assignment

#3. Skapa en ny tupel ny_koordinater genom att lägga till värdet 45 till koordinater med hjälp av konkatenering ( + ).

ny_koordinater = koordinater + (45,)

print ('ny_koordinater = ',ny_koordinater)

#4. Använd tupel-uppackning för att tilldela de tre värdena i ny_koordinater till variablerna x , y och z . Skriv ut x .

x, y, z = ny_koordinater

print ('X = ',x)
print ('Z = ',z)