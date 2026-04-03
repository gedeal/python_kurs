import os
import subprocess

def clear_console():
    cmd = "cls" if os.name == "nt" else "clear"
    subprocess.call(cmd, shell=True)

clear_console()

## ---------------------------------------------------

#1. Skapa listan 
siffror = [50, 10, 50, 5, 20, 10, 99]
#2. Ta bort den första förekomsten av värdet 10 .

for i in range(len(siffror)):
    if siffror[i] == 10:
        siffror[i] = 1000
        break

print(siffror)


#3. Ta bort det sista elementet i listan och spara det borttagna värdet i en variabel. Skriv utdet borttagna värdet.
b= siffror.pop()

print (siffror)
print (b)



#4. Sortera den kvarvarande listan i fallande ordning.

ny_list = sorted(siffror)

print (ny_list)

#5. Skriv ut den sorterade listan.