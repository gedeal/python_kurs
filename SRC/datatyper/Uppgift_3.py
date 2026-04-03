import os
import subprocess

def clear_console():
    cmd = "cls" if os.name == "nt" else "clear"
    subprocess.call(cmd, shell=True)

clear_console()

## ---------------------------------------------------


# 1. Skapa listan 
veckodagar = ["måndag", "tisdag", "onsdag", "torsdag","fredag"] 

# 2. Lägg till helgen i slutet av listan med en enda metod.

helgen =  ["lördag" , "söndag"]

vecka = veckodagar + helgen

print (vecka)


#3. Anta att du gjorde fel och vill byta ut "torsdag" mot "LÄSDAG". Ändra elementet direkt via dess index.

### print(vecka.replace("torsdag", "LÄSDAG")) # " Tjena Världen! Tjena! "  # does not work !!

vecka = [vecka if vecka != "torsdag" else "LÄSDAG " for vecka in vecka]

print (vecka)
vecka[3] = 'Gerson '

# 4. Skriv ut den slutgiltiga listan.
print (vecka)
