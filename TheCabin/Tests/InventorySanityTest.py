import time

from termcolor import *

for i in range(30):
    print("")
    
def main():

    userInput = input(colored("What do you want to do? (type help for a list of commands): ", "red", attrs=["bold"]))

    if userInput == "inventory":
        
        def loop():
            for i in range(40):
                print("You have nothing",end="")
                
        
            
main()
