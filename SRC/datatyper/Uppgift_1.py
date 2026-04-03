
import os
import subprocess

def clear_console():
    cmd = "cls" if os.name == "nt" else "clear"
    subprocess.call(cmd, shell=True)

clear_console()

## ---------------------------------------------------

name= '10'
print ('Name: ', name, type(name)) 

#1. Skapar en variabel a med heltalet 10 .
a= 10
print ('A: ', a, type(a)) 
# 2. Skapar en variabel b med flyttalet 3.5 .
b = 3.5
print ('B: ', b, type(b)) 
# 3. Beräknar och skriver ut a dividerat med b med vanlig division ( / ). Vilken datatyp får resultatet?
c= a / b
print ('C: ', c, type(c)) 
# 4. Beräknar och skriver ut a dividerat med b med heltalsdivision ( // ). Vilken datatyp får resultatet?
d = a // b
print ('D: ', d, type(d)) 


#5. Skapar en variabel jämförelse som är True om a är större än 10, annars False . Skriv ut jämförelse .
test = True
while (test):
    input_a = int(input ('\n enter a number:  '))
    #print(type(input_a)) 
    
      
    #print (': ',input_a)

    if input_a > 10: 
        print (input_a ,' > 10  - Good ;-) ')
        print('Bye !')

        test = False
        #break
    elif input_a == 10:
        print (input_a ,' = 10 - Try again :-(')

    else :
        print (input_a ,' < 10  - Try again :-(')
 
