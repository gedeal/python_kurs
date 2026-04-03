import os
import subprocess

def clear_console():
    cmd = "cls" if os.name == "nt" else "clear"
    subprocess.call(cmd, shell=True)

clear_console()

## ---------------------------------------------------

poäng = {"Anna": 85, "Bertil": 92, "Cecilia": 78}

#1.Loopa igenom ordboken och skriv ut endast nycklarna (namnen).

for nyckel in poäng:
    varde = poäng[nyckel]
    #print(f"{nyckel}: {varde}")
    print(f"{nyckel}")
print ('------------------')


#2. Loopa igenom ordboken och skriv ut endast värdena (poängen).

for nyckel in poäng:
    varde = poäng[nyckel]
    #print(f"{nyckel}: {varde}")
    print(f"{varde}")
print ('------------------')

#3. Loopa igenom ordboken och skriv ut både nyckeln och värdet i formatet: "Anna fick 85 poäng."

for nyckel in poäng:
    varde = poäng[nyckel]
    print(f"{nyckel} fick {varde} poäng.")