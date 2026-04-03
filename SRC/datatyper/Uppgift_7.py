import os
import subprocess

def clear_console():
    cmd = "cls" if os.name == "nt" else "clear"
    subprocess.call(cmd, shell=True)

clear_console()

## ---------------------------------------------------

#1. Skapa en tupel 
t = ("data", [1, 2, 3], 100)
print ('Origin: ',t)


#2. Ändra innehållet i listan inuti tupeln genom att lägga till värdet 4 till listan.

ny_t = t + (4,)
print ('Ny T  : ',ny_t)
x, y, z, a= ny_t
print ('X = ',x)
print ('Y = ',y)
print ('Z = ',z)
print ('A = ',a)

#3. Skriv ut tupeln och förklara varför du kunde ändra listans innehåll men inte byta ut listan´mot ett nytt värde.
print('ny_t  : ', ny_t)

'''
När en tupel väl har skapats man kan inte ändra dess värden. Tupler är oföränderliga.
Men det finns en lösning. Man kan konvertera tupeln till en lista, ändra listan och konvertera listan tillbaka till en tupel.

'''
x, y, z, a = ny_t

test_t = (z,a,y,x)
print ('test_t: ', test_t, ' <- ',type(test_t))