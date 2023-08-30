#!/usr/bin/env python3
from time import sleep
import os
from colorama import init, Fore, Style
init()
os.system("pip install colorama")
os.system("pip install os")
os.system("pip install time")
print(Fore.GREEN+Style.BRIGHT+"""
::::::::'##'##::::'##'########:'######:::'#######: :                  
:::::::: ##:##:::: ##:##.....:'##... ##:'##.... ##:                  
:::::::: ##:##:::: ##:##:::::::##:::..:::##:::: ##:                  
:::::::: ##:##:::: ##:######:::##::'####:##:::: ##:                  
::'##::: ##:##:::: ##:##...::::##::: ##::##:::: ##:                  
:::##::: ##:##:::: ##:##:::::::##::: ##::##:::: ##:                  
::. ######:. #######::########. ######::. #######::                  
:'######::'#######:'##:::::::'######:::::'###:::'# #######::'#######::
'##... ##'##.... ##:##::::::'##... ##:::'## ##:::##... .##'##.... ##:
 ##:::..::##:::: ##:##:::::::##:::..:::'##:. ##::##:::: ##:##:::: ##:
 ##:::::::##:::: ##:##:::::::##::'####'##:::. ##:##:::: ##:##:::: ##:
 ##:::::::##:::: ##:##::::::::##::: ##::#########:##:: :: ##:##:::: ##:
 ##::: ##:##:::: ##:##:::::::##::: ##::##.... ##:##:::: ##:##:::: ##:
. ######:. #######::########. ######:::##:::: ##:########:. #######::
:......:::.......::........::......:::..:::::..:.. ......:::.......:::



\n\n""")

title = Fore.YELLOW+Style.BRIGHT+""" 
                Created   by:   
                                                                                                    1LugarParaProgramar
                
                Author:  Hans Saldias
                
                Script : Juego del colgado 
                
                 *__________ V 1 _________*
                
                \n\n"""
for t in title:
    print(t, end='', flush=True)      
    sleep(0.1)         
palabra = input("Ingresa una palabra: ")
letras_adivinadas = []
os.system("clear")
print(title)


while True:
    letra = input("Ingresa una letra: ")

    if letra in palabra:
        letras_adivinadas.append(letra)
        palabra_mostrada = ""
        for caracter in palabra:
            if caracter in letras_adivinadas:
                palabra_mostrada += caracter
            else:
                palabra_mostrada += " _ "
        print(palabra_mostrada)

        if palabra_mostrada == palabra:
            print("¡Felicidades! Has adivinado la palabra correctamente.")
            break
    else:
        print(f"La {letra} no está en la palabra. Intenta nuevamente.")
        
op = input("¿Deseas jugar nuevamente? (s/n): ")
if op == "s":
    os.system("python3  colgado.py")
else:
    print("Gracias 1LugarParaProgramar Created : Hans saldias")