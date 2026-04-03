import os
import subprocess

def clear_console():
    cmd = "cls" if os.name == "nt" else "clear"
    subprocess.call(cmd, shell=True)

clear_console()

## ---------------------------------------------------

def add (a, b):
    add_ab = a+b
    print(f"{a}+{b}= {add_ab}")

def sub (a, b):
    sub_ab = a-b
    print(f"{a}-{b}= {sub_ab}")

def div(a, b):
    try:
        div_ab = a / b
        print(f"{a}/{b}= {div_ab}")
    except ZeroDivisionError as zde:
        print(f"ZeroDivisionError: {zde} =>  {a}/{b}")
        exit(0)

def getnumber():
    try:
        nr_1 = int(input(' Give 1st number : '))
        #print(f"Result is {nr_1}")
    except ValueError as e:
        #print("Type of Exception:", type(e))
        #print("Message:", e)
        #print("str():", str(e))
        print("ERROR : ", repr(e))
        exit(0)

    try:
        nr_2 = int(input(' Give 2nd number : '))
        #print(f"Result is {nr_2}")
    except ValueError as e:
        print("ERROR : ", repr(e))
        exit(0)

    return nr_1, nr_2

while True:
    val = input('Choose operation [ + - / ] :  ')

    if val == '+':
        print ('== > Adding')
        allnr = getnumber()
        add(allnr[0], allnr[1])

    elif val == '-':
        print ('== > Subtracting')
        allnr = getnumber()
        sub(allnr[0], allnr[1])

    elif val == '/':
        print ('== > Dividing')
        allnr = getnumber()
        div(allnr[0], allnr[1])
    else:
        print (':-(  Not a valid operation')
        break




