import os
import subprocess

def clear_console():
    cmd = "cls" if os.name == "nt" else "clear"
    subprocess.call(cmd, shell=True)

clear_console()

## ---------------------------------------------------


#Skapa en sträng variabel text med värdet " python är roligt! " .

s = 'Öpython är roligt!Å'

#2. Ta bort blankstegen i början och slutet, gör första bokstaven stor, och skriv ut den nya strängen.
#print(textvar[0]) # Skriver ut 'P' (första tecknet)
#print(textvar[-1]) # Skriver ut 'n' (sista tecknet)

#s = "" + textvar[1:]
s= s.rstrip(s[1])
print('1:', s)

s = "P"+ s[2:]
#print(s) # Skriver ut 'Python..'
print('2:', s)

b= s.rstrip(s[-1])

print('\n3:', b) # new string


#3. Skapa två variabler: nummer_strang_1 med värdet "15" och nummer_strang_2 med värdet "20" .

#4. Konvertera strängarna till heltal och skriv ut summan av dem.


