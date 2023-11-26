import os
import time
import pyfiglet
import colorama
from colorama import Fore


title = Fore.BLUE+pyfiglet.figlet_format("PY TO EXE")+Fore.RESET


print(title)


filename = input("Input file name (INCLUDE .py): "+Fore.RESET).lower()

def makepytoexe():
    print(Fore.GREEN+"Installing PYINSTALLER To latest version! Please wait."+Fore.RESET)
    print(Fore.RED+"[IMPORTANT!]: Please press Y when it prompts you to..."+Fore.RESET)
    time.sleep(3)
    os.system("pip uninstall pyinstaller")
    print(Fore.GREEN+"Step 1 DONE"+Fore.RESET)
    time.sleep(1)
    os.system("pip install pyinstaller")
    print(Fore.GREEN+"Step 2 DONE"+Fore.RESET)
    os.system("python -m PyInstaller "+filename+" --onefile")
    print(Fore.GREEN+"File is in "+os.getcwd()+"/dist, Thanks for using program!")

if ".py" not in filename:
    print(Fore.RED+"This is not a py file."+Fore.RESET)
    print("Press ENTER To exit.")
elif ".py" in filename:
    print(Fore.GREEN+"This is a python file! Going on to step 2."+Fore.RESET)
    time.sleep(3)
    os.system("cls")
    print(title)
    makepytoexe()


input()