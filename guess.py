# -*- coding: utf-8 -*-

import random

def valorErroneo():
    while True:
        nuevaPartida = str(input("Quieres jugar de nuevo? (S/N): "))
        if nuevaPartida.casefold() == "s":
            break
        elif nuevaPartida.casefold() == "n":
            print( "Hasta Otra!".center(135, " ") )
            exit()
        else:
            print ( "El valor introducido es incorrecto!".center(125, " "))
            continue


while True:

    numeroRand = round(random.random()*2)

    try:
        numeroIntro = int(input( "Introduce un número del 1 al 100: " ))
    
        if numeroIntro == numeroRand:
            print ( "Has Acertado!".center(135, " ") )
        
            nuevaPartida = str(input("Quieres jugar de nuevo? (S/N): "))
            if nuevaPartida.casefold() == "s":
                continue
            elif nuevaPartida.casefold() == "n":
                print( "Hasta Otra!".center(135, " ") )
                break
            else:
                print ( "El valor introducido es incorrecto!".center(125, " "))
                valorErroneo()
            
        else:
            nuevaPartida = str(input("Has fallado, quieres jugar de nuevo? (S/N): "))
            if nuevaPartida.casefold() == "s":
                continue
            elif nuevaPartida.casefold() == "n":
                print( "Hasta Otra!".center(135, " ") )
                break
            else:
                print ( "El valor introducido es incorrecto!".center(125, " "))
                valorErroneo()
           
    except KeyboardInterrupt:
        print ( "Has interrumpido el programa!".center(125, " "))
        exit()
    except ValueError:
        print ( "El valor introducido es incorrecto!".center(125, " "))
        continue
