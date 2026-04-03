import os
import subprocess

def clear_console():
    cmd = "cls" if os.name == "nt" else "clear"
    subprocess.call(cmd, shell=True)

clear_console()

## ---------------------------------------------------

def skapa_anvandare(namn, alder):
    """
    :param namn:
    :param alder:
    :return: Informe Name and Age
    """
    print(f"{namn} is {alder} years old")


def kontrollera_alder(alder):
    """
    Control if Age is 0 or negative
    Return error info, if found
    """
    if alder < 0:
        # Vi skapar ett ValueError med ett eget meddelande
        raise ValueError("Age can not be negative!")
    elif alder == 0:
        raise ValueError("Age can not be zero!")
    elif alder > 150:
        raise ValueError("You are too old to be alive :-( !")

    return f"    Age {alder} is approved."


namn  = input(' Give your name : ')
alder = int(input(' Give your age  : '))
try:
    print(kontrollera_alder(alder))
except ValueError as e:
    print(f"Error: {e}")
    exit(1)


skapa_anvandare(namn,alder)