import os
import subprocess


def clear_console() -> None:
    cmd = "cls" if os.name == "nt" else "clear"
    subprocess.run(cmd, shell=True)



clear_console()


## ---------------------------------------------------
# Menyprogram med funktioner
numbers = []


def summa_lista(lista):
    ans = sum(lista)
    print('    Sum:', ans)


def medelvarde(lista):
    adding=0
    for item in lista:
        adding = adding + item
    print(f'    Midle value: {adding/2}')


def max_varde(lista):
    lista.sort(reverse=True)
    #print(f'Sorted lista : {lista}')
    print(f'    Max value: {lista[0]}')



print('Enter numbers (to finish enter: * )')


def Control_entry(len):
    if len == 0:
        # Vi skapar ett ValueError med ett eget meddelande
        raise ValueError("Array can not be zero !")
    return len


while True:
    nr = input('   Enter a number : ')

    if nr == '*':
        try:
            Control_entry(len(numbers))
            break
        except ValueError as e:
            print(f"Validation error: {e}")

    else:
        try:   # Fel inmatning (text istället för heltal)
            int_nr = int(nr)
            numbers.append(int_nr)

        except ValueError as e:
            print("  *****>  ERROR : ", repr(e))
            #exit(0)


lennumbers = len(numbers)
print('\n---------------------------')
#print('Array length : ',lennumbers)
print('Array : ', numbers)
#print('---------------------------')

## ---------------------------------------------------------------------
clear_console()   ## Does not work :-(  !!


while True:
    print('---------------------------')
    print('   What you want to see ?\n---------------------------')
    print('      [ x ]   Sum of the list')
    print('      [ y ]   Midle value of the list')
    print('      [ z ]   Max value of the list')
    print('      [ * ]   Finish')
    expr = input(' => ')
    match expr:
        case 'x':
            summa_lista(numbers)
        case 'y':
            medelvarde(numbers)
        case 'z':
            max_varde(numbers)
        case '*':
            print ('  ByBy :-)  ')
            break
        case _:
            print ('Not a valid option')
