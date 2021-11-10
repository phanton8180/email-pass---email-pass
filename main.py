import colorama

from colorama import Fore, Style, init

cyan = {Fore.RED}


def ascii():
    print(f"""{Fore.RED} {Style.BRIGHT}
 ███▄    █ ▓█████  █    ██ ▄▄▄█████▓ ██▀███   ▒█████   ███▄    █ 
 ██ ▀█   █ ▓█   ▀  ██  ▓██▒▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒ ██ ▀█   █ 
▓██  ▀█ ██▒▒███   ▓██  ▒██░▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒▓██  ▀█ ██▒
▓██▒  ▐▌██▒▒▓█  ▄ ▓▓█  ░██░░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░▓██▒  ▐▌██▒
▒██░   ▓██░░▒████▒▒▒█████▓   ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░▒██░   ▓██░
░ ▒░   ▒ ▒ ░░ ▒░ ░░▒▓▒ ▒ ▒   ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
░ ░░   ░ ▒░ ░ ░  ░░░▒░ ░ ░     ░      ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░░   ░ ▒░
   ░   ░ ░    ░    ░░░ ░ ░   ░        ░░   ░ ░ ░ ░ ▒     ░   ░ ░ 
         ░    ░  ░   ░                 ░         ░ ░           ░ 
     
                                                                 
                   ({Fore.YELLOW}MODULE{Fore.RED}) » {Fore.YELLOW} email:pass -> email|pass{Fore.RESET}                                          
""")


vr.title = (f"Neutron9 ~ {vr.user} ~ Dupe Remover")


def phanton():
    ascii()
    path = input(" Enter The File Path:  ")
    outpath = input(" Enter The File Path you would like to save it to:  ")
    fin = open(path, "rt")
    fout = open(outpath, "wt")
    for line in fin:
        fout.write(line.replace(':', ';'))
    path.close()
    fout.close()
    input("press Enter to Exit")


phanton()
