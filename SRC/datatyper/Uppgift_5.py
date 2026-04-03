import os
import subprocess

def clear_console():
    cmd = "cls" if os.name == "nt" else "clear"
    subprocess.call(cmd, shell=True)

clear_console()

## ---------------------------------------------------

#1 Skapa en ny lista resultat som innehåller kvadraten (talet upphöjt till 2) av alla heltal från 1 till 10 (båda inkluderade).

kvadrat_tal = [x ** 2 for x in range(1, 11)]

print (kvadrat_tal, '\n')

# 2. Skapa en annan lista namn_som_startar_med_s baserat på listan 
namn = ["Sara","Olle", "Stina", "Adam", "Simon"] 

print ('Origin: ', namn)


namn_som_startar_med_s =[] 

for user in namn:
    #print(user[0].upper())

    if user[0] == "S":
        #print ('= ',user)
        namn_som_startar_med_s.append(user)

print ('\n')
print (namn_som_startar_med_s,'\n')

#for user in namn:
 #  #print(user[0].upper())

  #  if user[0] != "S":
   #     print ('!= ',user)
    







# Den nya listan ska endast innehålla namn som börjar med bokstaven 'S' (case-sensitivt)

