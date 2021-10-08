import os
os.system("color")

def blankSpace():
    for i in range(40):
        print("")

BOLD = '\033[1m'
HEADER = "\033[95m"
BLUE =  "\033[94m"
GREEN =  "\033[92m"
RED =  "\033[91m"
PURPLE = "\033[95m"
YELLOW = "\033[33m"
ENDC = "\033[0m"

blankSpace()

def main():
    
    blankSpace()
    
    print(f"""
    1){BOLD}{RED} Cabin Default{ENDC}
    2){BOLD}{BLUE} Undercroft{ENDC}
    3){BOLD}{GREEN} Requiem{ENDC}
    4){BOLD}{YELLOW} Opulence{ENDC}
    5){BOLD}{PURPLE} Penumbra{ENDC}
    """)

    menuChoice = str(input("What menu do you want to view? (input the number of selection): "))

    blankSpace()

    if menuChoice == "1":
    
        print(f"""
        {RED}{BOLD}

▄▄▄█████▓ ██░ ██ ▓█████     ▄████▄   ▄▄▄       ▄▄▄▄    ██▓ ███▄    █ 
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▒██▀ ▀█  ▒████▄    ▓█████▄ ▓██▒ ██ ▀█   █ 
▒ ▓██░ ▒░▒██▀▀██░▒███      ▒▓█    ▄ ▒██  ▀█▄  ▒██▒ ▄██▒██▒▓██  ▀█ ██▒
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██░█▀  ░██░▓██▒  ▐▌██▒
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ▒ ▓███▀ ░ ▓█   ▓██▒░▓█  ▀█▓░██░▒██░   ▓██░
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░ ░▒ ▒  ░ ▒▒   ▓▒█░░▒▓███▀▒░▓  ░ ▒░   ▒ ▒ 
    ░     ▒ ░▒░ ░ ░ ░  ░     ░  ▒     ▒   ▒▒ ░▒░▒   ░  ▒ ░░ ░░   ░ ▒░
  ░       ░  ░░ ░   ░      ░          ░   ▒    ░    ░  ▒ ░   ░   ░ ░ 
          ░  ░  ░   ░  ░   ░ ░            ░  ░ ░       ░           ░ 
                           ░                        ░                
                       - Will you survive? - 
                       -       v1.0        -  
    {ENDC}{BOLD}
    1) Start
    2) Options
    3) Credits
    0) Exit{ENDC}
        """)

        userInput = input(f"{RED}{BOLD}What would you like to do (input the number of selection): {ENDC}")
        main()
    
    elif menuChoice == "2":
    
        print(f"""{RED}{BOLD}                   -       The Cabin       -   {ENDC}
        {BLUE}{BOLD}
  ▄      ▄   ██▄   ▄███▄   █▄▄▄▄ ▄█▄    █▄▄▄▄ ████▄ ▄████     ▄▄▄▄▀ 
   █      █  █  █  █▀   ▀  █  ▄▀ █▀ ▀▄  █  ▄▀ █   █ █▀   ▀ ▀▀▀ █    
█   █ ██   █ █   █ ██▄▄    █▀▀▌  █   ▀  █▀▀▌  █   █ █▀▀        █    
█   █ █ █  █ █  █  █▄   ▄▀ █  █  █▄  ▄▀ █  █  ▀████ █         █     
█▄ ▄█ █  █ █ ███▀  ▀███▀     █   ▀███▀    █          █       ▀      
 ▀▀▀  █   ██                ▀            ▀            ▀             
                   - Permanent Tribulation - 
                   -         v2.0          -  
    {ENDC}{BOLD}
    1) Start
    2) Options
    3) Credits
    0) Exit{ENDC}
        """)
    
        userInput = input(f"{BLUE}{BOLD}What would you like to do (input the number of selection): {ENDC}")
        main()
    
    elif menuChoice == "3":
    
        print(f"""{RED}{BOLD}                      -      The Cabin      -   {ENDC}
        {GREEN}{BOLD}
 ▄▀▀▄▀▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▀▀▄   ▄▀▀▄ ▄▀▀▄  ▄▀▀█▀▄   ▄▀▀█▄▄▄▄  ▄▀▀▄ ▄▀▄ 
█   █   █ ▐  ▄▀   ▐ █      █ █   █    █ █   █  █ ▐  ▄▀   ▐ █  █ ▀  █ 
▐  █▀▀█▀    █▄▄▄▄▄  █      █ ▐  █    █  ▐   █  ▐   █▄▄▄▄▄  ▐  █    █ 
 ▄▀    █    █    ▌   ▀▄▄▄▄▀▄   █    █       █      █    ▌    █    █  
█     █    ▄▀▄▄▄▄           █   ▀▄▄▄▄▀   ▄▀▀▀▀▀▄  ▄▀▄▄▄▄   ▄▀   ▄▀  
 
                      - Ascend while we die - 
                      -        v3.0         -  
    {ENDC}{BOLD}
    1) Start
    2) Options
    3) Credits
    0) Exit{ENDC}
        """)

        userInput = input(f"{GREEN}{BOLD}What would you like to do (input the number of selection): {ENDC}")
        main()

    elif menuChoice == "4":
    
        print(f"""{RED}{BOLD}                                              
                               -         The Cabin         -   {ENDC}
        {YELLOW}{BOLD}
 ▄██████▄     ▄███████▄ ███    █▄   ▄█          ▄████████ ███▄▄▄▄    ▄████████    ▄████████ 
███    ███   ███    ███ ███    ███ ███         ███    ███ ███▀▀▀██▄ ███    ███   ███    ███ 
███    ███   ███    ███ ███    ███ ███         ███    █▀  ███   ███ ███    █▀    ███    █▀  
███    ███   ███    ███ ███    ███ ███        ▄███▄▄▄     ███   ███ ███         ▄███▄▄▄     
███    ███ ▀█████████▀  ███    ███ ███       ▀▀███▀▀▀     ███   ███ ███        ▀▀███▀▀▀     
███    ███   ███        ███    ███ ███         ███    █▄  ███   ███ ███    █▄    ███    █▄  
███    ███   ███        ███    ███ ███▌    ▄   ███    ███ ███   ███ ███    ███   ███    ███ 
 ▀██████▀   ▄████▀      ████████▀  █████▄▄██   ██████████  ▀█   █▀  ████████▀    ██████████                                                         

                               - Oppression through wealth - 
                               -          v4.0             -  
    {ENDC}{BOLD}
    1) Start
    2) Options
    3) Credits
    0) Exit{ENDC}  
            """)

        userInput = input(f"{YELLOW}{BOLD}What would you like to do (input the number of selection): {ENDC}")
        main()

    elif menuChoice == "5":
    
        print(f"""{RED}{BOLD}
                         -      The Cabin     -   {ENDC}
        {PURPLE}{BOLD}
 ██▓███  ▓█████  ███▄    █  █    ██  ███▄ ▄███▓ ▄▄▄▄    ██▀███   ▄▄▄      
▓██░  ██▒▓█   ▀  ██ ▀█   █  ██  ▓██▒▓██▒▀█▀ ██▒▓█████▄ ▓██ ▒ ██▒▒████▄    
▓██░ ██▓▒▒███   ▓██  ▀█ ██▒▓██  ▒██░▓██    ▓██░▒██▒ ▄██▓██ ░▄█ ▒▒██  ▀█▄  
▒██▄█▓▒ ▒▒▓█  ▄ ▓██▒  ▐▌██▒▓▓█  ░██░▒██    ▒██ ▒██░█▀  ▒██▀▀█▄  ░██▄▄▄▄██ 
▒██▒ ░  ░░▒████▒▒██░   ▓██░▒▒█████▓ ▒██▒   ░██▒░▓█  ▀█▓░██▓ ▒██▒ ▓█   ▓██▒
▒▓▒░ ░  ░░░ ▒░ ░░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░░▒▓███▀▒░ ▒▓ ░▒▓░ ▒▒   ▓▒█░
░▒ ░      ░ ░  ░░ ░░   ░ ▒░░░▒░ ░ ░ ░  ░      ░▒░▒   ░   ░▒ ░ ▒░  ▒   ▒▒ ░
░░          ░      ░   ░ ░  ░░░ ░ ░ ░      ░    ░    ░   ░░   ░   ░   ▒   
            ░  ░         ░    ░            ░    ░         ░           ░  ░
                                                     ░                    
                         -  Fathom the Abyss  - 
                         -        v5.0        -  
    {ENDC}{BOLD}
    1) Start
    2) Options
    3) Credits
    0) Exit{ENDC}
            """)

        userInput = input(f"{PURPLE}{BOLD}What would you like to do (input the number of selection): {ENDC}")
        main()
        
main()