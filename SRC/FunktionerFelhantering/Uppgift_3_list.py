import os
import subprocess
from dbm import error


def clear_console() -> None:
    cmd = "cls" if os.name == "nt" else "clear"
    subprocess.run(cmd, shell=True)



clear_console()


## ---------------------------------------------------
# Menyprogram med funktioner
#numbers = []


def summa_lista(lista):
    ans = sum(lista)
    #print('    Sum:', ans)
    print('\033[31m' + f'  Sum: {ans} ' + '\033[0m')


def medelvarde(lista):
    adding=0
    for item in lista:
        adding = adding + item
    print('\033[31m' + f'  Midle value : {adding/2} ' + '\033[0m')


def max_varde(lista):
    lista.sort(reverse=True)
    #print(f'Sorted lista : {lista}')
    print('\033[31m' + f'  Max value: {lista[0]} ' + '\033[0m')



def read_int_sequence(prompt="Enter numbers separated by spaces: "):
    s = input(prompt).strip()
    if not s:
        raise ValueError("No input provided")
    parts = s.split()
    nums = []
    for p in parts:
        try:
            nums.append(int(p))
        except ValueError:
            raise ValueError(f"Non-numeric input: {p!r}")
    return nums


## ---------------------------------------------------------------------
clear_console()   ## Does not work :-(  !!

while True:
    # Example usage
    try:
        seq_numbers = read_int_sequence()
        print("Got integers:", seq_numbers)
        break
    except ValueError as e:
        print("Error:", e)




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
            summa_lista(seq_numbers)
        case 'y':
            medelvarde(seq_numbers)
        case 'z':
            max_varde(seq_numbers)
        case '*':
            print ('  ByBy :-)  ')
            break
        case _:
            print ('Not a valid option')
