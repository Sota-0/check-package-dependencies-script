import time
import os
import sys
from colorama import Fore, init

init(autoreset=True)


# Note: if a dependency cant be found, re-running the script is useless.
#       you may need to verify the package name incase of dependency failure.

# CHANGE ME
dependencies = ["curl", "nano", "PlaceHolder1", "PlaceHolder2"]
to_install = []
a = 0

def main():
    global a
    
    for i in dependencies:
        check = os.popen(f"apt-cache policy {i}").read()
        if i not in check:
            print(Fore.RED + "[-]", i)
            to_install.append(i)
            time.sleep(.1)
            a = 1    
        else:
            print(Fore.GREEN + "[+]", i)
            time.sleep(.1)
    
    if a == 1:
        print("install dependencies? (y / n) : ", to_install)

        while True:
                command = input(">>")

                if command == "y":
                    print("installing...")
                    for i in to_install:
                        os.system(f"sudo apt-get install {i}")
                    time.sleep(.5)
                    print("")
                    print(Fore.MAGENTA + "please re-run the script")
                    break

                elif command == "n":
                     print(Fore.RED + "Dependencies are REQUIRED")
                     print("exiting script...")
                     break
                
                else:
                     print("Please Enter a valid answer: y or n")

    else:
        print("")
        print("all requirements are met")
        # ADD NEXT STEP
        pass



main()

