from termcolor import *

print(colored("""
 █████╗ ██████╗ ██████╗  █████╗ ██████╗  █████╗ ████████╗ █████╗ 
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
███████║██████╔╝██████╔╝███████║██████╔╝███████║   ██║   ███████║
██╔══██║██╔═══╝ ██╔═══╝ ██╔══██║██╔══██╗██╔══██║   ██║   ██╔══██║
██║  ██║██║     ██║     ██║  ██║██║  ██║██║  ██║   ██║   ██║  ██║
╚═╝  ╚═╝╚═╝     ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝

1) Start
2) Options
3) Credits
0) Exit
     """, "grey", attrs=["bold", "blink`"]))

userInput = input(colored("What do you want to do? (Input the number of selection): ", "grey", attrs=["bold", "blink"]))