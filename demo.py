import threading
from trendCreate import createTCP
from TrendUpdateTCP import TCP


def main():
    print("Menu principal")
    print("1. Agregar agente")
    x = input("Opción: ")

    if x == '1':
        agrega()


def agrega():
    com = input("Dame la comunidad: ")
    ip = input("Dame la ip: ")
    par = input("Dame el parametro a contablilzar: ")
    nom = 'trend'+par
    createTCP(nom)
    z = threading.Thread(target=TCP, args=(com, ip))
    z.start()


main()