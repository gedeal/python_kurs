import os
import subprocess

def clear_console():
    cmd = "cls" if os.name == "nt" else "clear"
    subprocess.call(cmd, shell=True)

clear_console()

## ---------------------------------------------------

#1. Skapa en ordbok produkt med nycklarna "id" , "namn" och "pris" och tilldela dem lämpliga värden.

produkt = {
    "id" : "123" , 
    "namn" : "Potatis" ,
    "pris" : "8.90" 
}

print (produkt)
print (produkt["pris"])

#2. Ändra värdet för "pris" till ett nytt, högre värde.

produkt["pris"] = 10.99

print (produkt)
print (produkt["pris"])

#3. Försök hämta värdet för nyckeln "lagerstatus" med metoden .get() . 
# Om nyckeln saknas ska den returnera standardvärdet "Finns ej i lager" . Skriv ut resultatet.

#print(produkt["lagerstatus"])   # KeyError: 'lagerstatus'
print(produkt.get("lagerstatus", "Finns ej i lager"))


#4. Lägg till ett nytt nyckel-värde-par: "kategori" med värdet "Elektronik" .

#5. Skriv ut hela ordboken.