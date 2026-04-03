import os
import subprocess

def clear_console():
    cmd = "cls" if os.name == "nt" else "clear"
    subprocess.call(cmd, shell=True)

clear_console()

## ---------------------------------------------------
# Menyprogram med funktioner

numbers = []


def summa_lista(lista):
    ans = sum(lista)
    print('Sum:', ans)

def medelvarde(lista):
    adding=0
    for item in lista:
        adding = adding + item
    print(f'medelvärde: {adding/2}')


def max_varde(lista):
    lista.sort(reverse=True)
    print(f'Sorted lista : {lista}')
    print(f'max_varde: {lista[0]}')


print('Enter numbers (to finish enter: * )')
while True:
    nr = input('   Enter a number : ')
    if nr == '*':
        #print('EXIT')
        break
    else:
        try:
            int_nr = int(nr)
            numbers.append(int_nr)

        except ValueError as e:
            print("  *****>  ERROR : ", repr(e))
            #exit(0)

    #print('Test Array ', numbers)

lennumbers = len(numbers)
print('\n ---------------------------')
#print('Array length : ',lennumbers)

print('Entered Array ', numbers)

"""
TBD 
Anropa rätt funktion beroende på val
Fel input (text istället för tal)
Tom lista
Fel menyval
"""


summa_lista(numbers)

medelvarde(numbers)

max_varde(numbers)