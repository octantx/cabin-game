
# ? UPDATE LOG: (Current release: BETA | A=Alpha, B=Beta, F=Full)
# ? Major mechanic added = +0.1 
# ? Minor mechanic added = +0.05   
# ? Content added        = +0.03  
# ? Dialogue change      = +0.01  

    # * The Cabin | 24/8/21 | version A0.0 : Prototyping, making mechanics etc
    # * The Cabin | 25/8/21 | version A0.2 : Functional prototype, testing
    # * The Cabin | 25/8/21 | version A0.3 : Maps 
    # * The Cabin | 26/8/21 | version A0.4 : Functional saving system
    # * The Cabin | 31/8/21 | version A0.45: Map state appending across rooms, successful room loading after save
    # * The Cabin | 01/9/21 | version A0.55: Map progression system
    # * The Cabin | 01/9/21 | version B0.57: Revised dialogue 
    # * The Cabin | 02/9/21 | version B0.62: Revised first room (R1)
    # * The Cabin | 07/9/21 | version B0.67: Revised first room (R2), randint killer movement, more hallway content
    # * The Cabin | 09/9/21 | version B0.72: More hallway content, random killer location across saves
    # * The Cabin | 13/9/21 | version B0.77: Death added and works, third room prompt and death if killer is there
    # * The Cabin | 14/9/21 | version B0.82: Themes!
    # * The Cabin | 14/9/21 | version B0.85: Hallway finished and bedroom is ready to be made
    # * The Cabin | 15/9/21 | version B0.88: Bedroom finished and kitchen ready to be made
    # * The Cabin | 15/9/21 | version B0.89: Revised dialogue
    # * The Cabin | 20/9/21 | version B0.92: Touch ups across functions and kitchen content done
    # * The Cabin | 20/9/21 | version B0.95: Kitchen fully complete and living room ready to be made
    # * The Cabin | 25/9/21 | version F1.00: Full game complete, full release
    
# ? Blankspace function is created to clear up the terminal periodically
def blankspace():
    
    for i in range(45):
        print("")
        
# ? Save location variable so the path can be change (mostly for development purposes)
saveStateLocation = "TheCabin/SaveState.txt" # ! To be changed to just "SaveState.txt" when packaging

# ? Version number variable is created so I don't have to find every instance of the version being mentioned and change it
ver = "v1.00"

# ? Date of last update variable is created for the credits
date = "September 25th 2021"

# ? The regex module is imported so the program can search for strings in strings
import re

# ? Import the time module
import time

# ? Import the sys module for when the user wants to exit the program
import sys

# ? Import the termcolor module for colouring text with error checking
try:
    from termcolor import *
except:
    
    blankspace()

    print("""
Termcolor is not installed, and this game needs it to do all the fancy colouring effects!
To install termcolor, please close this terminal instance and input \"pip install termcolor\",
then run the python file again. This installation may vary from computer to computer so if that installation command doesn't work,
please try searching "how to install termcolor on my computer" on a web browser and follow those instructions. Enjoy!
    """)
    
    input("")
    
    sys.exit()
    
# ? Import the random module so random integers can be created
import random

# ? -------------- Loading game theme ----------------------------------------------------------------------------------------------

themeArray = ["red"]

try:
    
    saveState = open(saveStateLocation)

except:
    
    blankspace()
    
    print("\"SaveState.txt\" cannot be found, please reinstall the program or ensure that \"SaveState.txt\" is within the same directory as the executable.")
    
    print("")
    
    input("")
    
    sys.exit()

saveContent = saveState.read()

findRed = re.search("Theme=Red", saveContent)

findBlue = re.search("Theme=Blue", saveContent)

findGreen = re.search("Theme=Green", saveContent)

findYellow = re.search("Theme=Yellow", saveContent)

findMagenta = re.search("Theme=Magenta", saveContent)

if findRed:
    
    themeArray.clear()
    themeArray.append("red")
    
elif findBlue:
    
    themeArray.clear()
    themeArray.append("blue")

elif findGreen:
    
    themeArray.clear()
    themeArray.append("green")

elif findYellow:
    
    themeArray.clear()
    themeArray.append("yellow")
    
elif findMagenta:
    
    themeArray.clear()
    themeArray.append("magenta")
    
# ? -------------- Loading game theme ----------------------------------------------------------------------------------------------
    
def overwrite():
    
        saveState = open(saveStateLocation, "rt")
        
        saveSanityState = open(saveStateLocation)
        
        saveSanity = saveSanityState.readlines()
        
        saveContent = saveState.read()
        
        # ? ------------------------------------------------------------------------
        
        sanfind = saveSanity[1]
        
        sanfind = sanfind.replace("Sanity=", "")
        
        sanfind = str(sanfind)
        
        replace = """Sanity=0
"""
        saveContent = saveContent.replace(f"Sanity={sanfind}", replace)
        
        saveSanityState.close()
        
        saveState = open(saveStateLocation, "wt")
        
        saveState.write(saveContent)
        
        # ? ------------------------------------------------------------------------
        
        find3 = re.search("Location=3", saveContent)
        
        find4 = re.search("Location=4", saveContent)
        
        find5 = re.search("Location=5", saveContent)
        
        saveContent = saveContent.replace("True", "False")
            
        saveState.close()
        
        saveState = open(saveStateLocation, "wt")
        
        saveState.write(saveContent)
        
        saveState = open(saveStateLocation, "rt")
        
        saveContent = saveState.read()
        
        if find3:
            
            saveContent = saveContent.replace("Location=3", "Location=0")
            saveState.close()
            saveState = open(saveStateLocation, "wt")
            saveState.write(saveContent)
            
        elif find4:
            
            saveContent = saveContent.replace("Location=4", "Location=0")
            saveState.close()
            saveState = open(saveStateLocation, "wt")
            saveState.write(saveContent)
            
        elif find5:
            
            saveContent = saveContent.replace("Location=5", "Location=0")
            saveState.close()
            saveState = open(saveStateLocation, "wt")
            saveState.write(saveContent)
            
        saveState.close()
        
# ? Define the function called "game" which is called when the user selects the option to begin the game
def game():
    
    saveState = open(saveStateLocation)
    
    saveContent = saveState.read()
    
    saveState.close()
    
    theme = str(themeArray[0])
    
    continueCheck = re.search("True", saveContent)
    
    sanity = [0]
    
    sanityevents = []
    
    inventory = []
    
    interactionSave = []
    
    mapState = ["1"]
    
    mapBeen = []
    
    mapProgression = []

    exitCheck = []
    
    if continueCheck:

        location3Check = re.search("Location=3", saveContent)
        
        location4Check = re.search("Location=4", saveContent)
        
        location5Check = re.search("Location=5", saveContent)
        
        if location3Check: 
            
            interactionSave.append("location3")
            
        elif location4Check:
            
            interactionSave.append("location4")
            
        elif location5Check:
            
            interactionSave.append("location5")

    else:
        
        starLocation = random.randint(3,5)
        starLocation = str(starLocation)
        staticLocationAppend = str("location"+starLocation)
        interactionSave.append(staticLocationAppend)
    
    help =  """
        inventory: Shows you the items in your inventory
        save: Saves the game based on your current interactions and inventory items, when you start the game again you'll load from this point
        prompt: Prints the prompt of the current room
        exit: Saves and quits the game
        clear: Clears up the terminal and removes all old commands from sight
        restart: Restarts the whole game
        menu: Takes you back to the menu of the game
        pick up _____: Picks up items to be added to your inventory
        look at _____: Uses your eyes to look at an object or thing, and provides a further examination
        go to the _____: Goes to a different room if the means of entrance are unlocked
        use _____: Use and/or interact with an item or thing in the world
        use _____ with _____: Uses an item in your inventory with an item or thing in the world
            """

    blankspace()
    
    print(colored("""
    ▓█████▄  █    ██  ███▄    █ 
    ▒██▀ ██▌ ██  ▓██▒ ██ ▀█   █ 
    ░██   █▌▓██  ▒██░▓██  ▀█ ██▒
    ░▓█▄   ▌▓▓█  ░██░▓██▒  ▐▌██▒
    ░▒████▓ ▒▒█████▓ ▒██░   ▓██░
     ▒▒▓  ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ 
     ░ ▒  ▒ ░░▒░ ░ ░ ░ ░░   ░ ▒░
     ░ ░  ░  ░░░ ░ ░    ░   ░ ░ 
       ░       ░              ░ 
     ░                          
    """, f"{theme}", attrs=["bold"]))
    
    time.sleep(0.9)
    
    blankspace()
        
    time.sleep(0.6)
    
    print(colored("""
    ▓█████▄     █    ██     ███▄    █ 
    ▒██▀ ██▌    ██  ▓██▒    ██ ▀█   █ 
    ░██   █▌   ▓██  ▒██░   ▓██  ▀█ ██▒
    ░▓█▄   ▌   ▓▓█  ░██░   ▓██▒  ▐▌██▒
    ░▒████▓    ▒▒█████▓    ▒██░   ▓██░
     ▒▒▓  ▒    ░▒▓▒ ▒ ▒    ░ ▒░   ▒ ▒ 
     ░ ▒  ▒    ░░▒░ ░ ░    ░ ░░   ░ ▒░
     ░ ░  ░     ░░░ ░ ░       ░   ░ ░ 
       ░          ░                 ░ 
     ░                                
    """, f"{theme}", attrs=["bold"]))
    
    time.sleep(0.9)
    
    blankspace()
        
    time.sleep(0.6)
    
    print(colored("""
    ▓█████▄     █    ██     █    ██     █    ██     ███▄    █     ███▄    █     ███▄    █     ███▄    █                         
    ▒██▀ ██▌    ██  ▓██▒    ██  ▓██▒    ██  ▓██▒    ██ ▀█   █     ██ ▀█   █     ██ ▀█   █     ██ ▀█   █                         
    ░██   █▌   ▓██  ▒██░   ▓██  ▒██░   ▓██  ▒██░   ▓██  ▀█ ██▒   ▓██  ▀█ ██▒   ▓██  ▀█ ██▒   ▓██  ▀█ ██▒                        
    ░▓█▄   ▌   ▓▓█  ░██░   ▓▓█  ░██░   ▓▓█  ░██░   ▓██▒  ▐▌██▒   ▓██▒  ▐▌██▒   ▓██▒  ▐▌██▒   ▓██▒  ▐▌██▒                        
    ░▒████▓    ▒▒█████▓    ▒▒█████▓    ▒▒█████▓    ▒██░   ▓██░   ▒██░   ▓██░   ▒██░   ▓██░   ▒██░   ▓██░    ██▓     ██▓     ██▓ 
     ▒▒▓  ▒    ░▒▓▒ ▒ ▒    ░▒▓▒ ▒ ▒    ░▒▓▒ ▒ ▒    ░ ▒░   ▒ ▒    ░ ▒░   ▒ ▒    ░ ▒░   ▒ ▒    ░ ▒░   ▒ ▒     ▒▓▒     ▒▓▒     ▒▓▒ 
     ░ ▒  ▒    ░░▒░ ░ ░    ░░▒░ ░ ░    ░░▒░ ░ ░    ░ ░░   ░ ▒░   ░ ░░   ░ ▒░   ░ ░░   ░ ▒░   ░ ░░   ░ ▒░    ░▒      ░▒      ░▒  
     ░ ░  ░     ░░░ ░ ░     ░░░ ░ ░     ░░░ ░ ░       ░   ░ ░       ░   ░ ░       ░   ░ ░       ░   ░ ░     ░       ░       ░   
       ░          ░           ░           ░                 ░             ░             ░             ░      ░       ░       ░  
     ░                                                                                                       ░       ░       ░  
    """, f"{theme}", attrs=["bold"]))
    
    time.sleep(2)
    
    blankspace()
        
    time.sleep(0.25)
    
    startingPrompt = (colored("""
    Consciousness, your nightmare ends, but a larger fear kicks in. 
    You find yourself on a bare mattress in an office-like room where a desk in front of a large patch of blood has been aggressively thrown, 
    hurling several items down with it. Every window from head to toe covered in newspaper, 
    a bookshelf of immense scale in place of a wall and an opulent red rug in the centre of the room. 
    Any hope has been replaced with tribulation and nothing will be the same.
    """, attrs=["bold"]))

    hallwayPrompt = (colored("""
    You cautiously walk into the hall, wary of your own sound while pondering the physique of the monstoristy making the footsteps and groans previous.
    Stepping over the man and onto the creaky floorboard of the to be explored hallway which is covered by another red rug.
    You spot doors to your direct left and right, and a door in the middle from where you're standing.
    Pictures cover the hall but so does a noticeable absence of blood compared to the horror show in the room you woke up in.
    """, attrs=["bold"]))
    
    # ? ----------------------------------------------- Trolley concat
    
    interactionSaveUseable = str(interactionSave)
    
    location3Check = re.search("location3", interactionSaveUseable)
    
    location4Check = re.search("location4", interactionSaveUseable)
    
    location5Check = re.search("location5", interactionSaveUseable)
    
    if location4Check:

        bedroomKillerNotThere = (colored("""
    You open the door as carefully and as silently as you can. The room past the left door seems to be a quaint bedroom, with a large luxurious walnut bed
    accompanied by large walnut drawers and a seemingly vacant space for a wardrobe. How could a person like Frank have a nice bedroom like this?
    The last thing you notice is a large hand trolley to your direct right after opening the door.""", attrs=["bold"]))
    
    else:
        
        bedroomKillerNotThere = (colored("""
    You open the door as carefully and as silently as you can. The room past the left door seems to be a quaint bedroom, with a large luxurious walnut bed
    accompanied by large walnut drawers and a seemingly vacant space for a wardrobe. How could a person like Frank have a nice bedroom like this?""", attrs=["bold"]))
        
    bedroomKillerDead = (colored("""
    Frank Walker lays dead on the ground in a pool of his own blood. What you have done will stay with you for the rest of your days.
    The room, now docile, is a bedroom. It houses a large luxurious walnut bed, accompanied by large walnut drawers and a seemingly vacant space for a wardrobe.
    This place will devour your mind.
    """, attrs=["bold"]))
    
    bedroomKillerAlive = (colored("""
    Frank Walker writhes in pain on the ground in a pool of his own blood, screaming at your actions. What you have done will stay with you for the rest of your days.
    The room, now docile, is a bedroom. It houses a large luxurious walnut bed, accompanied by large walnut drawers and a seemingly vacant space for a wardrobe.
    This place will devour your mind.
    """, attrs=["bold"])) 
    
    if location3Check:

        kitchenKillerNotThere = (colored("""
    You open the door as carefully and as silently as you can. But suddenly the smell hits you and the sight overwhelms you.
    The room past the right door is a horrific kitchen, where only the worst has occurred. In attempts to cover tracks and out of pure desperation, atrocities have been committed.
    The center of the kitchen holds a huge meat grinder and to the left of the door, a befouled stove contains boiling over pots and several pans which have been knocked over.
    Directly ahead are windows with no newspaper on them, however they've been barred, and it would be near impossible to get out that way.
    A fridge stands valiantly as one of the only relatively clean objects in the room. 
    How could Frank do something like this? The last thing you notice is a large hand trolley at the back of the room.""", attrs=["bold"]))
        
    elif location5Check:
        
        kitchenKillerNotThere = (colored("""
    You open the door as carefully and as silently as you can. But suddenly the smell hits you and the sight overwhelms you.
    The room past the right door is a horrific kitchen, where only the worst has occurred. In attempts to cover tracks and out of pure desperation, atrocities have been committed.
    The center of the kitchen holds a huge meat grinder and to the left of the door, a befouled stove contains boiling over pots and several pans which have been knocked over.
    Directly ahead are windows with no newspaper on them, however they've been barred, and it would be near impossible to get out that way.
    A fridge stands valiantly as one of the only relatively clean objects in the room. 
    How could Frank do something like this? You notice a large hand trolley at the back of the room, and a scarlet crowbar at the foot of the grinder.""", attrs=["bold"]))
        
    else:
        
        kitchenKillerNotThere = (colored("""
    You open the door as carefully and as silently as you can. But suddenly the smell hits you and the sight overwhelms you.
    The room past the right door is a horrific kitchen, where only the worst has occurred. In attempts to cover tracks and out of pure desperation, atrocities have been committed.
    The center of the kitchen holds a huge meat grinder and to the left of the door, a befouled stove contains boiling over pots and several pans which have been knocked over.
    Directly ahead are windows with no newspaper on them, however they've been barred, and it would be near impossible to get out that way.
    A fridge stands valiantly as one of the only relatively clean objects in the room. 
    How could Frank do something like this?""", attrs=["bold"]))
        
    kitchenKillerDead = (colored("""
    Frank Walker lays dead on the ground in a pool of his own blood. What you have done will stay with you for the rest of your days.
    The room, now hostile, is a truly disgusting horror to behold. Your sense of smell is overwhelmed and the sight of the room, now truly taking it in, is awful.
    In attempts to cover tracks and out of pure desperation, atrocities have been committed. The center of the kitchen holds a huge meat grinder and to the left of the door,
    a befouled stove contains boiling over pots and several pans which have been knocked over.
    Directly ahead are windows with no newspaper on them, however they've been barred, and it would be near impossible to get out that way.
    A fridge stands valiantly as one of the only relatively clean objects in the room. All you know is pain.
    """, attrs=["bold"]))
    
    kitchenKillerAlive = (colored("""
    Frank Walker writhes in pain on the ground in a pool of his own blood, screaming at your actions. What you have done will stay with you for the rest of your days.
    The room, now hostile, is a truly disgusting horror to behold. Your sense of smell is overwhelmed and the sight of the room, now truly taking it in, is awful.
    In attempts to cover tracks and out of pure desperation, atrocities have been committed. The center of the kitchen holds a huge meat grinder and to the left of the door,
    a befouled stove contains boiling over pots and several pans which have been knocked over.
    Directly ahead are windows with no newspaper on them, however they've been barred, and it would be near impossible to get out that way.
    A fridge stands valiantly as one of the only relatively clean objects in the room. All you know is pain.
    """, attrs=["bold"]))
    
    # ? -------------------------------------------------------------------------------------------------
    
    livingRoomKillerNotThere = (colored("""
    You open the door to the final room and a living room greets you upon entry. A final door is parallel to your position which holds 3 locks.
    The rest of the room is homely, a fireplace is on for warmth, joined by a large leather couch. Another rug makes itself known with it's familiar red and gold swirls,
    a large triumphant paining above the fireplace rests perfectly centered, and a counter with an alluring amount of alcohol with accompanying wine glasses.
    """, attrs=["bold"]))
    # ? main prompt ^ 
    
    livingRoomKillerAlive = (colored("""
    Frank Walker writhes in pain on the ground in a pool of his own blood, screaming at your actions. What you have done will stay with you for the rest of your days.
    The room, now malignant, is uncomfortably homely to take in. A living room greets you upon entry. A final door is parallel to your position which holds 3 locks.
    The rest of the room is homely, a fireplace is on for warmth, joined by a large leather couch. Another rug makes itself known with it's familiar red and gold swirls,
    a large triumphant paining above the fireplace rests perfectly centered, and a counter with an alluring amount of alcohol with accompanying wine glasses.
    Permanent tribulation.
    """, attrs=["bold"]))
    # ? frank alive in room ^ 
    
    livingRoomKillerDead = (colored("""
    Frank Walker lays dead on the ground in a pool of his own blood.
    The room, now malignant, is uncomfortably homely to take in. A living room greets you upon entry. A final door is parallel to your position which holds 3 locks.
    The rest of the room is homely, a fireplace is on for warmth, joined by a large leather couch. Another rug makes itself known with it's familiar red and gold swirls,
    a large triumphant paining above the fireplace rests perfectly centered, and a counter with an alluring amount of alcohol with accompanying wine glasses.
    Permanent tribulation.
    """, attrs=["bold"]))
    # ? frank alive in room ^

    def bedroomKillerThere():
        
        inventoryUseable = str(inventory)
        
        sancheck = int(sanity[0])
        
        knifeCheck = re.search("knife", inventoryUseable)
        
        pistolCheck = re.search("pistol", inventoryUseable)
    
        print(colored("""
You move closer to the left door, stepping on the mixture of food and blood while turning the knob and pulling it towards you..
        """, attrs=["bold"]))
        
        heIsThere = """
        He is there He is there He is there He is there He is there He is there He is there He is there He is there He is there He is there 
        He is there He is there He is there He is there He is there He is there He is there He is there He is there He is there He is there 
        He is there He is there He is there He is there He is there He is there He is there He is there He is there He is there He is there 
        He is there He is there He is there He is there He is there He is there He is there He is there He is there He is there He is there 
        He is there He is there He is there He is there He is there He is there He is there He is there He is there He is there He is there"""
            
        time.sleep(4)
            
        print(heIsThere)
        time.sleep(0.5)
        print(heIsThere)
        time.sleep(0.5)
        print(heIsThere)
        time.sleep(0.5)
        print(heIsThere)
        time.sleep(0.5)
        print(heIsThere)
        time.sleep(0.5)
        print(heIsThere)
        time.sleep(0.5)
        
        blankspace()
            
        if knifeCheck or pistolCheck:
            
            if sancheck <= 10:
                
                death()
                
            elif sancheck > 10:
                
                incapicatate()
                
        else:
            
            death()
        
    def kitchenKillerThere():
        
        inventoryUseable = str(inventory)
        
        sancheck = int(sanity[0])
        
        knifeCheck = re.search("knife", inventoryUseable)
        
        pistolCheck = re.search("pistol", inventoryUseable)
    
        print(colored("""
You move closer to the right door, stepping on the mixture of food and blood while turning the knob and pulling it towards you..
        """, attrs=["bold"]))
        
        heIsThere = """
        He is there He is there He is there He is there He is there He is there He is there He is there He is there He is there He is there 
        He is there He is there He is there He is there He is there He is there He is there He is there He is there He is there He is there 
        He is there He is there He is there He is there He is there He is there He is there He is there He is there He is there He is there 
        He is there He is there He is there He is there He is there He is there He is there He is there He is there He is there He is there 
        He is there He is there He is there He is there He is there He is there He is there He is there He is there He is there He is there"""
            
        time.sleep(4)
            
        print(heIsThere)
        time.sleep(0.5)
        print(heIsThere)
        time.sleep(0.5)
        print(heIsThere)
        time.sleep(0.5)
        print(heIsThere)
        time.sleep(0.5)
        print(heIsThere)
        time.sleep(0.5)
        print(heIsThere)
        time.sleep(0.5)
        
        blankspace()
        
        if knifeCheck or pistolCheck:
            
            if sancheck <= 10:
                
                death()
                
            elif sancheck > 10:
                
                incapicatate()

        else:
            
            death()
    
    def livingRoomKillerThere():
        
        inventoryUseable = str(inventory)
        
        sancheck = int(sanity[0])
        
        knifeCheck = re.search("knife", inventoryUseable)
        
        pistolCheck = re.search("pistol", inventoryUseable)
    
        print(colored("""
You move closer to the middle door, stepping on the mixture of food and blood while turning the knob and pulling it towards you..
        """, attrs=["bold"]))
        
        heIsThere = """
        He is there He is there He is there He is there He is there He is there He is there He is there He is there He is there He is there 
        He is there He is there He is there He is there He is there He is there He is there He is there He is there He is there He is there 
        He is there He is there He is there He is there He is there He is there He is there He is there He is there He is there He is there 
        He is there He is there He is there He is there He is there He is there He is there He is there He is there He is there He is there 
        He is there He is there He is there He is there He is there He is there He is there He is there He is there He is there He is there"""
            
        time.sleep(4)
            
        print(heIsThere)
        time.sleep(0.5)
        print(heIsThere)
        time.sleep(0.5)
        print(heIsThere)
        time.sleep(0.5)
        print(heIsThere)
        time.sleep(0.5)
        print(heIsThere)
        time.sleep(0.5)
        print(heIsThere)
        time.sleep(0.5)
        
        blankspace()
        
        if knifeCheck or pistolCheck:
            
            if sancheck <=10:
                
                death()
                
            elif sancheck > 10:
                
                incapicatate()

        else:
            
            death()
    
    saveState = open(saveStateLocation, "r")
    
    saveContent = saveState.read()
    
    saveState.close()
    
    continueCheck = re.search("True", saveContent)
    
    if continueCheck:
        
        print("")
        
        print("Loaded successfully!")
        
        print("")
        
    else:
    
        print(startingPrompt)
        inventory.append("rusty necklace")

    def roomOne(): # ? ROOM ONE
        
        # ? Area prompt:
        """
    You awake, a neverending coma within a neverending nightmare ceases and your eyes dart around the room: a whole section of a wall covered in blood,
    newspaper all across the windows, a luxurious red rug covering a large majority of the room, and expansive bookshelves.
    The most unusual being a flipped over mahogany desk which brought papers, feathers, an ink pot, and a small burgandy box along with it when it fell.
    After gathering that this room is a study you raise yourself and attempt to mentally prepare for what's ahead. Tribulation begins. 
        """
    
        userInput = input(colored("What do you want to do? (type help for a list of commands): ", f"{theme}", attrs=["bold"])).lower()
            
        pickUpAction = re.search("pick up+", userInput)
        
        lookAtAction = re.search("look at+", userInput)
        
        goToTheAction1 = re.search("go", userInput)
        
        goToTheAction2 = re.search("to", userInput)
        
        useAction = re.search("use+", userInput)
        
        useWithAction = re.search("with+", userInput)
            
        if userInput == "help":
                
            print(help)
                
            roomOne()
            
        elif userInput == "inventory":
            
            print("")
            
            print("You have:")
            
            print("")
            
            for items in inventory:
                print(items)
            
            print("")
            
            roomOne()
            
        elif userInput == "save":
            
            save()
            
        elif userInput == "prompt":
            
            print(startingPrompt)
            
            roomOne()
            
        elif userInput == "exit":
            
            exitCheck.append("exit")
            save()
            
        elif userInput == "clear":
            
            blankspace()
                
            roomOne()
            
        elif userInput == "restart":
            
            game()
            
        elif userInput == "menu":
            
            startMenu()
            
        elif lookAtAction:
            
            lookAtDoor = re.search("door+", userInput)
            
            lookAtRug = re.search("rug+", userInput)
            
            lookAtHatch = re.search("hatch", userInput)
            
            lookAtBookshelves = re.search("bookshelves", userInput)
                
            lookAtBookshelfAlternative = re.search("bookshelf", userInput)
    
            lookAtDesk = re.search("desk", userInput)
            
            lookAtInkPot1 = re.search("ink", userInput)
            
            lookAtInkPot2 = re.search("pot", userInput)
            
            lookAtPaper = re.search(r"\bpaper\b", userInput)
            
            lookAtDrawer = re.search("drawer", userInput)
            
            lookAtBlood = re.search("blood+", userInput)
            
            lookAtBox = re.search("box+", userInput)
            
            lookAtMattress = re.search("mattress+", userInput)
            
            lookAtWindows = re.search("window", userInput)
            
            lookAtFloor = re.search("floor", userInput)
            
            lookAtWalls = re.search("wall", userInput)
            
            lookAtRustyNecklace = re.search("necklace", userInput)
            
            lookAtMyself = re.search(r"\bself\b", userInput)
            
            lookAtMyselfAlternative = re.search("myself", userInput)
            
            lookAtFeathers = re.search("feather", userInput)
            
            lookAtNewspaper = re.search("newspaper+", userInput)
            
            lookAtBody = re.search("body", userInput)
            
            lookAtCorpseAlternative = re.search("corpse", userInput)
            
            lookAtConstellation = re.search("constellation", userInput)
            
            lookAtPoliceUniform = re.search("uniform", userInput)
            
            if lookAtDoor:
                
                print("")
                
                print("The door is pristine with an accompanying pristine keyhole, and it looks sturdy, it most likely couldn't be brute forced.") 
                
                print("")
                
                roomOne()   
                
            elif lookAtMattress:
                
                print("")
                
                print("The mattress seems to be very old, there are springs sticking out of it, and it sure did a number on your back.")
                
                print("")
                
                roomOne()
                
            elif lookAtRug:
                
                interactionSaveUseable = str(interactionSave)
                
                rugMovedCheck = re.search("rugMoved", interactionSaveUseable)
                
                if rugMovedCheck:
                    
                    print("")
                    
                    print("The rolled up rug in the corner of the room revealed a hatch underneath")
                    
                    print("")
                    
                    roomOne()
                    
                else:
                
                    print("""
The luxurious rug in the center of the room is a dark red with golden swirls all around it.
It isn't stuck to the floor in any way, and could likely be moved.
                    """)
                    
                    roomOne()  
                    
            elif lookAtHatch:
                
                interactionSaveUseable = str(interactionSave)
                
                hatchOpenedCheck = re.search("hatchOpened", interactionSaveUseable)
                
                rugMovedCheck = re.search("rugMoved", interactionSaveUseable)
                
                if hatchOpenedCheck:
                    
                    print("")
                    
                    print("The opened hatch revealed a rusty key beneath it's door, and is waiting to be picked up.")
                    
                    print("")
                    
                    roomOne()
                
                elif rugMovedCheck:
                    
                    print("")
                    
                    print("There is a small hatch within the floor that was revealed by moving the opulent rug to the side.")
                    
                    print("")
                    
                    roomOne()

                else:
                    
                    print("")
                    
                    print("There is no hatch to look at")
                    
                    print("")
                    
                    roomOne()                    
                    
            elif lookAtBookshelves or lookAtBookshelfAlternative:
                
                print("")
                
                print("The grand bookcase contains an incredible amount of books, head to toe covering a whole wall")
                
                print("")
                
                roomOne()
                
            elif lookAtDesk:

                print("""
You look at the thrown old mahogany desk closer. It brought dry feathers with an ink pot, some blank paper, and a small burgandy box with it when it fell. 
The desk also has a drawer with no conventional handle, which might be worth taking a closer look at. You notice a sharp weapon's marks on some of the edges,
it looks like there was a fight here. The wall behind the desk has blood all over it. 
                """)
                
                roomOne()
                
            elif lookAtInkPot1 or lookAtInkPot2:
                
                print("")
                
                print("The ink in the pot is dry, and couldn't be used")
                
                print("")
                
                roomOne()
                
            elif lookAtPaper:
                
                interactionSaveUseable = str(interactionSave)
                
                paperGotCheck = re.search("paperGot", interactionSaveUseable)
                
                if paperGotCheck:
                    
                    print("")
                    
                    print("The paper in your pocket is blank, and could be written on if you had a writing intermediary.")
                    
                    print("")
                    
                    roomOne()
                    
                else:
                
                    print("")
                    
                    print("There is blank paper on the floor. If you had some ink or an equivalent of ink for the feathers nearby you could write on it.")
                    
                    print("")
                    
                    roomOne()
                
            elif lookAtDrawer:
                
                print("""
The drawer in the desk doesn't have a handle, or much of anything, other than a constellation pattern, which seems to have multiple missing stars:

  *--- 
  |    \\
    --*   
       \\
        \\
         *
        /
       /
      *
     /
    *
   /           *
  /
 /
*        

Ominous.
                """)
                
                roomOne()
        
            elif lookAtBlood:
                
                print("")
                
                print("The blood is still dripping down the wall behind the desk, looks like it's fresh, and might be able to be used with something")      
                
                print("")
                
                sanchange = int(sanity[0])
                        
                sanchange += 2
                
                sanity.clear()
                
                sanity.append(sanchange)
                
                roomOne()
                
            elif lookAtBox:
                
                print("")
                
                print("A burgandy box lies on top of scattered papers and feathers from when the desk was thrown. It has a rusty keyhole.")
                
                print("")
                
                roomOne()
                
            elif lookAtWindows:
                
                print("")
                
                print("The windows are covered in old newspaper articles, dated April 3rd, 1956")
                
                print("")
                
                roomOne()
                
            elif lookAtFloor:
                
                print("")
                
                print("The floors are wooden and creaky, a section of the floor looks like it's had an axe driven right into it. The back of the room has a fallen desk on the floor.")
                
                print("")
                
                roomOne()
                
            elif lookAtWalls:
                
                print("""
The walls are made out of sturdy logs, and they're certainly not in their prime, the wood seems to have been chipped time and time again,
there's a blood splatter on one side.
                """)
                
                roomOne()
                
            elif lookAtRustyNecklace:
                
                print("")
                
                print("There is a rusty necklace around your neck, it doesn't have a lock and looks like it can be opened")
                
                print("")
                
                roomOne()
                
            elif lookAtFeathers:
                
                interactionSaveUseable = str(interactionSave)
                
                featherGotCheck = re.search("featherGot", interactionSaveUseable)
                
                if featherGotCheck:
                    
                    print("")
                    
                    print("The feather in your pocket has a very sharp tip, and was most likely used for writing, but you need some form of liquid to write.")
                    
                    print("")
                    
                    roomOne()
                
                else:
                
                    print("")
                    
                    print("There are a bundle of feathers on the floor, with sharp tips at the end")
                    
                    print("")
                    
                    roomOne()
                
            elif lookAtNewspaper:

                print("")
                
                print("There are a mass amount of newspapers covering the windows for one side of the whole room")
                
                print("")
                
                roomOne()
                
            elif lookAtMyself or lookAtMyselfAlternative:
                
                print("""
You look down at yourself, your hands are bruised and see signs of wear, you're wearing a ripped up suit with no tie,
you can't seem to remember anything, and you feel woozy, as if drunk.
                """)
                
                roomOne()
                
            elif lookAtBody or lookAtCorpseAlternative:
                
                interactionSaveUseable = str(interactionSave)
                
                doorOpenedCheck = re.search("doorOpened", interactionSaveUseable)
                
                bodyFlippedCheck = re.search("bodyFlipped", interactionSaveUseable)
                
                sancheck = int(sanity[0])
                
                if sancheck >= 7:
                    
                    sanityeventsUseable = str(sanityevents)
                    
                    bodyEventCheck = re.search("bodyEvent", sanityeventsUseable)
                    
                    if bodyEventCheck:
                        
                        pass
                    
                    else:
                    
                        blankspace()
                        
                        bodyEvent = """
        Help me Help me Help me Help me Help me Help me Help me Help me Help me Help me Help me Help me Help me Help me Help me 
        Help me Help me Help me Help me Help me Help me Help me Help me Help me Help me Help me Help me Help me Help me Help me 
        Help me Help me Help me Help me Help me Help me Help me Help me Help me Help me Help me Help me Help me Help me Help me 
        Help me Help me Help me Help me Help me Help me Help me Help me Help me Help me Help me Help me Help me Help me Help me 
                        """
                    
                        time.sleep(2)
                        
                        print(bodyEvent)
                        time.sleep(0.5)
                        print(bodyEvent)
                        time.sleep(0.3)
                        print(bodyEvent)
                        time.sleep(0.1)
                        print(bodyEvent)
                        time.sleep(0.3)
                        
                        blankspace() 
                        
                        sanityevents.append("bodyEvent")
                
                if doorOpenedCheck:
                    
                    if bodyFlippedCheck:

                        print("""
You look back at the flipped body, this person feels familiar upon closer examination, so does the constellation and the uniform.
But you knew that, didn't you?
                        """)
                        
                        roomOne()
                        
                    else:
                    
                        print("""
You flip the corpse around and immediately something strikes you, a constellation pattern on the forehead of the victim,
and a police uniform. It looks like he was strangled and recently, he's still warm. 
                        """)
                        
                        interactionSave.append("bodyFlipped")
                        
                        sanchange = int(sanity[0])
                        
                        sanchange += 4
                        
                        sanity.clear()
                        
                        sanity.append(sanchange)
                        
                        roomOne()
                    
                else: 
                    
                    print("")
                    
                    print("There is no body to look at")
                    
                    print("")
                
                    roomOne()
                    
            elif lookAtConstellation:
                
                interactionSaveUseable = str(interactionSave)
                
                bodyFlippedCheck = re.search("bodyFlipped", interactionSaveUseable)
                
                sancheck = int(sanity[0])
                
                if bodyFlippedCheck:
                    
                    if sancheck >= 12:
                        
                        sanityeventsUseable = str(sanityevents)
                        
                        constellationEventCheck = re.search("constellationEvent", sanityeventsUseable)
                        
                        if constellationEventCheck:
                            
                            pass
                        
                        else:
                    
                            blankspace()
                                
                            constellationEvent = """
        ✦ 　　　　　　　         　        　　　　 　　 　　　　　　　 　　　　　.　　　　　　　　　　　　　　　　　　.　　　 　　　˚　　　　　　　　　　　　　　    　　
        . 　 　　　　　.　　　　 　　　　　   　　　　　.　　　　　　　　　　　.　　　　　　　　　　  　　　* .　　　　　 　　　　　　　　　　　　　　.　　　　　　　　　　 ✦
        　　　　 　 　˚　　 . ✦ ✦　　　　　　　　　　　　　　　　　　　ﾟ　　　　　.　　　　　　　　　　　　　　　. 　　 　  ,　 　　　　　　　　　　　　　　  　　　　
        　　   　　　　　　　　　　　　　　　.　　　　　　　　　　　　　　 ✦ .　　　　　　　　　　 ✦ 　　　　   　 　　　˚　　　　　　　　　　　　　　　　　　　　   
        　　　　　　　　　　　　　.　　　　　　　　　　　 　　　. 　　 　　　　　　　 ✦ 　　　　　　　　　　 　 　　　　 　　　　　　　　　　　　,　　   　 .　　　　　　
        　　　　　　　.　　　ﾟ　  　　　.　　　　　　　　　　　　　✦ 　　　　　　,　　　　　　　.　　　　　　    　　　　 　　　　　　　　　　　　　　　　　　  .  　　　
        　　　　　　　　　　　　　　　    　      　　　　　        　　　　　　　　　　　　　. 　　　　　　　　.　　　　　　　　　　　　　.　　　　　　       　   　　　　 　　　
        　　　　　　　　　　　　　       　   　　　　　　　　　　　　　　　　       　    ✦ 　   　　　,　　　　　　　　　　　  　　　　 　　,　　　 　 　　　　　　　　　　　　.　
        　　　　 　　 　　　.　　　　　　　　　　　　　 　           　　　　　　　　　　　　　　　　　　　. ˚　　　 　   . ,　　　　　　　　　　　       　    　　　　　　　　　　　
        　　. .　　　  　　    ✦　 ✦　　　　 　　　　　.　　　　　　　　　　　　　.　　　　　　　　　　　　　　　 　　   　　　　　 ✦"""
                    
                            time.sleep(4)
                            
                            print(constellationEvent)
                            time.sleep(0.2)
                            print(constellationEvent)
                            time.sleep(0.1)
                            print(constellationEvent)
                            time.sleep(3)
                            print("")
                            print("Aren't they beautiful, Chris?")
                            print("")
                            
                            time.sleep(2.3)
                            
                            sanityevents.append("constellationEvent")
                            
                            blankspace()
                    
                    print("""
  *---* 
  |    \\
   *--*   
       \\
        \\
         *
        /
     * /
      *
     /
    *
   /           *
  /
 /
*   *     
                    """)
                    
                    sanchange = int(sanity[0])
                        
                    sanchange += 1
                    
                    sanity.clear()
                    
                    sanity.append(sanchange)
                    
                    roomOne()
                    
                else:
                    
                    print("")
                    
                    print("There is no body to look at")
                    
                    print("")
                    
                    roomOne()
                    
            elif lookAtPoliceUniform:
                
                interactionSaveUseable = str(interactionSave)
                
                bodyFlippedCheck = re.search("bodyFlipped", interactionSaveUseable)
                
                if bodyFlippedCheck:
                    
                    print("")
                    
                    print("Jamestown Police, badge number 14P2")
                    
                    print("")
                    
                    roomOne()
                    
                else:
                    
                    print("")
                    
                    print("There is no uniform to look at")
                    
                    print("")
                    
                    roomOne()
                
            else:
                
                print("")
                
                print("You can't look at that")
                
                print("")
                
                roomOne()
        
        elif goToTheAction1 and goToTheAction2:
            
            goToTheSecondRoom = re.search("second", userInput)
            
            goToTheSecondRoomAlternative1 = re.search("hallway", userInput)
            
            goToTheThirdRoom = re.search("third", userInput)
            
            goToTheThirdRoomAlternative1 = re.search("bedroom", userInput)
            
            goToTheThirdRoomAlternative2 = re.search("left", userInput)
            
            goToTheFourthRoom = re.search("fourth", userInput)
            
            goToTheFourthRoomAlternative1 = re.search("kitchen", userInput)
            
            goToTheFourthRoomAlternative2 = re.search("right", userInput)
            
            goToTheFifthRoom = re.search("fifth", userInput)
            
            goToTheFifthRoomAlternative1 = re.search("living room", userInput)
            
            goToTheFifthRoomAlternative2 = re.search("middle", userInput)
            
            goToDoor = re.search("door", userInput)
            
            goToRoom = re.search("room", userInput)
            
            if goToTheSecondRoom and goToRoom or goToTheSecondRoomAlternative1 or goToDoor:
                
                interactionSaveUseable = str(interactionSave)
                
                doorOpenedCheck = re.search("doorOpened", interactionSaveUseable)
                
                if doorOpenedCheck:
                    
                    mapBeenUseable = str(mapBeen)
                    
                    secondBeenCheck = re.search("secondBeen", mapBeenUseable)
                    
                    if secondBeenCheck:
                        
                        print(colored("""
    You move back into the second room, the hallway is so quiet that it makes you uneasy
                    """, attrs=["bold"]))
                        
                        mapState.clear()
                        
                        mapState.append("2")
                        
                        sanchange = int(sanity[0])
                        
                        sanchange += 1
                        
                        sanity.clear()
                        
                        sanity.append(sanchange)
                        
                        roomTwo()
                        
                    else:
                    
                        print(hallwayPrompt)
                        
                        mapState.clear()
                        
                        mapState.append("2")
                        
                        mapBeen.append("secondBeen")
                        
                        roomTwo()
                    
                else:
                    
                    print("")
                    
                    print("The door is not open")
                    
                    print("")
                    
                    roomOne()
                    
            elif goToTheThirdRoom and goToRoom or goToTheThirdRoomAlternative2 and goToDoor or goToTheThirdRoomAlternative1:
                
                mapBeenUseable = str(mapBeen)
                
                interactionSaveUseable = str(interactionSave)
                
                thirdBeenCheck = re.search("thirdBeen", mapBeenUseable)
                
                doorOpenedCheck = re.search("doorOpened", interactionSaveUseable)
                
                starLocation3Check = re.search("location3", interactionSaveUseable)
                
                if doorOpenedCheck:
                
                    if thirdBeenCheck:
                        
                        print(colored("""
    You move back into the third room, its unusual homeliness makes you increasingly uneasy when compared to the atrocities previously seen.
                        """, attrs=["bold"]))
                            
                        mapState.clear()
                        
                        mapState.append("3")
                        
                        sanchange = int(sanity[0])
                        
                        sanchange += 1
                        
                        sanity.clear()
                        
                        sanity.append(sanchange)
                    
                        roomThree()
                        
                    elif starLocation3Check:
                        
                        interactionSaveUseable = str(interactionSave)
                        
                        bedroomKillerAliveCheck = re.search("bedroomKillerAlive", interactionSaveUseable)
                        
                        bedroomKillerDeadCheck = re.search("bedroomKillerDead", interactionSaveUseable)
                        
                        if bedroomKillerAliveCheck or bedroomKillerDeadCheck:
                            
                            mapState.clear()
                            
                            mapState.append("3")
                            
                            print(colored("""
    You move back into the bedroom, its unusual homeliness makes you increasingly uneasy when compared to the atrocities previously seen
                        """, attrs=["bold"]))
                            
                            roomThree()
                            
                        else:
                    
                            mapState.clear()
                            
                            mapState.append("3")
                            
                            mapBeen.append("thirdBeen")
                            
                            bedroomKillerThere()
                        
                    else:
                        
                        print(bedroomKillerNotThere)
                        print("")
                        mapState.clear()
                        mapState.append("3")
                        mapBeen.append("secondBeen")
                        mapBeen.append("thirdBeen")
                        roomThree()
                    
                else:
                    
                    print("")
                    
                    print("The door is not open")
                    
                    print("")
                    
                    roomOne()
                    
            elif goToTheFourthRoom and goToRoom or goToTheFourthRoomAlternative2 and goToDoor or goToTheFourthRoomAlternative1:
                
                mapBeenUseable = str(mapBeen)
                
                interactionSaveUseable = str(interactionSave)
                
                fourthBeenCheck = re.search("fourthBeen", mapBeenUseable)
                
                doorOpenedCheck = re.search("doorOpened", interactionSaveUseable)
                
                starLocation4Check = re.search("location4", interactionSaveUseable)
                
                if doorOpenedCheck:
                
                    if fourthBeenCheck:
                        
                        print(colored("""
    You move back into the kitchen, the horrific sight and smell freeze your body stone cold before continuing onward.
                        """, attrs=["bold"]))
                            
                        mapState.clear()
                        
                        mapState.append("4")
                    
                        roomFour()
                    
                    elif starLocation4Check:
                        
                        interactionSaveUseable = str(interactionSave)
                        
                        kitchenKillerAliveCheck = re.search("kitchenKillerAlive", interactionSaveUseable)
                        
                        kitchenKillerDeadCheck = re.search("kitchenKillerDead", interactionSaveUseable)
                        
                        if kitchenKillerAliveCheck or kitchenKillerDeadCheck:
                            
                            mapState.clear()
                            
                            mapState.append("4")
                            
                            print(colored("""
    You move back into the kitchen, the horrific sight and smell freeze your body stone cold before continuing onward.
                        """, attrs=["bold"]))
                            
                            roomFour()
                            
                        else:
                    
                            mapState.clear()
                            
                            mapState.append("4")
                            
                            mapBeen.append("fourthBeen")
                            
                            kitchenKillerThere()
                        
                    else:
                        
                        print(kitchenKillerNotThere)
                        print("")
                        mapState.clear()
                        mapState.append("4")
                        mapBeen.append("secondBeen")
                        mapBeen.append("fourthBeen")
                        roomFour()
                    
                else:
                    
                    print("")
                    
                    print("The door is not open")
                    
                    print("")
                    
                    roomOne()
                    
            elif goToTheFifthRoom and goToRoom or goToTheFifthRoomAlternative2 and goToDoor or goToTheFifthRoomAlternative1:
                
                mapBeenUseable = str(mapBeen)
                
                interactionSaveUseable = str(interactionSave)
                
                fifthBeenCheck = re.search("fifthBeen", mapBeenUseable)
                
                wardrobeMovedTrolleyCheck = re.search("wardrobeMovedTrolley", interactionSaveUseable)
                
                starLocation5Check = re.search("location5", interactionSaveUseable)
                
                if wardrobeMovedTrolleyCheck:
                
                    if fifthBeenCheck:
                        
                        print(colored("""
    You move back into living room, your body wishes to leave and never look back.
                        """, attrs=["bold"]))
                            
                        mapState.clear()
                        
                        mapState.append("5")
                    
                        roomFour()
                    
                    elif starLocation5Check:
                        
                        interactionSaveUseable = str(interactionSave)
                        
                        livingRoomKillerAliveCheck = re.search("livingRoomKillerAlive", interactionSaveUseable)
                        
                        livingRoomKillerDeadCheck = re.search("livingRoomKillerDead", interactionSaveUseable)
                        
                        if livingRoomKillerAliveCheck or livingRoomKillerDeadCheck:
                            
                            mapState.clear()
                            
                            mapState.append("5")
                            
                            print(colored("""
    You move back into living room, your body wishes to leave and never look back.
                        """, attrs=["bold"]))
                            
                            roomFive()
                            
                        else:
                    
                            mapState.clear()
                            
                            mapState.append("5")
                            
                            mapBeen.append("fifthBeen")
                            
                            livingRoomKillerThere()
                        
                    else:
                        
                        print(livingRoomKillerNotThere)
                        mapState.clear()
                        mapState.append("5")
                        mapBeen.append("secondBeen")
                        mapBeen.append("thirdBeen")
                        mapBeen.append("fourthBeen")
                        mapBeen.append("fifth")
                        roomFive()
                    
                else:
                    
                    print("")
                    
                    print("The wardrobe is in the way")
                    
                    print("")
                    
                    roomOne()
                    
            else:
                
                print("")
                
                print("You can't go to that")
                
                print("")
                
                roomOne()
        
        elif useWithAction:
            
            usePristineKeyWithDoor1 = re.search("pristine", userInput)
            
            usePristineKeyWithDoor2 = re.search("door", userInput)
            
            useKeyWithDoor1 = re.search("pristine key", userInput)
            
            useKeyWithDoor2 = re.search("door", userInput)
            
            useKeyWithBox1 = re.search("key", userInput)
            
            useKeyWithBox2 = re.search("box", userInput)
            
            useFeatherWithBlood1 = re.search("feather+", userInput)
            
            useFeatherWithBlood2 = re.search("blood", userInput)
            
            useQuillWithPaper1 = re.search("quill", userInput)
            
            useQuillWithPaper2 = re.search("paper", userInput)
            
            if usePristineKeyWithDoor1 and usePristineKeyWithDoor2:
                
                inventoryUseable = str(inventory)
                
                hasPristineKeyCheck = re.search("pristine key", inventoryUseable)
                
                if hasPristineKeyCheck:
                    
                    interactionSaveUseable = str(interactionSave)
                    
                    doorOpenedCheck = re.search("doorOpened", interactionSaveUseable)
                    
                    if doorOpenedCheck:
                        
                        print("")
                        
                        print("The door is already open, and the hallway awaits.")
                        
                        print("")
                        
                        roomOne()
                        
                    else:
                    
                        print("")
                        
                        print("""
You insert the bigger pristine key into the door and it fits perfectly,
fading groans come from behind the door as the lock clicks, you open the door inwards and...
                        """)
                        
                        time.sleep(6.5)
                        
                        print(colored("""
▄▄▄▄    ▒█████   ▒█████   ███▄ ▄███▓ ▐██▌ 
▓█████▄ ▒██▒  ██▒▒██▒  ██▒▓██▒▀█▀ ██▒ ▐██▌ 
▒██▒ ▄██▒██░  ██▒▒██░  ██▒▓██    ▓██░ ▐██▌ 
▒██░█▀  ▒██   ██░▒██   ██░▒██    ▒██  ▓██▒ 
░▓█  ▀█▓░ ████▓▒░░ ████▓▒░▒██▒   ░██▒ ▒▄▄  
░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░   ░  ░ ░▀▀▒ 
▒░▒   ░   ░ ▒ ▒░   ░ ▒ ▒░ ░  ░      ░ ░  ░ 
░    ░ ░ ░ ░ ▒  ░ ░ ░ ▒  ░      ░       ░ 
░          ░ ░      ░ ░         ░    ░    
    ░                                    
                        """, f"{theme}", attrs=["bold"]))
                        
                        time.sleep(2.1)
                        
                        print("""
A corpse which was leaning against the door collapses onto the floor as you open it,
the body stays flat on the ground as your heart beats faster,
you go cold and warm at the same time, the hair on your neck standing up.
Footsteps get quieter and quieter, and the hallway, awaits.

(type: "go to second room" etc to go to different room if the means of entrance are unlocked).
                        """)
                        
                        interactionSave.append("doorOpened")
                        
                        sanchange = int(sanity[0])
                        
                        sanchange += 3
                        
                        sanity.clear()
                        
                        sanity.append(sanchange)
                        
                        roomOne()
                        
                else:
                    
                    print("")
                    
                    print("You don't have a pristine key to use with the door")
                    
                    print("")
                    
                    roomOne()
            
            elif useKeyWithDoor1 and useKeyWithDoor2:
                
                inventoryUseable = str(inventory)
                
                hasKeyCheck = re.search("key", inventoryUseable)
                
                if hasKeyCheck:
                
                    print("")
                    
                    print("You attempt to put the key into the keyhole of the door but it doesn't fit")
                    
                    print("")
                    
                    roomOne()
                    
                else:
                    
                    print("")
                    
                    print("You do not have a key to use with this door")
                    
                    print("")
                    
                    roomOne()
                    
            elif useKeyWithBox1 and useKeyWithBox2:
                
                inventoryUseable = str(inventory)
                
                hasKeyCheck = re.search("key", inventoryUseable)
                
                if hasKeyCheck:
                    
                    interactionSaveUseable = str(interactionSave)
                    
                    boxOpenedCheck = re.search("boxOpened+", interactionSaveUseable)
                    
                    if boxOpenedCheck:
                        
                        print("")
                        
                        print("You have already opened the box")
                        
                        print("")
                        
                        roomOne()
                        
                    else:

                        print("""
You fit the key into the hole of the box and turn slowly, it opens!
As you lift open the top of the box a scream rings out in the next room and the loud thud comes from the door.
You see a bigger, pristine key in the box, while taking your rusty key out of the box and placing it back in your pocket.
                        """)
                        
                        interactionSave.append("boxOpened")
                        
                        sanchange = int(sanity[0])
                        
                        sanchange += 2
                        
                        sanity.clear()
                        
                        sanity.append(sanchange)
                        
                        roomOne()
                    
                else:
                    
                    print("")
                    
                    print("You do not have a key to use with this box")
                    
                    print("")
                    
                    roomOne()
                    
            elif useFeatherWithBlood1 and useFeatherWithBlood2:
                
                interactionSaveUseable = str(interactionSave)
                
                quillMadeCheck = re.search("quillMade", interactionSaveUseable)
                
                if quillMadeCheck:
                    
                    print("")
                    
                    print("You have already made the quill")
                    
                    print("")
                    
                    roomOne()
                    
                else:
                    
                    print("")
                    
                    print("You scrape the tip of the feather against the fresh blood, you have made a makeshift quill with ink")
                    
                    print("")
                    
                    interactionSave.append("quillMade")
                    
                    inventory.append("quill")
                    
                    findFeather = inventory.index("feather")
                    
                    inventory.pop(findFeather)
                    
                    sanchange = int(sanity[0])
                        
                    sanchange += 1

                    sanity.clear()

                    sanity.append(sanchange)
                    
                    roomOne()
                    
            elif useQuillWithPaper1 and useQuillWithPaper2:
                
                inventoryUseable = str(inventory)
                
                quillGotCheck = re.search("quill", inventoryUseable)
                
                paperGotCheck = re.search("paper", inventoryUseable)
                
                if quillGotCheck and paperGotCheck:
                    
                    print("")
                    
                    print("You draw a map of your surroundings, and place it in your pocket for future reference")
                    
                    print("")
                    
                    inventory.append("map")
                    
                    mapState.clear()
                    
                    mapState.append("1")
                    
                    interactionSave.append("mapMade")
                    
                    sanchange = int(sanity[0])

                    sanchange += 1

                    sanity.clear()

                    sanity.append(sanchange)

                    roomOne()
                    
                elif quillGotCheck:
                    
                    print("")
                    
                    print("You don't have a piece of paper")
                    
                    print("")
                    
                    roomOne()
                    
                elif paperGotCheck:
                    
                    print("")
                    
                    print("You don't have a quill")
                    
                    print("")
                    
                    roomOne()
                    
                else:
                    
                    print("")
                    
                    print("You don't have a quill or paper")
                    
                    print("")
                    
                    roomOne()
                    
            else:
                
                print("")
                
                print("You can't use that with that")
                
                print("")
                
                roomOne()

        elif useAction:
            
            useDoor = re.search("door+", userInput)
            
            useRug = re.search("rug+", userInput)
            
            useHatch = re.search("hatch", userInput)
    
            useOmnipotentAlternative = re.search("omnipotent", userInput)
            
            useWindows = re.search("window", userInput)
            
            useBox = re.search("box", userInput)
            
            useRustyNecklace = re.search("necklace", userInput)
            
            useMap = re.search("map", userInput)
            
            useNewspaper = re.search("newspaper", userInput)
            
            if useDoor:
                
                print("")
                
                print("You turn the door knob but to no avail, it's locked, maybe you should keep looking around")
                
                print("")
                
                roomOne()
                
            elif useRug:
                
                interactionSaveUseable = str(interactionSave)
                
                rugMovedCheck = re.search("rugMoved", interactionSaveUseable)
                
                if rugMovedCheck:
                    
                    print("")
                    
                    print("You have already moved the rug to the side")
                    
                    print("")
                    
                    roomOne()
                    
                else:
                    
                    print("")
                    
                    print("You roll up the rug and put it in a corner, a small unlocked hatch reveals itself and could be opened")
                    
                    print("")
                    
                    interactionSave.append("rugMoved")
                    
                    roomOne()
                
            elif useHatch:
                
                interactionSaveUseable = str(interactionSave)
                
                rugMovedCheck = re.search("rugMoved", interactionSaveUseable)
                
                hatchOpenedCheck = re.search("hatchOpened", interactionSaveUseable)
                
                if rugMovedCheck:
                    
                    if hatchOpenedCheck:
                        
                        print("")
                        
                        print("You have already opened the hatch")
                        
                        print("")
                        
                        roomOne()
                        
                    else:
                    
                        print("")
                        
                        print("You open the hatch and a small rusty key is inside, if you pick this up you might be able to use it with something")
                        
                        print("")
                        
                        interactionSave.append("hatchOpened")
                        
                        roomOne()

                else:
                    
                    print("")
                    
                    print("There is no hatch to open")
                    
                    print("")
                    
                    roomOne()
            
            elif useWindows:
                
                sancheck = int(sanity[0])
                
                if sancheck >= 13:
                    
                    print("")
                    
                    print("The corpses of your partners are outside. They died because you failed them, Mike.")
                    
                    print("")
                    
                    roomOne()
                    
                else:

                    print("""
After tearing a piece of the newspaper off the windows you get to see a glimpse of the outside,
although the windows barred and the outside pitch black, it looks like a snowy location,
vast trees as far as your limited vision can see, and no lights anywhere in the distance. You're stranded.
                    """)
                
                    sanchange = int(sanity[0])
        
                    sanchange += 2

                    sanity.clear()

                    sanity.append(sanchange)
                    
                    roomOne()
                
            elif useBox:
                
                interactionSaveUseable = str(interactionSave)
                
                boxOpenedCheck = re.search("boxOpened+", interactionSaveUseable)
                
                if boxOpenedCheck:
                    
                    print("")
                    
                    print("The box is already opened")
                    
                    print("")
                    
                    roomOne()
                    
                else:
                    
                    print("")
                    
                    print("You attempt to open the box but it's locked, a rusty keyhole catches your eye, looks like you need a key for this")
                    
                    print("")
                    
                    roomOne()
                    
            elif useRustyNecklace:
                
                print("")
                
                print("You open the rusty necklace on your neck and see a picture of what you think is you and 2 children, it puts you at ease")
                
                print("")
                
                sanchange = int(sanity[0])
    
                sanchange -= 2

                sanity.clear()

                sanity.append(sanchange)
                
                roomOne()
                
            elif useMap:
                
                mapUse()
                
            elif useNewspaper:
                
                print("""
The closest newspaper towards you is an issue of the \'Jamestown Daily News\' dated April 3rd 1956, the headline reads:
"Constellation killer still out there, lock your door", the rest of the issue tells of a string of 21 killings, constellation marks on the forehead,
and a missing group of policemen.
                """)
                
                roomOne()
                
            else:
                
                print("")
                
                print("You can't use that")
                
                print("")
                
                roomOne()
        
        elif pickUpAction:
            
            pickUpKey = re.search("key+", userInput)
            
            pickUpPristineKey = re.search("pristine+", userInput)
            
            pickUpFeathers = re.search("feather", userInput)
            
            pickUpPaper = re.search("paper", userInput)
            
            if pickUpPristineKey:
                
                interactionSaveUseable = str(interactionSave)
                
                boxOpenedCheck = re.search("boxOpened+", interactionSaveUseable)
                
                if boxOpenedCheck:
                    
                    interactionSaveUseable = str(interactionSave)
                    
                    pristineKeyGotCheck = re.search("pristineKeyGot+", interactionSaveUseable)
                    
                    if pristineKeyGotCheck:
                        
                        print("")
                    
                        print("You already have the pristine key from the box")
            
                        print("")
                    
                        roomOne()
                    
                    else:
                    
                        print("")
                        
                        print("You pick up the pristine key from the box and put it in your pocket")
                        
                        print("")
                        
                        inventory.append("pristine key")
                        
                        interactionSave.append("pristineKeyGot")
                        
                        roomOne()
                        
                else:
                    
                    print("")
                    
                    print("There is no pristine key in sight to pick up")
                    
                    print("")
                    
                    roomOne()
                    
            elif pickUpKey:
                
                interactionSaveUseable = str(interactionSave)
                
                hatchOpenedCheck = re.search("hatchOpened+", interactionSaveUseable)
                
                if hatchOpenedCheck:
                    
                    interactionSaveUseable = str(interactionSave)
                    
                    keyGotCheck = re.search("keyGot+", interactionSaveUseable)
                    
                    if keyGotCheck:
                        
                        print("")
                        
                        print("You already have the rusty key from within the hatch")
                        
                        print("")
                        
                        roomOne()
                        
                    else:
                        
                        print("")
                        
                        print("You pick up the rusty key from within the hatch and place it in your pocket")
                        
                        print("")
                        
                        inventory.append("key")
                        
                        interactionSave.append("keyGot")
                        
                        roomOne()
                
                else:
                    
                    print("")
                    
                    print("There's no key in sight to pick up")
                    
                    print("")
                    
                    roomOne()
                    
            elif pickUpFeathers:
                
                interactionSaveUseable = str(interactionSave)
                
                featherGotCheck = re.search("featherGot", interactionSaveUseable)
                
                quillMadeCheck = re.search("quillMade", interactionSaveUseable)
                
                if featherGotCheck:
                    
                    print("")
                    
                    print("You already have the feather")
                    
                    print("")
                    
                    roomOne()
                    
                else:
                    
                    if quillMadeCheck:
                        
                        print("")
                        
                        print("You have already made the quill, you don't need these")
                        
                        print("")
                        
                        roomOne()
                    
                    else:
                    
                        print("")
                        
                        print("You pick up a feather and carefully place it in your pocket")
                        
                        print("")
                        
                        inventory.append("feather")
                        
                        interactionSave.append("featherGot")
                        
                        roomOne()
                    
            elif pickUpPaper:
                
                interactionSaveUseable = str(interactionSave)
                
                paperGotCheck = re.search("paperGot", interactionSaveUseable)
                
                if paperGotCheck:
                    
                    print("")
                    
                    print("You already have paper")
                    
                    print("")
                    
                    roomOne()
                    
                else:
                    
                    print("")
                    
                    print("You pick up a piece of blank paper, fold it and put it in your pocket")
                    
                    print("")
                    
                    inventory.append("paper")
                    
                    interactionSave.append("paperGot")
                    
                    roomOne()
                
            else:
                
                print("")
                
                print("You can't pick that up")
                
                print("")
                
                roomOne()
            
        else:
            
            print("")
            
            print("That is not a valid input")
            
            print("")
            
            roomOne()
        
    def roomTwo():
        
        # ? Area prompt:
        """You cautiously walk into the hall, wary of your own sound while pondering the physique of the monstoristy making the footsteps and groans previous.
        Stepping over the man and onto the creaky floorboard of the to be explored hallway, you spot a room to your direct left and right, and a door straight ahead.
        Pictures cover the hall but so does a noticeable absence of blood on the walls compared to the horror show in the room you woke up."""
        
        # ? --------------------------- Drop of trolley START ---------------------------------------------------
        
        inventoryUseable = str(inventory)
        
        handTrolleyCheck = re.search("hand trolley", inventoryUseable)
        
        if handTrolleyCheck:
            
            print(colored("What do you want to do? (type help for a list of commands): ", f"{theme}", attrs=["bold"]))
            
            print("")
            
            print("You drop off the hand trolley next to the wardrobe")
            
            print("")
            
            findHandTrolley = inventory.index("hand trolley")
            
            inventory.pop(findHandTrolley)
            
            interactionSave.append("handTrolleyDroppedOff")
            
            roomTwo()
            
        else:
            
            pass
        
        userInput = input(colored("What do you want to do? (type help for a list of commands): ", f"{theme}", attrs=["bold"])).lower()
        
        # ? --------------------------- Drop of trolley END ---------------------------------------------------
            
        pickUpAction = re.search("pick up+", userInput)
        
        lookAtAction = re.search("look at+", userInput)
        
        goToTheAction1 = re.search("go", userInput)
        
        goToTheAction2 = re.search("to", userInput)
        
        useAction = re.search("use+", userInput)
        
        useWithAction = re.search("with+", userInput)
            
        if userInput == "help":
                
            print(help)
                
            roomTwo()
            
        elif userInput == "inventory":
            
            print("")
            
            print("You have:")
            
            print("")
            
            for items in inventory:
                print(items)
            
            print("")
            
            roomTwo()
            
        elif userInput == "save":
            
            save()
            
        elif userInput == "prompt":
            
            print(hallwayPrompt)
            
            roomTwo()
            
        elif userInput == "exit":
            
            exitCheck.append("exit")
            save()
            
        elif userInput == "clear":
            
            blankspace()
                
            roomTwo()
            
        elif userInput == "restart":
            
            game()
            
        elif userInput == "menu":
            
            startMenu()
            
        elif pickUpAction:
            
            print("")
            
            print("You can't pick that up")
            
            print("")
            
            roomTwo()
            
        elif lookAtAction:
            
            lookAtPictures = re.search("pictures", userInput)
            
            lookAtLeftDoor1 = re.search("left", userInput)
            
            lookAtLeftDoor2 = re.search("door", userInput)
            
            lookAtRightDoor1 = re.search("right", userInput)
            
            lookAtRightDoor2 = re.search("door", userInput)
            
            lookAtMiddleDoor1 = re.search("middle", userInput)
            
            lookAtMiddleDoor2 = re.search("door", userInput)
            
            lookAtRustyNecklace = re.search("necklace", userInput)
            
            lookAtMyself = re.search(r"\bself\b", userInput)
            
            lookAtMyselfAlternative = re.search("myself", userInput)
            
            lookAtFloor = re.search("floor", userInput)
            
            lookAtTrolley = re.search("trolley", userInput)
            
            lookAtTrolleyAlternative1 = re.search("dolly", userInput)
            
            interactionSaveUseable = str(interactionSave)
            
            starLocation3Check = re.search("location3", interactionSaveUseable)
            
            starLocation4Check = re.search("location4", interactionSaveUseable)
            
            starLocation5Check = re.search("location5", interactionSaveUseable)
            
            if lookAtPictures:

                print("""
There are a few pictures on the wall, one has a triumphant man holding the head of a mighty deer,
another with the same man next to a tent and a rifle. Looks like whoever this is enjoys hunting.
                """)
                
                roomTwo()
                
            elif lookAtLeftDoor1 and lookAtLeftDoor2:
                
                if starLocation3Check:
                    
                    sancheck = int(sanity[0])
                    
                    if sancheck >= 10:
                        
                        print("")
                        
                        print("The left door is slightly open and contains all of your deepest darkest nightmares from the depths of the abyss.")
                        
                        print("")
                        
                        roomTwo()
                        
                    else:

                        print("""
The left door is slightly open and there is a trail of dark red sludge, a mixture of food and blood, seaping from it.
                        """)
                    
                        sanchange = int(sanity[0])
        
                        sanchange += 2

                        sanity.clear()

                        sanity.append(sanchange)
                        
                        roomTwo()
                    
                else:

                    print("""
The left door doesn't appear to have a lock on it, but the handle looks dusty, you can infer this hasn't been opened recently.
                    """)
                    
                    roomTwo()
                
            elif lookAtRightDoor1 and lookAtRightDoor2:
                
                if starLocation4Check:
                    
                    sancheck = int(sanity[0])
                    
                    if sancheck >= 10:
                        
                        print("")
                        
                        print("The right door is slightly open and behind it is only pain and suffering.")
                        
                        print("")
                        
                        roomTwo()
                        
                    else:

                        print("""
The right door is slightly open and a dark red sludge, a mixture of food and blood, beckons you towards the room.
Your sense of smell is overwhelmed with the stench. Envisioning the contents past the door makes you uneasy.
                        """)
                    
                        sanchange = int(sanity[0])
                            
                        sanchange += 3
                        
                        sanity.clear()
                        
                        sanity.append(sanchange)

                        roomTwo()
                    
                else:
                
                    print("""
The right door doesn't appear to have a lock on it, from the handle's dust pattern it looks like it hasn't been opened recently, 
and you can smell something that reminds you of food from behind it. Envisioning the contents past the door makes you uneasy.
                    """)
                    
                    sanchange = int(sanity[0])
                        
                    sanchange += 1
                    
                    sanity.clear()
                    
                    sanity.append(sanchange)

                    roomTwo()
                
            elif lookAtMiddleDoor1 and lookAtMiddleDoor2:
                
                if starLocation5Check:
                    
                    sancheck = int(sanity[0])
                    
                    if sancheck >= 10:
                        
                        print("")
                        
                        print("The middle door is blocked by a heavy looking wardrobe that you couldn't move with your hands and there is no escape from your fate.")
                        
                        print("")
                        
                        roomTwo()
                        
                    else:

                        print("""
The middle door is blocked by a heavy looking wardrobe, and most likely can't be moved with just your hands.
Whoever this was didn't want anyone in or out. There is a dark sludge, a mixture of food and blood, 
that seems to scream for you while all senses are all overwhelmed.
                        """)
                    
                        sanchange = int(sanity[0])
        
                        sanchange += 2

                        sanity.clear()

                        sanity.append(sanchange)

                        roomTwo()
                    
                else:
    
                    print("""
The middle door is blocked by a heavy looking wardrobe, and most likely can't be moved with just your hands. 
Whoever did this didn't want anyone in our out.
                    """)
       
                    roomTwo()
                
            elif lookAtLeftDoor2 or lookAtRightDoor2 or lookAtMiddleDoor2:
                
                print("")
                
                print("Which door? (type: look at [direction] door")
                
                print()
                
                roomTwo()
            
            elif lookAtRustyNecklace:
                
                print("")
                
                print("There is a rusty necklace around your neck, it doesn't have a lock and looks like it can be opened")
                
                print("")
                
                roomTwo()
            
            elif lookAtMyself or lookAtMyselfAlternative:
                
                print("""
You look down at yourself, your hands are bruised and see signs of wear, you're wearing a ripped up suit with no tie,
you can't seem to remember anything, and you feel woozy, as if drunk.
                """)
                
                roomTwo()
                
            elif lookAtFloor:

                print("""
The portion of the floor in the hallway that isn't covered by a similar red rug to the last room is noticeably squeaky, but otherwise very immaculate
                """)
                
                roomTwo()
                
            elif lookAtTrolley or lookAtTrolleyAlternative1:
                
                interactionSaveUseable = str(interactionSave)
                
                handTrolleyDroppedOffCheck = re.search("handTrolleyDroppedOff", interactionSaveUseable)
                
                wardrobeMovedTrolleyCheck = re.search("wardrobeMovedTrolley", interactionSaveUseable)
                
                if handTrolleyDroppedOffCheck:
                    
                    if wardrobeMovedTrolleyCheck:
                        
                        print("")
                        
                        print("The trolley sits next to the moved wardrobe, and the door is free to be opened")
                        
                        print("")
                        
                        roomTwo()
                        
                    else:
                        
                        print("")
                        
                        print("There is a trolley next to the wardrobe, and could be used with the wardrobe to move it elsewhere")
                        
                        print("")
                        
                        roomTwo()
                    
                else:
                    
                    print("")
                    
                    print("There is no hand trolley to look at")
                    
                    print("")
                    
                    roomTwo()
            
            else:
                
                print("")
                
                print("You can't look at that")
                
                print("")
                
                roomTwo()
            
        elif goToTheAction1 and goToTheAction2:
            
            goToTheFirstRoom = re.search("first room", userInput)
            
            goToTheFirstRoomAlternative1 = re.search("study", userInput)
            
            goToTheThirdRoom = re.search("third room", userInput)
            
            goToTheThirdRoomAlternative1 = re.search("bedroom", userInput)
            
            goToTheThirdRoomAlternative2 = re.search("left door", userInput)
            
            goToTheFourthRoom = re.search("fourth room", userInput)
            
            goToTheFourthRoomAlternative1 = re.search("kitchen", userInput)
            
            goToTheFourthRoomAlternative2 = re.search("right door", userInput)
            
            goToTheFifthRoom = re.search("fifth", userInput)
            
            goToTheFifthRoomAlternative1 = re.search("living room", userInput)
            
            goToTheFifthRoomAlternative2 = re.search("middle", userInput)
            
            goToRoom = re.search("room", userInput)
            
            goToDoor = re.search("door", userInput)
            
            interactionSaveUseable = str(interactionSave)
            
            mapBeenUseable = str(mapBeen)
            
            thirdBeenCheck = re.search("thirdBeen", mapBeenUseable)
            
            fourthBeenCheck = re.search("fourthBeen", mapBeenUseable)
            
            starLocation3Check = re.search("location3", interactionSaveUseable)
            
            starLocation4Check = re.search("location4", interactionSaveUseable)
            
            starLocation5Check = re.search("location5", interactionSaveUseable)
            
            if goToTheFirstRoom or goToTheFirstRoomAlternative1:

                    print(colored("""
    You move back into the first room, seeing the blood on the walls again makes you feel uneasy.
                    """, attrs=["bold"]))

                    mapState.clear()
                    
                    mapState.append("1")
                    
                    sanchange = int(sanity[0])
                        
                    sanchange += 1
                    
                    sanity.clear()
                    
                    sanity.append(sanchange)
                    
                    roomOne()
            
            elif goToTheThirdRoom or goToTheThirdRoomAlternative1 or goToTheThirdRoomAlternative2:
                
                if thirdBeenCheck:
                        
                        print(colored("""
    You move back into the bedroom, its unusual homeliness makes you increasingly uneasy when compared to the atrocities previously seen
                        """, attrs=["bold"]))
                            
                        mapState.clear()
                        
                        mapState.append("3")
                        
                        sanchange = int(sanity[0])
                        
                        sanchange += 1
                        
                        sanity.clear()
                        
                        sanity.append(sanchange)
                    
                        roomThree()
                
                elif starLocation3Check:
                    
                    interactionSaveUseable = str(interactionSave)
                        
                    bedroomKillerAliveCheck = re.search("bedroomKillerAlive", interactionSaveUseable)
                    
                    bedroomKillerDeadCheck = re.search("bedroomKillerDead", interactionSaveUseable)
                    
                    if bedroomKillerAliveCheck or bedroomKillerDeadCheck:
                        
                        mapState.clear()
                        
                        mapState.append("3")
                        
                        print(colored("""
    You move back into the bedroom, its unusual homeliness makes you increasingly uneasy when compared to the atrocities previously seen
                        """, attrs=["bold"]))
                        
                        roomThree()
                        
                    else:
                
                        mapState.clear()
                        
                        mapState.append("3")
                        
                        mapBeen.append("thirdBeen")
                        
                        bedroomKillerThere()
                    
                else:
                    
                    print(bedroomKillerNotThere)
                    print("")
                    mapState.clear()
                    mapState.append("3")
                    mapBeen.append("thirdBeen")
                    roomThree()
                    
            elif goToTheFourthRoom or goToTheFourthRoomAlternative1 or goToTheFourthRoomAlternative2:
                
                if fourthBeenCheck:
                    
                    print(colored("""
    You move back into the kitchen, the horrific sight and smell freeze your body stone cold before continuing onward.
                    """, attrs=["bold"]))
                    
                    mapState.clear()
                    
                    mapState.append("4")
                    
                    roomFour()
                    
                elif starLocation4Check:
                    
                    interactionSaveUseable = str(interactionSave)
                        
                    bedroomKillerAliveCheck = re.search("bedroomKillerAlive", interactionSaveUseable)
                    
                    bedroomKillerDeadCheck = re.search("bedroomKillerDead", interactionSaveUseable)
                    
                    if bedroomKillerAliveCheck or bedroomKillerDeadCheck:
                        
                        mapState.clear()
                        
                        mapState.append("4")
                        
                        print(colored("""
    You move back into the kitchen, the horrific sight and smell freeze your body stone cold before continuing onward.
                        """, attrs=["bold"]))
                        
                        roomFour()
                        
                    else:
                
                        mapState.clear()
                        
                        mapState.append("4")
                        
                        mapBeen.append("fourthBeen")
                        
                        kitchenKillerThere()
                
                else:
                    
                    print(kitchenKillerNotThere)
                    print("")
                    mapState.clear()
                    mapState.append("4")
                    mapBeen.append("fourthBeen")
                    roomFour()
                    
            elif goToTheFifthRoom and goToRoom or goToTheFifthRoomAlternative2 and goToDoor or goToTheFifthRoomAlternative1:
                
                mapBeenUseable = str(mapBeen)
                
                interactionSaveUseable = str(interactionSave)
                
                fifthBeenCheck = re.search("fifthBeen", mapBeenUseable)
                
                wardrobeMovedTrolleyCheck = re.search("wardrobeMovedTrolley", interactionSaveUseable)
                
                starLocation5Check = re.search("location5", interactionSaveUseable)
                
                if wardrobeMovedTrolleyCheck:
                
                    if fifthBeenCheck:
                        
                        print(colored("""
    You move back into living room, your body wishes to leave and never look back.
                        """, attrs=["bold"]))
                            
                        mapState.clear()
                        
                        mapState.append("5")
                    
                        roomFour()
                    
                    elif starLocation5Check:
                        
                        interactionSaveUseable = str(interactionSave)
                        
                        livingRoomKillerAliveCheck = re.search("livingRoomKillerAlive", interactionSaveUseable)
                        
                        livingRoomKillerDeadCheck = re.search("livingRoomKillerDead", interactionSaveUseable)
                        
                        if livingRoomKillerAliveCheck or livingRoomKillerDeadCheck:
                            
                            mapState.clear()
                            
                            mapState.append("5")
                            
                            print(colored("""
    You move back into living room, your body wishes to leave and never look back.
                        """, attrs=["bold"]))
                            
                            roomFive()
                            
                        else:
                    
                            mapState.clear()
                            
                            mapState.append("5")
                            
                            mapBeen.append("fifthBeen")
                            
                            livingRoomKillerThere()
                        
                    else:
                        
                        print(livingRoomKillerNotThere)
                        mapState.clear()
                        mapState.append("5")
                        mapBeen.append("secondBeen")
                        mapBeen.append("thirdBeen")
                        mapBeen.append("fourthBeen")
                        mapBeen.append("fifth")
                        roomFive()
                    
                else:
                    
                    print("")
                    
                    print("The wardrobe is in the way")
                    
                    print("")
                    
                    roomOne()
            
            else:
                
                print("")
                
                print("You can't go to that")
                
                print("")
                
                roomTwo()
                    
        elif useWithAction:
            
            useCrowbarWithWardrobe1 = re.search("crowbar", userInput)
            
            useCrowbarWithWardrobe2 = re.search("wardrobe", userInput)
            
            useHandTrolleyWithWardrobe1 = re.search("hand", userInput)
            
            useHandTrolleyWithWardrobe2 = re.search("trolley", userInput)
            
            useHandTrolleyWithWardrobeAlternative1 = re.search("dolly", userInput)
            
            useHandTrolleyWithWardrobe3 = re.search("wardrobe", userInput)
            
            interactionSaveUseable = str(interactionSave)
            
            wardrobeUprightCheck = re.search("wardrobeUpright", interactionSaveUseable)
            
            crowbarGotCheck = re.search("crowbarGot", interactionSaveUseable)
            
            if useHandTrolleyWithWardrobe1 and useHandTrolleyWithWardrobe2 and useHandTrolleyWithWardrobe3 or useHandTrolleyWithWardrobeAlternative1 and useHandTrolleyWithWardrobe3 or useHandTrolleyWithWardrobe2 and useHandTrolleyWithWardrobe3:
                
                handTrolleyDroppedOffCheck = re.search("handTrolleyDroppedOff", interactionSaveUseable)
                
                wardrobeMovedTrolleyCheck = re.search("wardrobeMovedTrolley", interactionSaveUseable)
                
                if handTrolleyDroppedOffCheck:
                    
                    if wardrobeMovedTrolleyCheck:
                        
                        print("")
                        
                        print("You have already moved the wardrobe out of the way, escape, awaits.")
                        
                        print("")
                        
                        roomTwo()
                    
                    else:
                        
                        if wardrobeUprightCheck:
                
                            print("")
                            
                            print("You use the hand trolley to move the heavy wardrobe out of the way of the door, escape, awaits.")
                            
                            print("")
                            
                            interactionSave.append("wardrobeMovedTrolley")
                            
                            roomTwo()
                            
                        else:
                            
                            print("")
                            
                            print("You need the wardrobe to upright before you can move it away, and it's too difficult to get leverage with just your hands. Looks like you need another tool first.")
                
                            print("")
                            
                            roomTwo()
                
                else:
                    
                    print("")
                    
                    print("You can't use that with that")
                    
                    print("")
                    
                    roomTwo()
        
            elif useCrowbarWithWardrobe1 and useCrowbarWithWardrobe2:
                
                if crowbarGotCheck:
                
                    if wardrobeUprightCheck:
                        
                        print("")
                        
                        print("You have already propped the wardrobe upright with the crowbar.")
                        
                        print("")
                        
                        roomTwo()
                        
                    else:
                
                        print("""
You use your maximum strength currently achievable to prop the wardrobe upright,
it's still in front of the door, but now might be easier to move with another tool.
                        """)
                
                        interactionSave.append("wardrobeUpright")
                    
                        roomTwo()
                    
                else:
                
                    print("")
                    
                    print("You do not have a crowbar")
                    
                    print("")
                    
                    roomTwo()
            else:
            
                print("")
                
                print("You can't use that with that")
                
                print("")
                
                roomTwo()
            
        elif useAction:
            
            useMap = re.search("map", userInput)
            
            useRustyNecklace = re.search("necklace", userInput)
        
            if useMap:

                mapUse()
                
            elif useRustyNecklace:
                
                print("")
                
                print("You open the rusty necklace on your neck and see a picture of what you think is you and 2 children, it puts you at ease")
                
                print("")
                
                sanchange = int(sanity[0])
    
                sanchange -= 2

                sanity.clear()

                sanity.append(sanchange)
                
                roomOne()
                
            else:
                
                print("")
                
                print("You can't use that")
                
                print("")
                
                roomTwo()
        
        else: 
            
            print("")
            
            print("That is not a valid input")
            
            print("")
            
            roomTwo()
            
    def roomThree():
        
        # ? Area prompt:
        """You open the door as carefully and as silently as you can. The third room seems to be a quaint bedroom, with a large luxurious bed with red and gold covers
        accompanied by large walnut drawers and a seemingly vacant space for a huge wardrobe. How could a person like Frank have a nice bedroom like this?"""
        
        userInput = input(colored("What do you want to do? (type help for a list of commands): ", f"{theme}", attrs=["bold"])).lower()
            
        pickUpAction = re.search("pick up+", userInput)
        
        lookAtAction = re.search("look at+", userInput)
        
        goToTheAction1 = re.search("go", userInput)
        
        goToTheAction2 = re.search("to", userInput)
        
        useAction = re.search("use+", userInput)
        
        useWithAction = re.search("with+", userInput)
            
        if userInput == "help":
                
            print(help)
                
            roomThree()
            
        elif userInput == "inventory":
            
            print("")
            
            print("You have:")
            
            print("")
            
            for items in inventory:
                print(items)
            
            print("")
            
            roomThree()
            
        elif userInput == "save":
            
            save()
            
        elif userInput == "prompt":
            
            interactionSaveUseable = str(interactionSave)
            
            bedroomKillerAliveCheck = re.search("bedroomKillerAlive", interactionSaveUseable)
            
            bedroomKillerDeadCheck = re.search("bedroomKillerDead", interactionSaveUseable)
            
            handTrolleyDroppedOffCheck = re.search("handTrolleyDroppedOffCheck", interactionSaveUseable)
            
            if bedroomKillerAliveCheck:
                
                print(bedroomKillerAlive)
                
                roomThree()
            
            elif bedroomKillerDeadCheck:
                
                print(bedroomKillerDead)
                
                roomThree()
                
            elif handTrolleyDroppedOffCheck:
                
                print(colored("""You open the door as carefully and as silently as you can. The room past the left door seems to be a quaint bedroom, with a large luxurious walnut bed
    accompanied by large walnut drawers and a seemingly vacant space for a wardrobe. How could a person like Frank have a nice bedroom like this?""", attrs=["bold"]))
                
                print("")
                
                roomThree()
                
            else:
            
                print(bedroomKillerNotThere)
                
                print("")
                
                roomThree()
            
        elif userInput == "exit":
            
            exitCheck.append("exit")
            save()
            
        elif userInput == "clear":
            
            blankspace()
                
            roomThree()
            
        elif userInput == "restart":
            
            game()
            
        elif userInput == "menu":
            
            startMenu()
            
        elif pickUpAction:
            
            pickUpPistol = re.search("pistol", userInput)
            
            pickUpPistolAlternative = re.search("gun", userInput)
            
            pickUpCrowbar = re.search("crowbar", userInput)
            
            pickUpHandTrolley1 = re.search("hand", userInput)
            
            pickUpHandTrolley2 = re.search("trolley", userInput)
            
            pickUpHandTrolleyAlternative1 = re.search("dolly", userInput)
            
            if pickUpHandTrolley1 and pickUpHandTrolley2 or pickUpHandTrolley2 or pickUpHandTrolleyAlternative1:
                
                interactionSaveUseable = str(interactionSave)
                
                location4Check = re.search("location4", interactionSaveUseable)
                
                handTrolleyPickedUpCheck = re.search("handTrolleyPickedUp", interactionSaveUseable)
                
                if handTrolleyPickedUpCheck:
                    
                    print("")
                    
                    print("You already have the hand trolley")
                    
                    print("")
                    
                    roomThree()
                    
                else:
                
                    if location4Check:
                        
                        print("")
                        
                        print("You grab the hand trolley by it's handle and begin dragging it around.")
                        
                        print("")
                        
                        inventory.append("hand trolley")
                        
                        interactionSave.append("handTrolleyPickedUp")
                        
                        roomThree()
                        
                    else:
                        
                        print("")
                        
                        print("There is no trolley to pick up")
                        
                        print("")
                        
                        roomThree()
            
            elif pickUpPistol or pickUpPistolAlternative:
                
                interactionSaveUseable = str(interactionSave)
                
                bedroomDrawerOpenedCheck = re.search("bedroomDrawerOpened", interactionSaveUseable)
                
                knifeGotCheck = re.search("knifeGot", interactionSaveUseable)
                
                pistolGotCheck = re.search("pistolGot", interactionSaveUseable)
                
                if pistolGotCheck:
                    
                    print("")
                    
                    print("You already have the pistol")
                    
                    print("")
                    
                    roomThree()
                
                elif bedroomDrawerOpenedCheck and knifeGotCheck:
                    
                    print("")
                    
                    print("You're already holding a weapon.")
                    
                    print("")
                    
                    roomThree()
                
                elif bedroomDrawerOpenedCheck:
                    
                    sancheck = int(sanity[0])
                    
                    sanityeventsUseable = str(sanityevents)
                    
                    pickUpPistolEventCheck = re.search("pickUpPistolEvent", sanityeventsUseable)
                    
                    if sancheck >= 18:
                        
                        if pickUpPistolEventCheck:
                            
                            pass
                        
                        else:
                        
                            pickUpPistolEvent = colored("""
 ██ ▄█▀ ██▓ ██▓     ██▓    
 ██▄█▒ ▓██▒▓██▒    ▓██▒    
▓███▄░ ▒██▒▒██░    ▒██░    
▓██ █▄ ░██░▒██░    ▒██░    
▒██▒ █▄░██░░██████▒░██████▒
▒ ▒▒ ▓▒░▓  ░ ▒░▓  ░░ ▒░▓  ░
░ ░▒ ▒░ ▒ ░░ ░ ▒  ░░ ░ ▒  ░
░ ░░ ░  ▒ ░  ░ ░     ░ ░   
░  ░    ░      ░  ░    ░  ░
                            """, f"{theme}", attrs=["bold"])
                        
                            blankspace()
                                
                            time.sleep(2)
                            
                            print(pickUpPistolEvent)
                            time.sleep(0.3)
                            blankspace()
                            time.sleep(0.6)
                            print(pickUpPistolEvent)
                            time.sleep(0.3)
                            blankspace()
                            time.sleep(0.6)
                            print(pickUpPistolEvent)
                            time.sleep(0.3)
                            blankspace()
                                
                            sanityevents.append("pickUpPistolEvent")
                    
                    print("")
                    
                    print("You pick up the pistol and place it in your dominant hand, with only fear in your mind.")
                    
                    print("")
                    
                    interactionSave.append("pistolGot")
                    
                    inventory.append("pistol")
                    
                    sanchange = int(sanity[0])
    
                    sanchange += 2

                    sanity.clear()

                    sanity.append(sanchange)
                    
                    roomThree()
                    
                else:
                    
                    print("")
                    
                    print("There is no pistol to pick up.")
                    
                    print("")
                    
                    roomThree()
                    
            elif pickUpCrowbar:
                
                inventoryUseable = str(inventory)
                
                interactionSaveUseable = str(interactionSave)
                
                bedroomKillerAliveCheck = re.search("bedroomKillerAlive", interactionSaveUseable)
                
                bedroomKillerDeadCheck = re.search("bedroomKillerDead", interactionSaveUseable)
                
                kitchenKillerAliveCheck = re.search("kitchenKillerAlive", interactionSaveUseable)
                
                kitchenKillerDeadCheck = re.search("kitchenKillerDead", interactionSaveUseable)
                
                knifeGotCheck = re.search("knife", inventoryUseable)
                
                pistolGotCheck = re.search("pistol", inventoryUseable)
                
                crowbarGotCheck = re.search("crowbar", inventoryUseable)
                
                if bedroomKillerAliveCheck or bedroomKillerDeadCheck or kitchenKillerAliveCheck or kitchenKillerDeadCheck:
                    
                    if crowbarGotCheck:
                        
                        print("")
                        
                        print("You already have the crowbar")
                        
                        print("")
                        
                        roomThree()
                
                    elif knifeGotCheck:
                        
                        print("")
                        
                        print("You pick up the scarlet crowbar to replace the knife in your hand")
                        
                        print("")
                        
                        inventory.append("crowbar")
                        
                        interactionSave.append("crowbarGot")
                        
                        roomThree()
                        
                    elif pistolGotCheck:
                        
                        print("")
                        
                        print("You pick up the scarlet crowbar to replace the pistol in your hand")
                        
                        print("")
                        
                        inventory.append("crowbar")
                        
                        interactionSave.append("crowbarGot")
                        
                        roomThree()
                        
                else:
                    
                    print("")
                    
                    print("There is no crowbar to pick up")
                    
                    print("")
                    
                    roomThree()
                    
            else:
            
                print("")
                
                print("You can't pick that up")
                
                print("")
                
                roomThree()
            
        elif lookAtAction:
            
            lookAtRustyNecklace = re.search("necklace", userInput)
            
            lookAtMyself = re.search(r"\bself\b", userInput)
            
            lookAtMyselfAlternative = re.search("myself", userInput)
            
            lookAtWalnutDrawers = re.search("walnut", userInput)
            
            lookAtDrawers = re.search("drawer", userInput)
            
            lookAtPistol = re.search("pistol", userInput)
            
            lookAtPistolAlternative = re.search("gun", userInput)
            
            lookAtPicture = re.search("picture", userInput)
            
            lookAtLetter = re.search("letter", userInput)
            
            lookAtBed = re.search("bed", userInput)
            
            lookAtCovers1 = re.search("red", userInput)
            
            lookAtCovers2 = re.search("covers", userInput)
            
            lookAtVacantSpace1 = re.search("vacant", userInput)
            
            lookAtVacantSpace2 = re.search("space", userInput)

            lookAtWardrobe = re.search("wardrobe", userInput)
            
            lookAtBody = re.search("body", userInput)
            
            lookAtBodyAlter1 = re.search("corpse", userInput)
            
            lookAtBodyAlter2 = re.search("frank", userInput)
            
            lookAtBodyAlter3 = re.search("walker", userInput)
            
            lookAtBodyAlter4 = re.search("man", userInput)
            
            lookAtCrowbar = re.search("crowbar", userInput)
            
            if lookAtRustyNecklace:
                
                print("")
                
                print("There is a rusty necklace around your neck, it doesn't have a lock and looks like it can be opened")
                
                print("")
                
                roomThree()
                
            elif lookAtCrowbar:
                
                interactionSaveUseable = str(interactionSave)
                
                bedroomKillerAliveCheck = re.search("bedroomKillerAlive", interactionSaveUseable)
                
                bedroomKillerDeadCheck = re.search("bedroomKillerDead", interactionSaveUseable)
                
                if bedroomKillerAliveCheck:
                    
                    print("")
                    
                    print("Next to the killer is a scarlet crowbar, and might be able to help you move something large.")
                    
                    print("")
                    
                    roomThree()
                    
                elif bedroomKillerDeadCheck:
                    
                    print("")
                    
                    print("Next to Frank is a scarlet red crowbar which might be able to help you move a heavy object.")
                    
                    print("")
                    
                    roomThree()
                    
                else:
                    
                    print("")
                    
                    print("There is no crowbar to look at")
                    
                    print("")
                    
                    roomThree()
            
            elif lookAtBody or lookAtBodyAlter1 or lookAtBodyAlter2 or lookAtBodyAlter3 or lookAtBodyAlter4:
                
                interactionSaveUseable = str(interactionSave)
                
                bedroomKillerAliveCheck = re.search("bedroomKillerAlive", interactionSaveUseable)
                
                bedroomKillerDeadCheck = re.search("bedroomKillerDead", interactionSaveUseable)
                
                crowbarGotCheck = re.search("crowbarGot", interactionSaveUseable)
                
                if crowbarGotCheck:
                    
                    if bedroomKillerAliveCheck:
                        
                        print("")
                        
                        print("The killer lies on the ground, unable to get up.")
                        
                        print("")
                        
                        roomThree()
                        
                    elif bedroomKillerDeadCheck:
                        
                        print("")
                        
                        print("Frank Walker lies dead on the ground. Your duty, finally fulfilled.")
                        
                        print("")
                        
                        roomThree()
                        
                    else:
                        
                        print("")
                        
                        print("You can't look at that")
                        
                        print("")
                        
                        roomThree()
                        
                else:
                
                    if bedroomKillerAliveCheck:
                        
                        print("")
                        
                        print("The killer lies on the ground, unable to get up. He dropped a scarlet red crowbar on the ground next to him")
                        
                        print("")
                        
                        roomThree()
                        
                    elif bedroomKillerDeadCheck:
                        
                        print("")
                        
                        print("Frank Walker lies dead on the ground. Your duty, finally fulfilled. He dropped a scarlet red crowbar on the ground next to him")
                        
                        print("")
                        
                        roomThree()
                    
                    else:
                    
                        print("")
                        
                        print("You can't look at that")
                        
                        print("")
                        
                        roomThree()
                
            elif lookAtMyself or lookAtMyselfAlternative:
                
                print("""
You look down at yourself, your hands are bruised and see signs of wear, you're wearing a ripped up suit with no tie,
you can't seem to remember anything, and you feel woozy, as if drunk.
                """)
                
                roomThree()
                
            elif lookAtWalnutDrawers and lookAtDrawers or lookAtDrawers:

                print("""
The walnut drawers to the right of the bed, nearest the door, are completely clean, and could easily be opened.
On top of the drawers is a picture frame and a sealed letter.
                """)

                roomThree()
                
            elif lookAtPistol or lookAtPistolAlternative:
                
                interactionSaveUseable = str(interactionSave)
                
                bedroomDrawerOpenedCheck = re.search("bedroomDrawerOpened", interactionSaveUseable)
                
                pistolGotCheck = re.search("pistolGot", interactionSaveUseable)
                
                knifeGotCheck = re.search("knifeGot", interactionSaveUseable)
                
                if pistolGotCheck:
                    
                    print("")
                    
                    print("You already have the pistol from the drawer.")
                    
                    print("")
                    
                    roomThree()
                    
                elif knifeGotCheck:
                    
                    print("")
                    
                    print("You already have a weapon, best not to have another, for your own sake.")
                    
                    print("")
                    
                    roomThree()
                
                elif bedroomDrawerOpenedCheck:
                    
                    sancheck = int(sanity[0])
                    
                    sanityeventsUseable = str(sanityevents)
                    
                    pistolLookEventCheck = re.search("pistolLookEvent", sanityeventsUseable)
                    
                    if sancheck >= 10:
                        
                        if pistolLookEventCheck:
                            
                            pass
                        
                        else:
                        
                            blankspace()
                                
                            time.sleep(2.3)
                            
                            print(colored("""
 ██▓███   ██▓ ▄████▄   ██ ▄█▀    ██▓▄▄▄█████▓    █    ██  ██▓███  
▓██░  ██▒▓██▒▒██▀ ▀█   ██▄█▒    ▓██▒▓  ██▒ ▓▒    ██  ▓██▒▓██░  ██▒
▓██░ ██▓▒▒██▒▒▓█    ▄ ▓███▄░    ▒██▒▒ ▓██░ ▒░   ▓██  ▒██░▓██░ ██▓▒
▒██▄█▓▒ ▒░██░▒▓▓▄ ▄██▒▓██ █▄    ░██░░ ▓██▓ ░    ▓▓█  ░██░▒██▄█▓▒ ▒
▒██▒ ░  ░░██░▒ ▓███▀ ░▒██▒ █▄   ░██░  ▒██▒ ░    ▒▒█████▓ ▒██▒ ░  ░
▒▓▒░ ░  ░░▓  ░ ░▒ ▒  ░▒ ▒▒ ▓▒   ░▓    ▒ ░░      ░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░
░▒ ░      ▒ ░  ░  ▒   ░ ░▒ ▒░    ▒ ░    ░       ░░▒░ ░ ░ ░▒ ░     
░░        ▒ ░░        ░ ░░ ░     ▒ ░  ░          ░░░ ░ ░ ░░       
          ░  ░ ░      ░  ░       ░                 ░              
             ░                                                    
                            """, f"{theme}", attrs=["bold"]))
                        
                            time.sleep(3)
                            
                            print("You know you want to.")
                            
                            print("")
                            
                            time.sleep(2)
                            
                            blankspace()
                            
                            sanityevents.append("pistolLookEvent")
                    
                    print("")
                    
                    print("There is a pistol in the drawer, it beckons you.")
                    
                    print("")
                    
                    sanchange = int(sanity[0])
                    
                    sanchange += 1
                    
                    sanity.clear()
                    
                    sanity.append(sanchange)
                
                    roomThree()
                    
                else:
                
                    print("")
                    
                    print("There is no pistol to look at.")
                    
                    print("")
                    
                    roomThree()

            elif lookAtPicture:
                
                print("")
                
                print("The picture on the top of the walnut drawers is of a man accompanying a young boy with glasses next to a telescope on a starry night.")
                
                print("")
                
                roomThree()
                
            elif lookAtLetter:
                
                print("")
                
                print("The letter is addressed to \"Frank Walker\" from a \"Nancy Knott\", dated 23rd of March. It's perfectly sealed.")
                
                print("")
                
                roomThree()
                
            elif lookAtBed:

                print("""
The bed, with the accompanying red and gold covers looks incredibly expensive.
It has a wooden frame which goes up to the ceiling where a red curtain can be draped for privacy.
                """)
                
                roomThree()
                
            elif lookAtCovers1 and lookAtCovers2 or lookAtCovers1:
                
                print("")
                
                print("The red and gold covers on the bed are tightly tucked in and look incredibly expensive.")
                
                print("")
                
                roomThree()
                
            elif lookAtVacantSpace1 and lookAtVacantSpace2 or lookAtWardrobe and lookAtVacantSpace2 or lookAtVacantSpace2:
                
                print("")
                
                print("""
There is a portion of the room to the left of the bed which is completely blank, with scratch marks on the floor.
It looks like the wardrobe has been moved somewhere.
                """)
                
                roomThree()
                
            else:
                
                print("")
                
                print("You can't look at that")
                
                print("")
                
                roomThree()
            
        elif goToTheAction1 and goToTheAction2:
            
            goToTheFirstRoom = re.search("first", userInput)
            
            goToTheFirstRoomAlternative1 = re.search("study", userInput)
            
            goToTheSecondRoom = re.search("second", userInput)
            
            goToSecondRoomAlternative1 = re.search("hallway", userInput)
            
            goToTheFourthRoom = re.search("fourth", userInput)
            
            goToFourthRoomAlternative1 = re.search("kitchen", userInput)
            
            goToFourthRoomAlternative2 = re.search("right", userInput)
            
            goToTheFifthRoom = re.search("fifth", userInput)
            
            goToTheFifthRoomAlternative1 = re.search("living room", userInput)
            
            goToTheFifthRoomAlternative2 = re.search("middle", userInput)
            
            goToRoom = re.search("room", userInput)
            
            goToDoor = re.search("door", userInput)
            
            if goToTheFirstRoom and goToRoom or goToTheFirstRoomAlternative1:
                
                print(colored("""
    You move back into the first room, seeing the blood on the walls again makes you feel uneasy.
                    """, attrs=["bold"]))
                mapState.clear()
                mapState.append("1")
                sanchange = int(sanity[0])
                sanchange += 1
                sanity.clear()
                sanity.append(sanchange)
                roomOne()
            
            elif goToTheSecondRoom and goToRoom or goToSecondRoomAlternative1:
                
                print(colored("""
    You move back into the second room, the hallway is so quiet that it makes you uneasy
                    """, attrs=["bold"]))
                mapState.clear()
                mapState.append("2")
                sanchange = int(sanity[0])
                sanchange += 1
                sanity.clear()
                sanity.append(sanchange)
                roomTwo()
                
            elif goToTheFourthRoom and goToRoom or goToFourthRoomAlternative1 or goToFourthRoomAlternative2 and goToDoor:
                
                mapBeenUseable = str(mapBeen)
                
                interactionSaveUseable = str(interactionSave)
                
                fourthBeenCheck = re.search("fourthBeen", mapBeenUseable)
                
                starLocation4Check = re.search("location4", interactionSaveUseable)
                
                if fourthBeenCheck:
                    
                    print(colored("""
    You move back into the kitchen, the horrific sight and smell freeze your body stone cold before continuing onward.
                    """, attrs=["bold"]))
                    
                    mapState.clear()
                    
                    mapState.append("4")
                    
                    roomFour()
                    
                elif starLocation4Check:
                    
                    interactionSaveUseable = str(interactionSave)
                        
                    bedroomKillerAliveCheck = re.search("bedroomKillerAlive", interactionSaveUseable)
                    
                    bedroomKillerDeadCheck = re.search("bedroomKillerDead", interactionSaveUseable)
                    
                    if bedroomKillerAliveCheck or bedroomKillerDeadCheck:
                        
                        mapState.clear()
                        
                        mapState.append("4")
                        
                        print(colored("""
    You move back into the kitchen, the horrific sight and smell freeze your body stone cold before continuing onward.
                        """, attrs=["bold"]))
                        
                        roomFour()
                        
                    else:
                
                        mapState.clear()
                        
                        mapState.append("4")
                        
                        mapBeen.append("fourthBeen")
                        
                        kitchenKillerThere()
                
                else:
                    
                    print(kitchenKillerNotThere)
                    print("")
                    mapState.clear()
                    mapState.append("4")
                    mapBeen.append("fourthBeen")
                    roomFour()
                
            elif goToTheFifthRoom and goToRoom or goToTheFifthRoomAlternative2 and goToDoor or goToTheFifthRoomAlternative1:
                
                mapBeenUseable = str(mapBeen)
                
                interactionSaveUseable = str(interactionSave)
                
                fifthBeenCheck = re.search("fifthBeen", mapBeenUseable)
                
                wardrobeMovedTrolleyCheck = re.search("wardrobeMovedTrolley", interactionSaveUseable)
                
                starLocation5Check = re.search("location5", interactionSaveUseable)
                
                if wardrobeMovedTrolleyCheck:
                
                    if fifthBeenCheck:
                        
                        print(colored("""
    You move back into living room, your body wishes to leave and never look back.
                        """, attrs=["bold"]))
                            
                        mapState.clear()
                        
                        mapState.append("5")
                    
                        roomFour()
                    
                    elif starLocation5Check:
                        
                        interactionSaveUseable = str(interactionSave)
                        
                        livingRoomKillerAliveCheck = re.search("livingRoomKillerAlive", interactionSaveUseable)
                        
                        livingRoomKillerDeadCheck = re.search("livingRoomKillerDead", interactionSaveUseable)
                        
                        if livingRoomKillerAliveCheck or livingRoomKillerDeadCheck:
                            
                            mapState.clear()
                            
                            mapState.append("5")
                            
                            print(colored("""
    You move back into living room, your body wishes to leave and never look back.
                        """, attrs=["bold"]))
                            
                            roomFive()
                            
                        else:
                    
                            mapState.clear()
                            
                            mapState.append("5")
                            
                            mapBeen.append("fifthBeen")
                            
                            livingRoomKillerThere()
                        
                    else:
                        
                        print(livingRoomKillerNotThere)
                        mapState.clear()
                        mapState.append("5")
                        mapBeen.append("secondBeen")
                        mapBeen.append("thirdBeen")
                        mapBeen.append("fourthBeen")
                        mapBeen.append("fifth")
                        roomFive()
                    
                else:
                    
                    print("")
                    
                    print("The wardrobe is in the way")
                    
                    print("")
                    
                    roomOne()
                
            else:
                
                print("")
                
                print("You can't go to that")
                
                print("")
                
                roomThree()
                
        elif useAction:
                
            useMap = re.search("map", userInput)
            
            useRustyNecklace = re.search("necklace", userInput)
            
            useDrawers1 = re.search("walnut", userInput)
            
            useDrawers2 = re.search("drawer", userInput)
            
            useLetter = re.search("letter", userInput)
            
            interactionSaveUseable = str(interactionSave)
            
            letterOpenedCheck = re.search("letterOpened", interactionSaveUseable)
            
            bedroomDrawerOpenedCheck = re.search("bedroomDrawerOpened", interactionSaveUseable)
            
            if useMap:
                
                mapUse()
                
            elif useRustyNecklace:
                
                print("")
                
                print("You open the rusty necklace on your neck and see a picture of what you think is you and 2 children, it puts you at ease")
                
                print("")
                
                roomThree()
                
            elif useDrawers1 and useDrawers2 or useDrawers2:
                
                if bedroomDrawerOpenedCheck:
                    
                    print("")
                    
                    print("There is gun next to a small club badge for the \"Starfarers Junior Astronomy Club\"")
                    
                    print("")
                    
                    roomThree()
                    
                else:
                
                    print("")
                    
                    print("You open the drawer quietly and quickly notice a fearsome pistol next to a small club badge for the \"Starfarers Junior Astronomy Club\"")
                    
                    print("")
                    
                    interactionSave.append("bedroomDrawerOpened")
                    
                    roomThree()
                    
            elif useLetter:
                
                if letterOpenedCheck:
                    
                    print("""
The letter reads:

\"Thank you for making an appearance at Chris's funeral last saturday, even though it was meant to be so so long ago.
I know it was hard to get up there and talk in front of all those people because of how much he meant to you.
It feels like just yesterday you two were going on your little stargazing trips with that big telescope of his.

Anyhow, I hope you're doing well after what happened between us, the funeral was the only time I've seen you in weeks.
Mike also hopes you're doing okay, I know you never liked him but one day I hope you two get along. He's been so distracted
with this big \"Constellation Killer\" case, we've even had to board our windows and home school our kids!

Sorry for the rambling, I just hope you're okay in these tough times, you've had too much put on you.

Love,

Nancy\"
                    """)
                    
                    roomThree()
                    
                else:
                
                    print("""
You open the letter from \"Nancy Knott\" and feel the name is familiar, but you can't place your finger on it.

The letter reads:

\"Thank you for making an appearance at Chris's funeral last saturday, even though it was meant to be so so long ago.
I know it was hard to get up there and talk in front of all those people because of how much he meant to you.
It feels like just yesterday you two were going on your little stargazing trips with that big telescope of his.

Anyhow, I hope you're doing well after what happened between us, the funeral was the only time I've seen you in weeks.
Mike also hopes you're doing okay, I know you never liked him but one day I hope you two get along. He's been so distracted
with this big \"Constellation Killer\" case, we've even had to board our windows and home school our kids!.

Sorry for the rambling, I just hope you're okay in these tough times, you've had too much put on you.

Love,

Nancy\"
                    """)
                
                    interactionSave.append("letterOpened")
                    
                    sanchange = int(sanity[0])
    
                    sanchange -= 2

                    sanity.clear()

                    sanity.append(sanchange)
                
                    roomThree()
                
            else:
                
                print("")
                
                print("You can't use that")
                
                print("")
                
                roomThree()
                
        elif useWithAction:
            
            print("")
            
            print("You can't use that with that")
            
            print("")
            
            roomThree()
            
        else:
            
            print("")
            
            print("That is not a valid input")
            
            print("")
            
            roomThree()
                
    def roomFour():
        
        # ? Area prompt:
        """You open the door as carefully and as silently as you can. But suddenly the smell hits you and the sight overwhelms you.
        The room past the right door is a horrific kitchen, where only the worst has occurred. In attempts to cover tracks and out of pure desperation, atrocities have been committed.
        The center of the kitchen holds a huge meat grinder and to the left of the door, a befouled stove contains boiling over pots and several pans which have been knocked over.
        Directly ahead are windows with no newspaper on them, however they've been barred, and it would be near impossible to get out that way.
        A fridge stands valiantly as one of the only relatively clean objects in the room. 
        You'll never let Walker get away with this."""
        
        userInput = input(colored("What do you want to do? (type help for a list of commands): ", f"{theme}", attrs=["bold"])).lower()
            
        pickUpAction = re.search("pick up+", userInput)
        
        lookAtAction = re.search("look at+", userInput)
        
        goToTheAction1 = re.search("go", userInput)
        
        goToTheAction2 = re.search("to", userInput)
        
        useAction = re.search("use+", userInput)
        
        useWithAction = re.search("with+", userInput)
            
        if userInput == "help":
                
            print(help)
                
            roomFour()
            
        elif userInput == "inventory":
            
            print("")
            
            print("You have:")
            
            print("")
            
            for items in inventory:
                print(items)
            
            print("")
            
            roomFour()
            
        elif userInput == "save":
            
            save()
            
        elif userInput == "prompt":
            
            interactionSaveUseable = str(interactionSave)
            
            kitchenKillerAliveCheck = re.search("kitchenKillerAlive", interactionSaveUseable)
            
            kitchenKillerDeadCheck = re.search("kitchenKillerDead", interactionSaveUseable)
            
            handTrolleyDroppedOffCheck = re.search("handTrolleyDroppedOff", interactionSaveUseable)
            
            if kitchenKillerAliveCheck:
                
                print(kitchenKillerAlive)
                
                roomFour()
                
            elif kitchenKillerDeadCheck:
                
                print(kitchenKillerDead)
                
                roomFour()
                
            elif handTrolleyDroppedOffCheck:
                
                print(colored("""
    You open the door as carefully and as silently as you can. But suddenly the smell hits you and the sight overwhelms you.
    The room past the right door is a horrific kitchen, where only the worst has occurred. In attempts to cover tracks and out of pure desperation, atrocities have been committed.
    The center of the kitchen holds a huge meat grinder and to the left of the door, a befouled stove contains boiling over pots and several pans which have been knocked over.
    Directly ahead are windows with no newspaper on them, however they've been barred, and it would be near impossible to get out that way.
    A fridge stands valiantly as one of the only relatively clean objects in the room. 
    How could Frank do something like this?""", attrs=["bold"]))
                
                print("")
                
                roomFour()
                
            else:
            
                print(kitchenKillerNotThere)
                
                print("")
                
                roomFour()
            
        elif userInput == "exit":
            
            exitCheck.append("exit")
            save()
            
        elif userInput == "clear":
            
            blankspace()
                
            roomFour()
            
        elif userInput == "restart":
            
            game()
            
        elif userInput == "menu":
            
            startMenu()
            
        elif pickUpAction:
            
            pickUpKnife = re.search("knife", userInput)
            
            pickUpCrowbar = re.search("crowbar", userInput)
            
            pickUpHandTrolley1 = re.search("hand", userInput)
            
            pickUpHandTrolley2 = re.search("trolley", userInput)
            
            pickUpHandTrolleyAlternative1 = re.search("dolly", userInput)
            
            if pickUpHandTrolley1 and pickUpHandTrolley2 or pickUpHandTrolley2 or pickUpHandTrolleyAlternative1:
                
                interactionSaveUseable = str(interactionSave)
                
                location3Check = re.search("location3", interactionSaveUseable)
                
                location5Check = re.search("location5", interactionSaveUseable)
                
                handTrolleyPickedUpCheck = re.search("handTrolleyPickedUp", interactionSaveUseable)
                
                if handTrolleyPickedUpCheck:
                    
                    print("")
                    
                    print("You already have the hand trolley")
                    
                    print("")
                    
                    roomFour()
                    
                else:
                
                    if location3Check or location5Check:
                        
                        print("")
                        
                        print("You grab the hand trolley by it's handle and begin dragging it around.")
                        
                        print("")
                        
                        inventory.append("hand trolley")
                        
                        interactionSave.append("handTrolleyPickedUp")
                        
                        roomFour()
                        
                    else:
                        
                        print("")
                        
                        print("There is no trolley to pick up")
                        
                        print("")
                        
                        roomFour()
            
            elif pickUpKnife:
                
                interactionSaveUseable = str(interactionSave)
                
                knifeGotCheck = re.search("knifeGot", interactionSaveUseable)
                
                pistolGotCheck = re.search("pistolGot", interactionSaveUseable)
                
                if pistolGotCheck:
                    
                    print("")
                    
                    print("You're already holding a weapon.")
                    
                    print("")
                    
                    roomFour()
                
                elif knifeGotCheck:
                    
                    print("")
                    
                    print("You already have the knife from the counter top.")
                    
                    print("")
                    
                    roomFour()
                
                else:
                    
                    sancheck = int(sanity[0])
                    
                    sanityeventsUseable = str(sanityevents)
                    
                    pickUpKnifeEventCheck = re.search("pickUpKnifeEvent", sanityeventsUseable)
                    
                    if sancheck >= 18:
                        
                        if pickUpKnifeEventCheck:
                            
                            pass
                        
                        else:
                        
                            pickUpKnifeEvent = colored("""
 ██ ▄█▀ ██▓ ██▓     ██▓    
 ██▄█▒ ▓██▒▓██▒    ▓██▒    
▓███▄░ ▒██▒▒██░    ▒██░    
▓██ █▄ ░██░▒██░    ▒██░    
▒██▒ █▄░██░░██████▒░██████▒
▒ ▒▒ ▓▒░▓  ░ ▒░▓  ░░ ▒░▓  ░
░ ░▒ ▒░ ▒ ░░ ░ ▒  ░░ ░ ▒  ░
░ ░░ ░  ▒ ░  ░ ░     ░ ░   
░  ░    ░      ░  ░    ░  ░
                            """, f"{theme}", attrs=["bold"])
                        
                            blankspace()
                                
                            time.sleep(2)
                            
                            print(pickUpKnifeEvent)
                            time.sleep(0.3)
                            blankspace()
                            time.sleep(0.6)
                            print(pickUpKnifeEvent)
                            time.sleep(0.3)
                            blankspace()
                            time.sleep(0.6)
                            print(pickUpKnifeEvent)
                            time.sleep(0.3)
                            blankspace()
                                
                            sanityevents.append("pickUpKnifeEvent")
                    
                    print("")
                    
                    print("You pick up the knife and place it in your dominant hand, with only fear in your mind.")
                    
                    print("")
                    
                    interactionSave.append("knifeGot")
                    
                    inventory.append("knife")
                    
                    sanchange = int(sanity[0])
    
                    sanchange += 2

                    sanity.clear()

                    sanity.append(sanchange)
                    
                    roomFour()
            
            elif pickUpCrowbar:
                
                inventoryUseable = str(inventory)
                
                interactionSaveUseable = str(interactionSave)
                
                bedroomKillerAliveCheck = re.search("bedroomKillerAlive", interactionSaveUseable)
                
                bedroomKillerDeadCheck = re.search("bedroomKillerDead", interactionSaveUseable)
                
                kitchenKillerAliveCheck = re.search("kitchenKillerAlive", interactionSaveUseable)
                
                kitchenKillerDeadCheck = re.search("kitchenKillerDead", interactionSaveUseable)
                
                location5Check = re.search("location5", interactionSaveUseable)
                
                knifeGotCheck = re.search("knife", inventoryUseable)
                
                pistolGotCheck = re.search("pistol", inventoryUseable)
                
                crowbarGotCheck = re.search("crowbar", inventoryUseable)
                
                if bedroomKillerAliveCheck or bedroomKillerDeadCheck or kitchenKillerAliveCheck or kitchenKillerDeadCheck or location5Check:
                
                    if crowbarGotCheck:
                        
                        print("")
                        
                        print("You already have the crowbar")
                        
                        print("")
                        
                        roomFour()
                        
                
                    elif knifeGotCheck:
                        
                        print("")
                        
                        print("You pick up the scarlet crowbar to replace the knife in your hand")
                        
                        print("")
                        
                        inventory.append("crowbar")
                        
                        interactionSave.append("crowbarGot")
                        
                        roomFour()
                        
                    elif pistolGotCheck:
                        
                        print("")
                        
                        print("You pick up the scarlet crowbar to replace the pistol in your hand")
                        
                        print("")
                        
                        inventory.append("crowbar")
                        
                        interactionSave.append("crowbarGot")
                        
                        roomFour()
                        
                    
                    else:
                        
                        print("")
                        
                        print("You pick up the crowbar and place it in your hand")
                        
                        print("")
                        
                        inventory.append("crowbar")
                        
                        interactionSave.append("crowbarGot")
                        
                        roomFour()
                        
                else:
                    
                    print("")
                    
                    print("There is no crowbar to pick up")
                    
                    print("")
                    
                    roomFour()

            else:
                
                print("")
                
                print("You can't pick that up")
                
                print("")
                
                roomFour()
        
        elif lookAtAction:
            
            lookAtRustyNecklace = re.search("necklace", userInput)
            
            lookAtMyself = re.search(r"\bself\b", userInput)
            
            lookAtMyselfAlternative = re.search("myself", userInput)
            
            lookAtStove = re.search("stove", userInput)
            
            lookAtCounter = re.search("counter", userInput)
            
            lookAtPots = re.search("pot", userInput)
            
            lookAtPans = re.search("pan", userInput)
            
            lookAtGrinder = re.search("grinder", userInput)
            
            lookAtFridge = re.search("fridge", userInput)
            
            lookAtFloor = re.search("floor", userInput)
            
            lookAtWindow = re.search("window", userInput)
            
            lookAtKnife = re.search("knife", userInput)
            
            lookAtRedSubstance = re.search("red substance", userInput)
            
            lookAtRedSubstanceAlternative1 = re.search("blood", userInput)
            
            lookAtBody = re.search("body", userInput)
            
            lookAtBodyAlter1 = re.search("corpse", userInput)
            
            lookAtBodyAlter2 = re.search("frank", userInput)
            
            lookAtBodyAlter3 = re.search("walker", userInput)
            
            lookAtBodyAlter4 = re.search("man", userInput)
            
            lookAtCrowbar = re.search("crowbar", userInput)
            
            if lookAtRustyNecklace:
                
                print("")
                
                print("There is a rusty necklace around your neck, it doesn't have a lock and looks like it can be opened")
                
                print("")
                
                roomFour()
            
            elif lookAtCrowbar:
                
                interactionSaveUseable = str(interactionSave)
                
                kitchenKillerAliveCheck = re.search("kitchenKillerAlive", interactionSaveUseable)
                
                kitchenKillerDeadCheck = re.search("kitchenKillerDead", interactionSaveUseable)
                
                location5Check = re.search("location5", interactionSaveUseable)
                
                if kitchenKillerAliveCheck:
                    
                    print("")
                    
                    print("Next to the killer is a scarlet crowbar, and might be able to help you move something large.")
                    
                    print("")
                    
                    roomFour()
                    
                elif kitchenKillerDeadCheck:
                    
                    print("")
                    
                    print("Next to Frank is a scarlet red crowbar which might be able to help you move a heavy object.")
                    
                    print("")
                    
                    roomFour()
                    
                elif location5Check:
                    
                    print("")
                    
                    print("Besides the meat grinder is a scarlet crowbar, and it might be able to help you move something large.")
                    
                    print("")
                    
                    roomFour()
                    
                else:
                    
                    print("")
                    
                    print("There is no crowbar to look at")
                    
                    print("")
                    
                    roomFour()
                
            elif lookAtBody or lookAtBodyAlter1 or lookAtBodyAlter2 or lookAtBodyAlter3 or lookAtBodyAlter4:
                
                interactionSaveUseable = str(interactionSave)
                
                kitchenKillerAliveCheck = re.search("kitchenKillerAlive", interactionSaveUseable)
                
                kitchenKillerDeadCheck = re.search("kitchenKillerDead", interactionSaveUseable)
                
                crowbarGotCheck = re.search("crowbarGot", interactionSaveUseable)
                
                if crowbarGotCheck:
                    
                    if kitchenKillerAliveCheck:
                        
                        print("")
                        
                        print("The killer lies on the ground, unable to get up.")
                        
                        print("")
                        
                        roomThree()
                        
                    elif kitchenKillerDeadCheck:
                        
                        print("")
                        
                        print("Frank Walker lies dead on the ground. Your duty, finally fulfilled.")
                        
                        print("")
                        
                        roomThree()
                        
                    else:
                        
                        print("")
                        
                        print("You can't look at that")
                        
                        print("")
                        
                        roomThree()
                        
                else:
                
                    if kitchenKillerAliveCheck:
                        
                        print("")
                        
                        print("The killer lies on the ground, unable to get up. He dropped a scarlet red crowbar on the ground next to him")
                        
                        print("")
                        
                        roomThree()
                        
                    elif kitchenKillerDeadCheck:
                        
                        print("")
                        
                        print("Frank Walker lies dead on the ground. Your duty, finally fulfilled. He dropped a scarlet red crowbar on the ground next to him")
                        
                        print("")
                        
                        roomThree()
                    
                    else:
                    
                        print("")
                        
                        print("You can't look at that")
                        
                        print("")
                        
                        roomThree()
                
            elif lookAtMyself or lookAtMyselfAlternative:
                
                print("""
You look down at yourself, your hands are bruised and see signs of wear, you're wearing a ripped up suit with no tie,
you can't seem to remember anything, and you feel woozy, as if drunk.
                """)
                
                roomFour()
            
            elif lookAtStove:
                
                print("")
                
                print("The stove top is egregious at best and holds several pots and pans on top of it. There is a small counter top to the left of it.")
                
                print("")
                
                roomFour()
                
            elif lookAtCounter:
                
                print("")
                
                print("The counter to the left of the stove contains a small amount of kitchen utensils, and a remarkably sharp knife.")
                
                print("")
                
                roomFour()
                
            elif lookAtKnife:
                
                interactionSaveUseable = str(interactionSave)
                
                bedroomDrawerOpenedCheck = re.search("bedroomDrawerOpened", interactionSaveUseable)
                
                pistolGotCheck = re.search("pistolGot", interactionSaveUseable)
                
                knifeGotCheck = re.search("knifeGot", interactionSaveUseable)
                
                if pistolGotCheck:
                    
                    print("")
                    
                    print("You already have a weapon, best not to have another, for your own sake.")
                    
                    print("")
                    
                    roomFour()
                    
                elif knifeGotCheck:
                    
                    print("")
                    
                    print("You already have the knife from the counter top")
                    
                    print("")
                    
                    roomFour()
                
                else:
                    
                    sancheck = int(sanity[0])
                    
                    sanityeventsUseable = str(sanityevents)
                    
                    knifeLookEventCheck = re.search("knifeLookEvent", sanityeventsUseable)
                    
                    if sancheck >= 14:
                        
                        if knifeLookEventCheck:
                            
                            pass
                        
                        else:
                        
                            blankspace()
                                
                            time.sleep(2.3)
                            
                            print(colored("""
 ██▓███   ██▓ ▄████▄   ██ ▄█▀    ██▓▄▄▄█████▓    █    ██  ██▓███  
▓██░  ██▒▓██▒▒██▀ ▀█   ██▄█▒    ▓██▒▓  ██▒ ▓▒    ██  ▓██▒▓██░  ██▒
▓██░ ██▓▒▒██▒▒▓█    ▄ ▓███▄░    ▒██▒▒ ▓██░ ▒░   ▓██  ▒██░▓██░ ██▓▒
▒██▄█▓▒ ▒░██░▒▓▓▄ ▄██▒▓██ █▄    ░██░░ ▓██▓ ░    ▓▓█  ░██░▒██▄█▓▒ ▒
▒██▒ ░  ░░██░▒ ▓███▀ ░▒██▒ █▄   ░██░  ▒██▒ ░    ▒▒█████▓ ▒██▒ ░  ░
▒▓▒░ ░  ░░▓  ░ ░▒ ▒  ░▒ ▒▒ ▓▒   ░▓    ▒ ░░      ░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░
░▒ ░      ▒ ░  ░  ▒   ░ ░▒ ▒░    ▒ ░    ░       ░░▒░ ░ ░ ░▒ ░     
░░        ▒ ░░        ░ ░░ ░     ▒ ░  ░          ░░░ ░ ░ ░░       
          ░  ░ ░      ░  ░       ░                 ░              
             ░                                                    
                            """, f"{theme}", attrs=["bold"]))
                        
                            time.sleep(3)
                            
                            print("You know you want to.")
                            
                            print("")
                            
                            time.sleep(2)
                            
                            blankspace()
                            
                            sanityevents.append("knifeLookEvent")
                
                print("")
                
                print("The knife on top of the counter is incredibly sharp and should be handled with care.")
                
                print("")
                
                sanchange = int(sanity[0])
    
                sanchange += 1

                sanity.clear()

                sanity.append(sanchange)
                
                roomFour()
            
            elif lookAtPots:
                
                interactionSaveUseable = str(interactionSave)
                
                potLookedAtCheck = re.search("potLookedAt", interactionSaveUseable)
                
                sancheck = int(sanity[0])
                
                sanityeventsUseable = str(sanityevents)
                
                lookAtPotsEventCheck = re.search("lookAtPotsEvent", sanityeventsUseable)
                
                eyeAscii = colored("""
            ..,,;;;;;;,,,,
       .,;'';;,..,;;;,,,,,.''';;,..
    ,,''                    '';;;;,;''
   ;'    ,;@@;'  ,@@;, @@, ';;;@@;,;';.
  ''  ,;@@@@@'  ;@@@@; ''    ;;@@@@@;;;;
     ;;@@@@@;    '''     .,,;;;@@@@@@@;;;
    ;;@@@@@@;           , ';;;@@@@@@@@;;;.
     '';@@@@@,.  ,   .   ',;;;@@@@@@;;;;;;
        .   '';;;;;;;;;,;;;;@@@@@;;' ,.:;'
          ''..,,     ''''    '  .,;'
               ''''''::''''''''
                """, f"{theme}", attrs=["bold"])
                
                if sancheck >= 16:
                    
                    if lookAtPotsEventCheck:
                        
                        pass
                    
                    elif potLookedAtCheck:
                    
                        blankspace()
                            
                        time.sleep(3)
                        
                        print(eyeAscii)
                        
                        time.sleep(1.5)
                        
                        print("You failed me")
                        
                        print("")
                        
                        time.sleep(1.5)

                        blankspace()
                            
                        print(eyeAscii)
                        time.sleep(0.1)
                        blankspace()
                        time.sleep(0.1)
                        print(eyeAscii)
                        time.sleep(0.1)
                        blankspace()
                        time.sleep(0.1)
                        print(eyeAscii)
                        time.sleep(0.1)
                        blankspace()
                        time.sleep(0.1)
                        print(eyeAscii)
                        time.sleep(0.1)
                        blankspace()
                        time.sleep(0.1)
                        print(eyeAscii)
                        time.sleep(0.1)
                        blankspace()
                        
                        print("You failed")
                        
                        print("")
                        
                        time.sleep(3)
                        
                        blankspace()
                            
                        sanityevents.append("lookAtPotsEvent")
                        
                    else:
                        
                        pass
                                    
                if potLookedAtCheck:
                    
                    print(f"""
{eyeAscii}

A blue eye is floating at the top of the pot, mixed in with the dark red sludge
                """)
                
                    roomFour()
                
                else:
                    
                    print("""
The pots on the stove have some form of a dark red sludge which keeps boiling over within them, leaking onto the floor. You keep looking at the pot with some sick fascination, until...
                    """)
                
                    time.sleep(5.8)
                
                    print(f"""
{eyeAscii}

An eye.
                    """)
                    
                    sanchange = int(sanity[0])
    
                    sanchange += 3

                    sanity.clear()

                    sanity.append(sanchange)
                
                    interactionSave.append("potLookedAt")

                    roomFour()
                    
            elif lookAtPans:
                
                sancheck = int(sanity[0])
                
                sanityeventsUseable = str(sanityevents)
                
                lookAtPansEventCheck = re.search("lookAtPansEvent", sanityeventsUseable)
                
                if lookAtPansEventCheck:
                    
                    pass
                
                elif sancheck >= 16:
                    
                    bloodAscii = colored("""                
                ░░░░░░      ░░                                                                                  ░░░░                    
            ░░▒▒░░░░      ░░                                                                                    ██                    
            ░░▒▒░░  ░░    ░░                                                                      ░░                                  
                ░░░░    ░░    ░░                                                                  ░░                                    
                    ░░░░░░░░  ▒▒                          ░░                                    ░░          ░░                          
                ░░      ░░░░░░░░▒▒░░▒▒░░░░              ░░                                  ░░            ░░                          
                ░░  ▒▒░░  ░░░░░░░░░░░░  ░░                                            ░░  ░░            ░░                                                       
                    ░░░░      ░░      ░░  ▒▒░░░░░░░░░░    ▒▒                ░░  ▒▒                ░░░░                                  
                    ░░░░░░    ░░░░░░░░░░▒▒░░▒▒░░░░    ░░░░  ▒▒            ▒▒▒▒░░      ░░░░░░░░░░░░░░                                    
                    ░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░  ░░░░░░░░░░░░        ▒▒▒▒  ░░▒▒▒▒▒▒▒▒▓▓▓▓▒▒░░░░                                      
                ░░  ░░▒▒░░▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░▒▒▒▒░░░░░░░░░░░░░░▒▒░░▒▒░░▒▒░░▒▒▒▒░░░░░░░░░░░░░░▒▒░░▒▒░░░░░░░░                              
            ░░  ░░░░▓▓▓▓▒▒▒▒▒▒░░░░░░░░▒▒░░▒▒░░░░░░░░░░▒▒░░░░░░░░  ▓▓░░░░░░░░░░░░░░░░░░▒▒▒▒░░░░▒▒      ░░  ░░░░░░░░░░                  
    ░░░░░░░░░░░░░░░░░░▓▓▓▓▒▒▒▒▒▒▒▒▓▓░░▓▓░░░░▒▒░░░░░░░░░░▒▒░░░░░░░░▒▒░░▒▒▓▓▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒░░▒▒░░      ░░░░░░                                             
                    ░░░░░░░░░░░░▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░░░                                
                    ░░░░░░░░░░░░░░░░░░░░  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░                    ░░  ░░     
                    """, f"{theme}", attrs=["bold"])
                    
                    blankspace()
                    
                    print(bloodAscii)
                    
                    print("You violently stomp on the puddle of meat and blood out of pure rage")
                    
                    print("")
                    
                    time.sleep(3)
                    
                    blankspace()
                        
                    print("You wish to cease")
                    
                    print("")
                    
                    time.sleep(3)
                    
                    blankspace()
                        
                    sanityevents.append("lookAtPansEvent")
                    
                print("")
                
                print("There are a few pans on the stove containing a dark red mixture of food and blood, some of them have fallen on the floor and spilt the red substance.")
                
                print("")
                
                sanchange = int(sanity[0])
    
                sanchange += 2

                sanity.clear()

                sanity.append(sanchange)
                
                roomFour()
                
            elif lookAtGrinder:
                
                interactionSaveUseable = str(interactionSave)
                
                grinderTurnedCheck = re.search("grinderTurned", interactionSaveUseable)
                
                sancheck = int(sanity[0])
                
                sanityeventsUseable = str(sanityevents)
                
                lookAtGrinderEventCheck = re.search("lookAtGrinderEvent", sanityeventsUseable)
                
                if sancheck >= 20:
                    
                    if lookAtGrinderEventCheck:
                        
                        pass
                    
                    else:
                    
                        print("")
                        
                        print("That's where all of your friends are, and where you'll be soon. If you listened to Nancy you would be safe.")
                        
                        print("")

                        sanityevents.append("lookAtGrinderEvent")
                
                if grinderTurnedCheck:
                    
                    print("")
                    
                    print("The grinder in the center of the room is massive and couldn't be moved at all, the grinder is near empty.")
                    
                    print("")
                    
                    roomFour()
                    
                else:
                
                    print("")
                    
                    print("The grinder in the center of the room is massive and couldn't be moved at all, it looks like the grinder's passage is being blocked")
                    
                    print("")
                    
                    sanchange = int(sanity[0])
    
                    sanchange += 1

                    sanity.clear()

                    sanity.append(sanchange)
                    
                    roomFour()
                
            elif lookAtFridge:
                
                print("")
                
                print("The fridge to the right of the stove is somewhat undefiled, and stands as one of the cleaner objects in the room.")
                
                print("")
                
                roomFour()
                
            elif lookAtFloor:
                
                print("")
                
                print("The floors are incredibly disgusting to behold, everything is covered completely in abyss-like red")
                
                print("")
                
                sanchange = int(sanity[0])
    
                sanchange += 2

                sanity.clear()

                sanity.append(sanchange)
                
                roomFour()
                
            elif lookAtWindow:
                
                sancheck = int(sanity[0])
                
                sanityeventsUseable = str(sanityevents)
                
                lookAtWindowEventCheck = re.search("lookAtWindowEvent", sanityeventsUseable)
                
                if sancheck >= 15:
                    
                    if lookAtWindowEventCheck:
                        
                        pass
                    
                    else:
                    
                        print("""
There are a large group of people standing outside the window who all have grim expressions on their face. After about 3 seconds a gargantuan portion of snow
obscures the group and they disappear without a trace. They remind you of people who have since ceased, due to your negligence.
                        """)
                    
                        sanityevents.append("lookAtWindowEvent")
                        
                        roomFour()
                
                print("")
                
                print("The most you can see outside of the window is a few trees and a complete absence of light, no one is coming for you.")
                
                print("")
                
                sanchange = int(sanity[0])
    
                sanchange += 2

                sanity.clear()

                sanity.append(sanchange)
                
                roomFour()
            
            elif lookAtRedSubstance or lookAtRedSubstanceAlternative1:
                
                print("")
                
                print("All of the floor is littered with a mixture of meat and blood.")
                
                print("")
                
                sanchange = int(sanity[0])

                sanchange += 2

                sanity.clear()

                sanity.append(sanchange)
                
                roomFour()
            
            else:
                
                print("")
                
                print("You can't look at that")
                
                print("")
                
                roomFour()
                
        elif goToTheAction1 and goToTheAction2:
            
            goToTheFirstRoom = re.search("first", userInput)
            
            goToTheFirstRoomAlternative1 = re.search("study", userInput)
            
            goToTheSecondRoom = re.search("second", userInput)
            
            goToSecondRoomAlternative1 = re.search("hallway", userInput)
            
            goToTheThirdRoom = re.search("third", userInput)
            
            goToThirdRoomAlternative1 = re.search("bedroom", userInput)
            
            goToThirdRoomAlternative2 = re.search("left", userInput)
            
            goToTheFifthRoom = re.search("fifth", userInput)
            
            goToTheFifthRoomAlternative1 = re.search("living room", userInput)
            
            goToTheFifthRoomAlternative2 = re.search("middle", userInput)
            
            goToRoom = re.search("room", userInput)
            
            goToDoor = re.search("door", userInput)
            
            if goToTheFirstRoom and goToRoom or goToTheFirstRoomAlternative1:
                
                print(colored("""
    You move back into the first room, seeing the blood on the walls again makes you feel uneasy.
                    """, attrs=["bold"]))
                mapState.clear()
                mapState.append("1")
                sanchange = int(sanity[0])
                sanchange += 1
                sanity.clear()
                sanity.append(sanchange)
                roomOne()
            
            elif goToTheSecondRoom and goToRoom or goToSecondRoomAlternative1:
                
                print(colored("""
    You move back into the second room, the hallway is so quiet that it makes you uneasy
                    """, attrs=["bold"]))
                mapState.clear()
                mapState.append("2")
                sanchange = int(sanity[0])
                sanchange += 1
                sanity.clear()
                sanity.append(sanchange)
                roomTwo()
                
            elif goToTheThirdRoom and goToRoom or goToThirdRoomAlternative1 or goToThirdRoomAlternative2 and goToDoor:
                
                mapBeenUseable = str(mapBeen)
                
                interactionSaveUseable = str(interactionSave)
                
                thirdBeenCheck = re.search("thirdBeen", mapBeenUseable)
                
                starLocation3Check = re.search("location3", interactionSaveUseable)
                
                if thirdBeenCheck:
                    
                    print(colored("""
    You move back into the bedroom, its unusual homeliness makes you increasingly uneasy when compared to the atrocities previously seen
                    """, attrs=["bold"]))
                    
                    mapState.clear()
                    
                    mapState.append("3")
                    
                    sanchange = int(sanity[0])
                        
                    sanchange += 1
                    
                    sanity.clear()
                    
                    sanity.append(sanchange)
                    
                    roomThree()
                    
                elif starLocation3Check:
                    
                    interactionSaveUseable = str(interactionSave)
                        
                    bedroomKillerAliveCheck = re.search("bedroomKillerAlive", interactionSaveUseable)
                    
                    bedroomKillerDeadCheck = re.search("bedroomKillerDead", interactionSaveUseable)
                    
                    if bedroomKillerAliveCheck or bedroomKillerDeadCheck:
                        
                        mapState.clear()
                        
                        mapState.append("3")
                        
                        print(colored("""
    You move back into the bedroom, its unusual homeliness makes you increasingly uneasy when compared to the atrocities previously seen
                        """, attrs=["bold"]))
                        
                        roomThree()
                        
                    else:
                        
                        mapState.clear()
                        
                        mapState.append("3")
                        
                        mapBeen.append("thirdBeen")
                        
                        bedroomKillerThere()
                
                else:
                    
                    print(bedroomKillerNotThere)
                    print("")
                    mapState.clear()
                    mapState.append("3")
                    mapBeen.append("thirdBeen")
                    roomThree()
                
            elif goToTheFifthRoom and goToRoom or goToTheFifthRoomAlternative2 and goToDoor or goToTheFifthRoomAlternative1:
                
                mapBeenUseable = str(mapBeen)
                
                interactionSaveUseable = str(interactionSave)
                
                fifthBeenCheck = re.search("fifthBeen", mapBeenUseable)
                
                wardrobeMovedTrolleyCheck = re.search("wardrobeMovedTrolley", interactionSaveUseable)
                
                starLocation5Check = re.search("location5", interactionSaveUseable)
                
                if wardrobeMovedTrolleyCheck:
                
                    if fifthBeenCheck:
                        
                        print(colored("""
    You move back into living room, your body wishes to leave and never look back.
                        """, attrs=["bold"]))
                            
                        mapState.clear()
                        
                        mapState.append("5")
                    
                        roomFour()
                    
                    elif starLocation5Check:
                        
                        interactionSaveUseable = str(interactionSave)
                        
                        livingRoomKillerAliveCheck = re.search("livingRoomKillerAlive", interactionSaveUseable)
                        
                        livingRoomKillerDeadCheck = re.search("livingRoomKillerDead", interactionSaveUseable)
                        
                        if livingRoomKillerAliveCheck or livingRoomKillerDeadCheck:
                            
                            mapState.clear()
                            
                            mapState.append("5")
                            
                            print(colored("""
    You move back into living room, your body wishes to leave and never look back.
                        """, attrs=["bold"]))
                            
                            roomFive()
                            
                        else:
                    
                            mapState.clear()
                            
                            mapState.append("5")
                            
                            mapBeen.append("fifthBeen")
                            
                            livingRoomKillerThere()
                        
                    else:
                        
                        print(livingRoomKillerNotThere)
                        mapState.clear()
                        mapState.append("5")
                        mapBeen.append("secondBeen")
                        mapBeen.append("thirdBeen")
                        mapBeen.append("fourthBeen")
                        mapBeen.append("fifth")
                        roomFive()
                    
                else:
                    
                    print("")
                    
                    print("The wardrobe is in the way")
                    
                    print("")
                    
                    roomOne()
                
            else:
                
                print("")
                
                print("You can't go to that")
                
                print("")
                
                roomThree()
        
        elif useAction:
            
            useRustyNecklace = re.search("necklace", userInput)
            
            useMap = re.search("map", userInput)
            
            useGrinder = re.search("grinder", userInput)
            
            useFridge = re.search("fridge", userInput)
            
            if useRustyNecklace:
                
                print("")
                
                print("You open the rusty necklace on your neck and see a picture of what you think is you and 2 children, it puts you at ease")
                
                print("")
                
                sanchange = int(sanity[0])

                sanchange -= 2

                sanity.clear()

                sanity.append(sanchange)
                
                roomFour()
            
            elif useMap:
                
                mapUse()
                
            elif useGrinder:
                
                interactionSaveUseable = str(interactionSave)
                
                grinderTurnedCheck = re.search("grinderTurned", interactionSaveUseable)
                
                sancheck = int(sanity[0])
                
                if sancheck >= 24:
                    
                    sanityeventsUseable = str(sanityevents)
                    
                    useGrinderEventCheck = re.search("useGrinderEvent", sanityeventsUseable)
                    
                    if useGrinderEventCheck:
                        
                        pass
                    
                    else:
                    
                        bu = colored("""
 ▄▄▄▄    █    ██ 
▓█████▄  ██  ▓██▒
▒██▒ ▄██▓██  ▒██░
▒██░█▀  ▓▓█  ░██░
░▓█  ▀█▓▒▒█████▓ 
░▒▓███▀▒░▒▓▒ ▒ ▒ 
▒░▒   ░ ░░▒░ ░ ░ 
 ░    ░  ░░░ ░ ░ 
 ░         ░     
      ░          
                        """, f"{theme}", attrs=["bold"])
                    
                        dum = colored("""
▓█████▄  █    ██  ███▄ ▄███▓
▒██▀ ██▌ ██  ▓██▒▓██▒▀█▀ ██▒
░██   █▌▓██  ▒██░▓██    ▓██░
░▓█▄   ▌▓▓█  ░██░▒██    ▒██ 
░▒████▓ ▒▒█████▓ ▒██▒   ░██▒
 ▒▒▓  ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░
 ░ ▒  ▒ ░░▒░ ░ ░ ░  ░      ░
 ░ ░  ░  ░░░ ░ ░ ░      ░   
   ░       ░            ░   
 ░                          
                        """, f"{theme}", attrs=["bold"])
                    
                        blankspace()
                            
                        time.sleep(10)
                        
                        # ? first set bu
                        
                        print(bu)
                        
                        time.sleep(0.4)
                        
                        blankspace()
                            
                        time.sleep(0.2)
                        
                        # ? first set dum
                        
                        print(dum)
                        
                        time.sleep(2.8)
                        
                        blankspace()
                            
                        time.sleep(0.2)
                        
                        # ? second set bu
                        
                        print(bu)
                        
                        time.sleep(0.4)
                        
                        blankspace()
                            
                        time.sleep(0.2)
                        
                        # ? second set dum
                        
                        print(dum)
                        
                        time.sleep(2.8)
                        
                        blankspace()
                            
                        time.sleep(0.2)
                        
                        # ? third set bu
                        
                        print(bu)
                        
                        time.sleep(0.4)
                        
                        blankspace()
                            
                        time.sleep(0.2)
                        
                        # ? third set dum
                        
                        print(dum)
                        
                        time.sleep(2.8)
                        
                        blankspace()
                            
                        time.sleep(0.2)
                        
                        # ? fourth set bu
                        
                        print(bu)
                        
                        time.sleep(0.4)
                        
                        blankspace()
                            
                        time.sleep(0.2)
                        
                        # ? fourth set dum
                        
                        print(dum)
                        
                        time.sleep(2.8)
                        
                        blankspace()
                            
                        sanityevents.append("useGrinderEvent")
                    
                if grinderTurnedCheck:
                    
                    print("")
                    
                    print("The grinder almost freezes your finger as soon as you make contact again. It's empty now and turning the handle reveals nothing.")
                    
                    print("")
                    
                    roomFour()
                    
                else:
                
                    print("""
The grinder is incredibly cold to the touch. After slightly turning the handle, a significant portion of gore escapes the mouth of the grinder.
Your only wish is to escape and rid your mind forever of this madness.
                    """)
                    
                    interactionSave.append("grinderTurned")
                    
                    sanchange = int(sanity[0])
    
                    sanchange += 3

                    sanity.clear()

                    sanity.append(sanchange)

                    roomFour()
                    
            elif useFridge:
                
                print("""
Opening the fridge inwards reveals an incredible amount of \"SPAM\" cans which could last anyone several months.
                """)
                
                roomFour()
                
            else:
                
                print("")
                
                print("You can't use that")
                
                print("")
                
                roomFour()
        
        elif useWithAction:
            
            print("")
            
            print("You can't use that with that")
            
            print("")
            
            roomFour()
        
        else:
            
            print("")
            
            print("That is not a valid input")
            
            print("")
            
            roomFour()
            
    def roomFive():
        
        # ? Area prompt:
        """You open the door to the final room and a living room greets you upon entry. A final door is parallel to your position which holds 3 locks.
        The rest of the room is homely, a fireplace is on for warmth, joined by a large leather couch. Another rug makes itself known with it's familiar red and gold swirls,
        a large triumphant paining above the fireplace rests perfectly centered, and a counter with an alluring amount of alcohol with accompanying wine glasses."""
        
        userInput = input(colored("What do you want to do? (type help for a list of commands): ", f"{theme}", attrs=["bold"])).lower()
            
        pickUpAction = re.search("pick up+", userInput)
        
        lookAtAction = re.search("look at+", userInput)
        
        goToTheAction1 = re.search("go", userInput)
        
        goToTheAction2 = re.search("to", userInput)
        
        useAction = re.search("use+", userInput)
        
        useWithAction = re.search("with+", userInput)
            
        if userInput == "help":
                
            print(help)
                
            roomFive()
            
        elif userInput == "inventory":
            
            print("")
            
            print("You have:")
            
            print("")
            
            for items in inventory:
                print(items)
            
            print("")
            
            roomFive()
            
        elif userInput == "save":
            
            save()
            
        elif userInput == "prompt":
        
            interactionSaveUseable = str(interactionSave)
            
            livingRoomKillerAliveCheck = re.search("livingRoomKillerAlive", interactionSaveUseable)
            
            livingRoomKillerDeadCheck = re.search("livingRoomKillerDead", interactionSaveUseable)
            
            if livingRoomKillerAliveCheck:
                
                print(livingRoomKillerAlive)
                
                roomFive()
                
            elif livingRoomKillerDeadCheck:
                
                print(livingRoomKillerDead)
                
                roomFive()
                
            else:
            
                print(livingRoomKillerNotThere)
                
                roomFive()
            
        elif userInput == "exit":
            
            exitCheck.append("exit")
            save()
            
        elif userInput == "clear":
            
            blankspace()
                
            roomFive()
            
        elif userInput == "restart":
            
            game()
            
        elif userInput == "menu":
            
            startMenu()
            
        elif pickUpAction:
            
            pickUpBucket = re.search("bucket", userInput)
            
            pickUpBronzeKey = re.search("bronze", userInput)
            
            pickUpSilverKey = re.search("silver", userInput)
            
            pickUpGoldKey = re.search("gold", userInput)
            
            pickUpKey = re.search("key", userInput)
            
            if pickUpBucket:
                
                inventoryUseable = str(inventory)
                
                bucketGotCheck = re.search("bucket", inventoryUseable)
                
                if bucketGotCheck:
                    
                    print("")
                    
                    print("You already have the bucket")
                    
                    print("")
                    
                    roomFive()
                    
                else:
                
                    print("")
                    
                    print("You pick up the cooler bucket which is full of ice.")
                    
                    print("")
                    
                    inventory.append("bucket")
                    
                    roomFive()
                    
            elif pickUpBronzeKey and pickUpKey:
                
                interactionSaveUseable = str(interactionSave)
                
                panelOpenedCheck = re.search("panelOpened", interactionSaveUseable)
                
                bronzeKeyGotCheck = re.search("bronzeKeyGot", interactionSaveUseable)
                
                if panelOpenedCheck:
                    
                    if bronzeKeyGotCheck:
                        
                        print("")
                        
                        print("You already have the bronze key")
                        
                        print("")
                        
                        roomFive()
                        
                    else:
                    
                        print("")
                        
                        print("You pick up the bronze key and place it in your pocket")
                        
                        print("")
                        
                        inventory.append("bronze key")
                        
                        interactionSave.append("bronzeKeyGot")
                        
                        roomFive()
                        
                else:
                    
                    print("")
                    
                    print("There is no bronze key to pick up")
                    
                    print("")
                    
                    roomFive()
                    
            elif pickUpSilverKey and pickUpKey:
                
                interactionSaveUseable = str(interactionSave)
                
                safeOpenedCheck = re.search("safeOpened", interactionSaveUseable)
                
                silverKeyGotCheck = re.search("silverKeyGot", interactionSaveUseable)
                
                if safeOpenedCheck:
                    
                    if silverKeyGotCheck:
                        
                        print("")
                        
                        print("You already have the silver key")
                        
                        print("")
                        
                        roomFive()
                        
                    else:
                    
                        print("")
                        
                        print("You pick up the silver key from the safe and place it in your pocket")
                        
                        print("")
                        
                        inventory.append("silver key")
                        
                        interactionSave.append("silverKeyGot")
                        
                        roomFive()
                        
                else:
                    
                    print("")
                    
                    print("There is no silver key to pick up")
                    
                    print("")
                    
                    roomFive()
                    
            elif pickUpGoldKey and pickUpKey:
                
                interactionSaveUseable = str(interactionSave)
                
                goldHatchOpenedCheck = re.search("goldHatchOpened", interactionSaveUseable)
                
                goldKeyGotCheck = re.search("goldKeyGot", interactionSaveUseable)
                
                if goldHatchOpenedCheck:
                    
                    if goldKeyGotCheck:
                        
                        print("")
                        
                        print("You already have the gold key")
                        
                        print("")
                        
                        roomFive()
                        
                    else:
                    
                        print("")
                        
                        print("You pick up the gold key from the hatch and place it in your pocket")
                        
                        print("")
                        
                        inventory.append("gold key")
                        
                        interactionSave.append("goldKeyGot")
                        
                        roomFive()
                        
                else:
                    
                    print("")
                    
                    print("There is no gold key to pick up")
                    
                    print("")
                    
                    roomFive()
            
            else:
            
                print("")
                
                print("You can't pick that up")
                
                print("")
                
                roomFive()
            
        elif lookAtAction:
            
            lookAtRustyNecklace = re.search("necklace", userInput)
            
            lookAtMyself = re.search(r"\bself\b", userInput)
            
            lookAtMyselfAlternative = re.search("myself", userInput)
            
            lookAtBody = re.search("body", userInput)
            
            lookAtBodyAlter1 = re.search("corpse", userInput)
            
            lookAtBodyAlter2 = re.search("frank", userInput)
            
            lookAtBodyAlter3 = re.search("walker", userInput)
            
            lookAtBodyAlter4 = re.search("man", userInput)
            
            lookAtDoor = re.search("door", userInput)
            
            lookAtLocks = re.search("lock", userInput)
            
            lookAtFireplace = re.search("fireplace", userInput)
            
            lookAtFireplaceAlternative = re.search("fire", userInput)
            
            lookAtCouch = re.search("couch", userInput)
            
            lookAtCouchAlternative = re.search("lounge", userInput)
            
            lookAtRug = re.search("rug", userInput)
            
            lookAtPainting = re.search("painting", userInput)
            
            lookAtAlcohol = re.search("alcohol", userInput)
            
            lookAtAlcoholAlternative = re.search("wine", userInput)
            
            lookAtGlasses = re.search("glass", userInput)
            
            lookAtGlassesAlternative = re.search("cup", userInput)
            
            lookAtCounter = re.search("counter", userInput)
            
            lookAtCounterAlternative = re.search("cabinet", userInput)
            
            lookAtPaper = re.search("paper", userInput)
            
            if lookAtRustyNecklace:
            
                print("")
                
                print("There is a rusty necklace around your neck, it doesn't have a lock and looks like it can be opened")
                
                print("")
                
                roomFive()
                
            elif lookAtMyself or lookAtMyselfAlternative:
                
                print("""
You look down at yourself, your hands are bruised and see signs of wear, you're wearing a ripped up suit with no tie,
you can't seem to remember anything, and you feel woozy, as if drunk.
                """)
                
                roomFive()
                
            elif lookAtBody or lookAtBodyAlter1 or lookAtBodyAlter2 or lookAtBodyAlter3 or lookAtBodyAlter4:
                
                interactionSaveUseable = str(interactionSave)
                
                livingRoomKillerAliveCheck = re.search("livingRoomKillerAlive", interactionSaveUseable)
                
                livingRoomKillerDeadCheck = re.search("livingRoomKillerDead", interactionSaveUseable)
                    
                if livingRoomKillerAliveCheck:
                        
                        print("")
                        
                        print("The killer lies on the ground, unable to get up.")
                        
                        print("")
                        
                        roomFive()
                        
                elif livingRoomKillerDeadCheck:
                        
                        print("")
                        
                        print("Frank Walker lies dead on the ground. Your duty, finally fulfilled.")
                        
                        print("")
                        
                        roomFive()
                        
                else:
                        
                        print("")
                        
                        print("You can't look at that")
                        
                        print("")
                        
                        roomFive()
                        
            elif lookAtDoor:
                
                print("")
                
                print("The door to escape pure madness is keeping you here through just 3 locks.")
                
                print("")
                
                roomFive()
                
            elif lookAtLocks:
                
                print("")
                
                print("The locks on the door are made of different materials: gold, silver, and bronze.")
                
                print("")
                
                roomFive()
                
            elif lookAtFireplace or lookAtFireplaceAlternative:
                
                interactionSaveUseable = str(interactionSave)
                
                fireOutCheck = re.search("fireOut", interactionSaveUseable)

                if fireOutCheck:
                    
                    print("""
The fireplace has bronze bricks covering it's whole perimeter. There is a panel behind the fireplace which couldn't previously be seen.
A smoldering piece of paper has fallen out of the fireplace and might still be able to be read.
                    """)
                    
                    roomFive()
                    
                else:

                    print("""
The fireplace is burning an aggressive orange and the bricks around it glow a dim bronze.
It's difficult to make out, but the wall behind the fire has a seam in the shape of a rectangle, and might be a hatch,
however the fire is to hot to examine further. There is also a smoldering piece of paper which has fallen out of the fireplace.
                    """)
                
                    roomFive()
                
            elif lookAtCouch or lookAtCouchAlternative:
                
                print("")
                
                print("The couch looks incredibly comfy and is made of a sturdy leather. It rests right in front of the fireplace.")
                
                print("")
                
                roomFive()
            
            elif lookAtRug:
                
                print("") # ? gold key under rug and puzzle
                
                print("The gold and red rug lays on the ground covering a small portion of the room. It isn't stuck to the ground.")
                
                print("")
                
                roomFive()
                
            elif lookAtPainting:
                
                print("") # ? silver key behind painting
                
                print("There is a large painting on top of the fireplace of a man, woman, and child. It has a silver outer frame.")
                
                print("")
                
                roomFive()
                
            elif lookAtAlcohol or lookAtAlcoholAlternative:
                
                print("")
                
                print("The alcohol on top of the cabinet all looks very expensive, and is all very aged. Next to all of the alcohol rests a large bucket, full of ice.")
                        
                print("")
                
                roomFive()
                
            elif lookAtGlasses or lookAtGlassesAlternative:
                
                print("")
                
                print("All of the glasses are unwashed, and have obviously been used recently.")
                
                print("")
                
                roomFive()
                
            elif lookAtCounter or lookAtCounterAlternative:
                
                print("")
                
                print("The counter, or cabinet, holds a vast amount of wine and other alcohols. A large cooling bucket also resides with the alcohol, full of ice.")
                
                print("")
                
                roomFive()
                
            elif lookAtPaper:
                
                print(colored("""
   ███      ██ ███  ██     ██ ███  ██    ███  
           ██       ██    ██  ██           
 █████    ██             ██      ████  █████  
     ██  ██       █     ██         ██      ██ 
██████  ██        ██   ██     ███████ ██████  
                """, f"{theme}", attrs=["bold"]))
                
                print("It looks like a date of some kind, with dashes in between the numbers, but they're hard to make out.")
                
                print("")
                        
                roomFive()
                        
            else:
                
                print("")
                
                print("You can't look at that")
                
                print("")
                
                roomFive()
                
        elif goToTheAction1 and goToTheAction2:
            
            goToTheFirstRoom = re.search("first", userInput)
            
            goToTheFirstRoomAlternative1 = re.search("study", userInput)
            
            goToTheSecondRoom = re.search("second", userInput)
            
            goToTheSecondRoomAlternative1 = re.search("hallway", userInput)
            
            goToTheThirdRoom = re.search("third", userInput)
            
            goToTheThirdRoomAlternative1 = re.search("bedroom", userInput)
            
            goToTheThirdRoomAlternative2 = re.search("left", userInput)
            
            goToTheFourthRoom = re.search("fourth", userInput)
            
            goToTheFourthRoomAlternative1 = re.search("kitchen", userInput)
            
            goToTheFourthRoomAlternative2 = re.search("right", userInput)
            
            goToFinalDoor = re.search("final", userInput)
    
            goToDoor = re.search("door", userInput)
            
            goToRoom = re.search("room", userInput)
            
            if goToFinalDoor and goToDoor or goToDoor:
                
                blankspace()
                    
                time.sleep(2)
                    
                print(colored("That's it", attrs=["bold"]))
                
                print("")
                
                time.sleep(4)
                
                blankspace()
                
                print(colored("You're out", attrs=["bold"]))
                
                print("")
                
                time.sleep(4)
                
                blankspace()
                    
                print(colored("You realise there is no happy ending", attrs=["bold"]))
                
                print("")
                
                time.sleep(4)
                
                blankspace()
                    
                print(colored("You don't leave something like that and smell the flowers the next day", attrs=["bold"]))
                
                print("")
                
                time.sleep(4)
                
                blankspace()
                    
                print(colored("In the end, waking up was your biggest mistake.", attrs=["bold"]))
                
                print("")
                
                time.sleep(4)
                
                blankspace()
                
                print(colored("Until next time,", attrs=["bold"]))
                
                print("")
                
                time.sleep(4)
                
                blankspace()
                    
                print(colored("Mike", f"{theme}", attrs=["bold"]))
                
                print("")
                
                time.sleep(4)
                
                overwrite()
                
                startMenu()
            
            elif goToTheSecondRoom and goToRoom or goToTheSecondRoomAlternative1:
                
                interactionSaveUseable = str(interactionSave)
                    
                mapBeenUseable = str(mapBeen)
                
                secondBeenCheck = re.search("secondBeen", mapBeenUseable)
                
                if secondBeenCheck:
                    
                    print(colored("""
You move back into the second room, the hallway is so quiet that it makes you uneasy
                """, attrs=["bold"]))
                    
                    mapState.clear()
                    
                    mapState.append("2")
                    
                    sanchange = int(sanity[0])
                    
                    sanchange += 1
                    
                    sanity.clear()
                    
                    sanity.append(sanchange)
                    
                    roomTwo()
                    
                else:
                
                    print(hallwayPrompt)
                    
                    mapState.clear()
                    
                    mapState.append("2")
                    
                    mapBeen.append("secondBeen")
                    
                    roomTwo()
                    
            elif goToTheThirdRoom and goToRoom or goToTheThirdRoomAlternative2 and goToDoor or goToTheThirdRoomAlternative1:
                
                mapBeenUseable = str(mapBeen)
                
                interactionSaveUseable = str(interactionSave)
                
                thirdBeenCheck = re.search("thirdBeen", mapBeenUseable)
                
                starLocation3Check = re.search("location3", interactionSaveUseable)
                
                if thirdBeenCheck:
                    
                    print(colored("""
You move back into the third room, its unusual homeliness makes you increasingly uneasy when compared to the atrocities previously seen.
                    """, attrs=["bold"]))
                        
                    mapState.clear()
                    
                    mapState.append("3")
                    
                    sanchange = int(sanity[0])
                    
                    sanchange += 1
                    
                    sanity.clear()
                    
                    sanity.append(sanchange)
                
                    roomThree()
                    
                elif starLocation3Check:
                    
                    interactionSaveUseable = str(interactionSave)
                    
                    bedroomKillerAliveCheck = re.search("bedroomKillerAlive", interactionSaveUseable)
                    
                    bedroomKillerDeadCheck = re.search("bedroomKillerDead", interactionSaveUseable)
                    
                    if bedroomKillerAliveCheck or bedroomKillerDeadCheck:
                        
                        mapState.clear()
                        
                        mapState.append("3")
                        
                        print(colored("""
You move back into the bedroom, its unusual homeliness makes you increasingly uneasy when compared to the atrocities previously seen
                    """, attrs=["bold"]))
                        
                        roomThree()
                        
                    else:
                
                        mapState.clear()
                        
                        mapState.append("3")
                        
                        mapBeen.append("thirdBeen")
                        
                        bedroomKillerThere()
                    
                else:
                    
                    print(bedroomKillerNotThere)
                    print("")
                    mapState.clear()
                    mapState.append("3")
                    mapBeen.append("secondBeen")
                    mapBeen.append("thirdBeen")
                    roomThree()
                    
            elif goToTheFourthRoom and goToRoom or goToTheFourthRoomAlternative2 and goToDoor or goToTheFourthRoomAlternative1:
                
                mapBeenUseable = str(mapBeen)
                
                interactionSaveUseable = str(interactionSave)
                
                fourthBeenCheck = re.search("fourthBeen", mapBeenUseable)
    
                starLocation4Check = re.search("location4", interactionSaveUseable)
                
                if fourthBeenCheck:
                    
                    print(colored("""
You move back into the kitchen, the horrific sight and smell freeze your body stone cold before continuing onward.
                    """, attrs=["bold"]))
                        
                    mapState.clear()
                    
                    mapState.append("4")
                
                    roomFour()
                
                elif starLocation4Check:
                    
                    interactionSaveUseable = str(interactionSave)
                    
                    kitchenKillerAliveCheck = re.search("kitchenKillerAlive", interactionSaveUseable)
                    
                    kitchenKillerDeadCheck = re.search("kitchenKillerDead", interactionSaveUseable)
                    
                    if kitchenKillerAliveCheck or kitchenKillerDeadCheck:
                        
                        mapState.clear()
                        
                        mapState.append("4")
                        
                        print(colored("""
You move back into the kitchen, the horrific sight and smell freeze your body stone cold before continuing onward.
                    """, attrs=["bold"]))
                        
                        roomFour()
                        
                    else:
                
                        mapState.clear()
                        
                        mapState.append("4")
                        
                        mapBeen.append("fourthBeen")
                        
                        kitchenKillerThere()
                    
                else:
                    
                    print(kitchenKillerNotThere)
                    print("")
                    mapState.clear()
                    mapState.append("4")
                    mapBeen.append("secondBeen")
                    mapBeen.append("fourthBeen")
                    roomFour()
                    
            elif goToTheFirstRoom and goToRoom or goToTheFirstRoomAlternative1:
                
                print(colored("""
    You move back into the first room, seeing the blood on the walls again makes you feel uneasy.
                    """, attrs=["bold"]))
                mapState.clear()
                mapState.append("1")
                sanchange = int(sanity[0])
                sanchange += 1
                sanity.clear()
                sanity.append(sanchange)
                roomOne()
        
            else:
            
                print("")
                
                print("You can't go to that")
                
                print("")
                
                roomFive()
                
        elif useWithAction:
            
            useBucketWithFireplace1 = re.search("bucket", userInput)
            
            useBucketWithFireplace2 = re.search("fireplace", userInput)
            
            useBucketWithFireplace2Alternative = re.search("fire", userInput)
            
            useBronzeKeyWithDoor = re.search("bronze", userInput)
            
            useSilverKeyWithDoor = re.search("silver", userInput)
            
            useGoldKeyWithDoor = re.search("gold", userInput)
            
            useKeyWith = re.search("key", userInput)
            
            useWithLock = re.search("lock", userInput)
            
            useWithDoor = re.search("door", userInput)
            
            if useBucketWithFireplace1 and useBucketWithFireplace2 or useBucketWithFireplace1 and useBucketWithFireplace2Alternative:
                
                inventoryUseable = str(inventory)
                
                interactionSaveUseable = str(interactionSave)
                
                bucketGotCheck = re.search("bucket", inventoryUseable)
                
                bucketMeltedCheck = re.search("bucketMelted", interactionSaveUseable)
                
                fireOutCheck = re.search("fireOut", interactionSaveUseable)
                
                if bucketMeltedCheck:
                    
                    if fireOutCheck:
                        
                        print("")
                        
                        print("The fire is already out")
                        
                        print("")
                        
                        roomFive()
                    
                    else:
                    
                        print("")
                        
                        print("You pour the melted water from the bucket and put the flames out, you can now access the panel at the back of the fireplace.")
                        
                        print("")
                        
                        interactionSave.append("fireOut")
                        
                        roomFive()
                        
                else:
                
                    if bucketGotCheck:
                        
                        print("")
                        
                        print("You place the bucket next to the fireplace for a short period of time, and the ice melts, creating a large amount of water.")
                        
                        print("")
                        
                        interactionSave.append("bucketMelted")
                        
                        roomFive()
                        
                    else:
                        
                        print("")
                        
                        print("You don't have a bucket")
                        
                        print("")
                        
                        roomFive()
                        
            elif useBronzeKeyWithDoor and useKeyWith and useWithLock or useBronzeKeyWithDoor and useKeyWith and useWithDoor:
                
                interactionSaveUseable = str(interactionSave)
                
                inventoryUseable = str(inventory)
                
                bronzeKeyUsedCheck = re.search("bronzeKeyUsed", interactionSaveUseable)
                
                silverKeyUsedCheck = re.search("silverKeyUsed", interactionSaveUseable)
                
                goldKeyUsedCheck = re.search("goldKeyUsed", interactionSaveUseable)
                
                bronzeKeyGotCheck = re.search("bronze key", inventoryUseable)
                
                if bronzeKeyUsedCheck and silverKeyUsedCheck and goldKeyUsedCheck:
                    
                    print("")
                    
                    print("All locks are undone, and the door is open.")
                    
                    print("")
                    
                elif bronzeKeyUsedCheck:
                    
                    print("")
                    
                    print("The bronze lock is already unlocked")
                    
                    print("")
                    
                    roomFive()
                    
                else:
                    
                    if bronzeKeyGotCheck:
                        
                        if goldKeyUsedCheck and silverKeyUsedCheck:
                            
                            print("")
                            
                            print("You insert the bronze key into the bronze lock and a click is heard, all locks are undone and the door is open.")
                            
                            print("")
                            
                            interactionSave.append("bronzeKeyUsed")
                            
                            interactionSave.append("finalDoorOpened")
                            
                            bronzeKeyFind = inventory.index("bronze key")
                        
                            inventory.pop(bronzeKeyFind)
                            
                            roomFive()
                            
                        elif goldKeyUsedCheck or silverKeyUsedCheck:
                            
                            print("")
                            
                            print("You insert the bronze key into the bronze lock and a click is hear, there is one more lock to go.")
                            
                            print("")
                            
                            interactionSave.append("bronzeKeyUsed")
                            
                            bronzeKeyFind = inventory.index("bronze key")
                        
                            inventory.pop(bronzeKeyFind)
                            
                            roomFive()
                        
                        else:
                
                            print("")
                            
                            print("You insert the bronze key into the bronze lock and a click is heard, this lock is undone.")
                            
                            print("")
                            
                            interactionSave.append("bronzeKeyUsed")
                            
                            bronzeKeyFind = inventory.index("bronze key")
                            
                            inventory.pop(bronzeKeyFind)
                            
                            roomFive()
                        
                    else:
                        
                        print("")
                        
                        print("You do not have a bronze key to use with the lock")
                        
                        print("")
                        
                        roomFive()
                    
            elif useSilverKeyWithDoor and useKeyWith and useWithLock or useSilverKeyWithDoor and useKeyWith and useWithDoor:
                
                interactionSaveUseable = str(interactionSave)
                
                inventoryUseable = str(inventory)
                
                bronzeKeyUsedCheck = re.search("bronzeKeyUsed", interactionSaveUseable)
                
                silverKeyUsedCheck = re.search("silverKeyUsed", interactionSaveUseable)
                
                goldKeyUsedCheck = re.search("goldKeyUsed", interactionSaveUseable)
                
                silverKeyGotCheck = re.search("silver key", inventoryUseable)
                
                if bronzeKeyUsedCheck and silverKeyUsedCheck and goldKeyUsedCheck:
                    
                    print("")
                    
                    print("All locks are undone, and the door is open.")
                    
                    print("")
                    
                elif silverKeyUsedCheck:
                    
                    print("")
                    
                    print("The silver lock is already unlocked")
                    
                    print("")
                    
                    roomFive()
                    
                else:
                    
                    if silverKeyGotCheck:
                        
                        if bronzeKeyUsedCheck and goldKeyUsedCheck:
                            
                            print("")
                            
                            print("You insert the silver key into the silver lock and a click is heard, all locks are undone and the door is open.")
                            
                            print("")
                            
                            interactionSave.append("silverKeyUsed")
                            
                            interactionSave.append("finalDoorOpened")
                            
                            silverKeyFind = inventory.index("silver key")
                        
                            inventory.pop(silverKeyFind)
                            
                            roomFive()
                            
                        elif bronzeKeyUsedCheck or goldKeyUsedCheck:
                            
                            print("")
                            
                            print("You insert the silver key into the silver lock and a click is hear, there is one more lock to go.")
                            
                            print("")
                            
                            interactionSave.append("silverKeyUsed")
                            
                            silverKeyFind = inventory.index("silver key")
                        
                            inventory.pop(silverKeyFind)
                            
                            roomFive()
                        
                        else:
                
                            print("")
                            
                            print("You insert the silver key into the silver lock and a click is heard, this lock is undone.")
                            
                            print("")
                            
                            interactionSave.append("silverKeyUsed")
                            
                            silverKeyFind = inventory.index("silver key")
                            
                            inventory.pop(silverKeyFind)
                            
                            roomFive()
                        
                    else:
                        
                        print("")
                        
                        print("You do not have a silver key to use with the lock")
                        
                        print("")
                        
                        roomFive()
                    
            elif useGoldKeyWithDoor and useKeyWith and useWithLock or useGoldKeyWithDoor and useKeyWith and useWithDoor:
                
                interactionSaveUseable = str(interactionSave)
                
                inventoryUseable = str(inventory)
                
                bronzeKeyUsedCheck = re.search("bronzeKeyUsed", interactionSaveUseable)
                
                silverKeyUsedCheck = re.search("silverKeyUsed", interactionSaveUseable)
                
                goldKeyUsedCheck = re.search("goldKeyUsed", interactionSaveUseable)
                
                goldKeyGotCheck = re.search("gold key", inventoryUseable)
                
                if bronzeKeyUsedCheck and silverKeyUsedCheck and goldKeyUsedCheck:
                    
                    print("")
                    
                    print("All locks are undone, and the door is open.")
                    
                    print("")
                    
                elif goldKeyUsedCheck:
                    
                    print("")
                    
                    print("The gold lock is already unlocked")
                    
                    print("")
                    
                    roomFive()
                    
                else:
                    
                    if goldKeyGotCheck:
                        
                        if bronzeKeyUsedCheck and silverKeyUsedCheck:
                            
                            print("")
                            
                            print("You insert the gold key into the gold lock and a click is heard, all locks are undone and the door is open.")
                            
                            print("")
                            
                            interactionSave.append("goldKeyUsed")
                            
                            interactionSave.append("finalDoorOpened")
                            
                            goldKeyFind = inventory.index("gold key")
                        
                            inventory.pop(goldKeyFind)
                            
                            roomFive()
                            
                        elif bronzeKeyUsedCheck or silverKeyUsedCheck:
                            
                            print("")
                            
                            print("You insert the gold key into the gold lock and a click is hear, there is one more lock to go.")
                            
                            print("")
                            
                            interactionSave.append("goldKeyUsed")
                            
                            goldKeyFind = inventory.index("gold key")
                        
                            inventory.pop(goldKeyFind)
                            
                            roomFive()
                        
                        else:
                
                            print("")
                            
                            print("You insert the gold key into the gold lock and a click is heard, this lock is undone.")
                            
                            print("")
                            
                            interactionSave.append("goldKeyUsed")
                            
                            goldKeyFind = inventory.index("gold key")
                            
                            inventory.pop(goldKeyFind)
                            
                            roomFive()
                        
                    else:
                        
                        print("")
                        
                        print("You do not have a gold key to use with the lock")
                        
                        print("")
                        
                        roomFive()
            else:
            
                print("")
                
                print("You can't use that with that")
                
                print("")
                
                roomFive()
                
        elif useAction:
            
            useRustyNecklace = re.search("rusty necklace", userInput)
            
            usePanel = re.search("panel", userInput)
            
            useDoor = re.search("door", userInput)
            
            useMap = re.search("map", userInput)
            
            usePainting = re.search("painting", userInput)
            
            useSafe = re.search("safe", userInput)
            
            useRug = re.search("rug", userInput)
            
            useHatch = re.search("hatch", userInput)
            
            if useMap:
                
                mapUse()
            
            elif useRustyNecklace:
            
                print("")
                
                print("You open the rusty necklace on your neck and see a picture of what you think is you and 2 children, it puts you at ease")
                
                print("")
                
                sanchange = int(sanity[0])
    
                sanchange -= 2

                sanity.clear()

                sanity.append(sanchange)
                
                roomFive()
                
            elif usePanel:
                
                interactionSaveUseable = str(interactionSave)
                
                fireOutCheck = re.search("fireOut", interactionSaveUseable)
                
                panelOpenedCheck = re.search("panelOpened", interactionSaveUseable)
                
                if fireOutCheck:
                    
                    if panelOpenedCheck:
                        
                        print("")
                        
                        print("You've already opened the panel at the back of the fireplace")
                        
                        print("")
                        
                        roomFive()
                        
                    else:
                    
                        print("""
You push in the panel at the back of the fireplace and it pops open. It reveals a stash of goods such as money and telescope lenses, but none of that matters now.
The important object is a small, bronze key, placed within all the other goods.
                        """)
                    
                        interactionSave.append("panelOpened")
                        
                        roomFive()
                    
                else:
                    
                    print("")
                    
                    print("You can touch the panel because of the fire in the way, you have to get rid of it somehow.")
                    
                    print("")
                    
                    roomFive()
                    
            elif useDoor:
                
                print("")
                
                print("You turn the knob but nothing happens, the door has three locks and all have to be unlocked to get out.")
                
                print("")
                
                roomFive()
                
            elif usePainting:
                
                print("""
You get up high and manage to take the paining off the wall, placing it to the side. Behind the painting is a large silver safe with a 4 digit combination.
                """)
                
                interactionSave.append("paintingMoved")
                
                roomFive()
                
            elif useSafe:
                
                interactionSaveUseable = str(interactionSave)
                
                safeOpenedCheck = re.search("safeOpened", interactionSaveUseable)
                
                def safeUse():
                    
                    if safeOpenedCheck:
                        
                        print("")
                        
                        print("The safe is already open")
                        
                        print("")
                        
                        roomFive()
                        
                    else:
                        
                        print("")
                        
                        safeCombo = input("You approach the safe, what's the passcode? (type \"0\" to leave at anytime): ")
                        
                        if safeCombo == "3753":
                            
                            print("")
                            
                            print("The safe pops open, a stash of valuables are inside, but the most important is a small silver key.")
                            
                            print("")
                            
                            interactionSave.append("safeOpened") 
                            
                            roomFive()
                            
                        elif safeCombo == "0":
                            
                            print("")
                            
                            print("You don't know the code at this current time, and decide to keep searching.")
                            
                            print("")
                            
                            roomFive()
                            
                        else:
                            
                            print("")
                            
                            print(f"You input {safeCombo} but nothing happens, the safe asks for the code again.")
                            
                            print("")
                            
                            safeUse()
        
                safeUse()
                
            elif useRug:
                
                interactionSaveUseable = str(interactionSave)
                
                goldKeyRugMovedCheck = re.search("goldKeyRugMoved", interactionSaveUseable)
                    
                if goldKeyRugMovedCheck:
                    
                    print("")
                    
                    print("You have already rolled up the rug and put it to the side, it revealed a golden hatch.")
                    
                    print("")
                    
                    roomFive()
                    
                else:
                
                    print("")
                    
                    print("You roll up the rug and put it in a corner and there it is, a familiar, but now golden hatch.")
                    
                    print("")
                    
                    interactionSave.append("goldKeyRugMoved") # ? SAVE AND LOAD THIS
                    
                    roomFive()
                
            elif useHatch:
                
                interactionSaveUseable = str(interactionSave)
                
                goldHatchOpenedCheck = re.search("goldHatchOpened", interactionSaveUseable)
                
                goldKeyGotCheck = re.search("goldKeyGot", interactionSaveUseable)
                
                if goldHatchOpenedCheck:
                    
                    if goldKeyGotCheck:
                        
                        print("")
                        
                        print("The hatch is open and is now empty")
                        
                        print("")
                        
                        roomFive()
                        
                    else:
                    
                        print("")
                        
                        print("The hatch is already open and a gold key is inside")
                        
                        print("")
                        
                        roomFive()
                    
                else:
                    
                    print("")
                    
                    print("You open the golden hatch and there is only one object, a small, golden key.")
                    
                    print("")
                    
                    interactionSave.append("goldHatchOpened") # ? SAVE AND LOAD THIS 
                    
                    roomFive()

            else:
                
                print("")
                
                print("You can't use that")
                
                print("")
                
                roomFive()
            
        else:
            
            print("")
            
            print("That isn't a valid input")
            
            print("")
            
            roomFive()
            
    def death():
        
        overwrite()
        
        deathPrompt = (colored("""
▓██   ██▓ ▒█████   █    ██    ▓█████▄  ██▓▓█████ ▓█████▄    
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▒██▀ ██▌▓██▒▓█   ▀ ▒██▀ ██▌   
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ░██   █▌▒██▒▒███   ░██   █▌   
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░▓█▄   ▌░██░▒▓█  ▄ ░▓█▄   ▌   
  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░▒████▓ ░██░░▒████▒░▒████▓    
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒     ▒▒▓  ▒ ░▓  ░░ ▒░ ░ ▒▒▓  ▒    
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░     ░ ▒  ▒  ▒ ░ ░ ░  ░ ░ ▒  ▒    
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░     ░ ░  ░  ▒ ░   ░    ░ ░  ░    
 ░ ░         ░ ░     ░           ░     ░     ░  ░   ░       
 ░ ░                           ░                  ░         

As soon as you see him he smells you, your body freezes and there's no stopping your imminent demise.
He kills you the same way they all died, strangled with black gloves and laughing maniacally.
You failed and he knows you failed.
            """, f"{theme}", attrs=["bold"]))

        time.sleep(0.3)
        
        print(deathPrompt)
        
        def deathInput():
            
            restartInput = input(colored("Do you want to restart? (Y/N): ", attrs=["bold"])).upper()
            
            if restartInput == "Y":
                
                game()
                
            elif restartInput == "N":
                
                startMenu()
                
            else:
                
                print("")
                
                print("That is not a valid input")
                
                print("")
                
                time.sleep(2)
                
                deathInput()
                
        deathInput()
        
    def incapicatate():
        
        inventoryUseable = str(inventory)
        
        mapStateUseable = str(mapState)
        
        pistolCheck = re.search("pistol", inventoryUseable)
        
        knifeCheck = re.search("knife", inventoryUseable)
        
        mapState3Check = re.search("3", mapStateUseable)
        
        mapState4Check = re.search("4", mapStateUseable)
        
        mapState5Check = re.search("5", mapStateUseable)
        
        if pistolCheck:
            
            blankspace()
                
            time.sleep(4)
            
            print(colored("One shot, eyes closed, point blank.", f"{theme}", attrs=["bold"]))
            
            print("")
            
            time.sleep(6)
            
            blankspace()
                
            print(colored("After one long, loud scream, a thud is heard.", attrs=["bold"]))
            
            print("")
            
            time.sleep(4)
            
            blankspace()
                
            print(colored("He's dropped to the floor", attrs=["bold"]))
            
            print("")
            
            time.sleep(4)
            
            blankspace()
                
            print(colored("He isn't dead", attrs=["bold"]))
            
            print("")
            
            time.sleep(4)
            
            blankspace()
                
            time.sleep(6)
            
            def finishOff():
            
                finishOffInp = input(colored("Finish him off? (Y/N): ", f"{theme}", attrs=["bold"])).upper()
                
                if finishOffInp == "Y":
                    
                    blankspace()
                        
                    time.sleep(4)
                    
                    print(colored("Two shots", attrs=["bold"]))
                    
                    print("")
                    
                    time.sleep(4)
                    
                    blankspace()
                        
                    time.sleep(4)
                    
                    print(colored("His screams stop.", attrs=["bold"]))
                    
                    print("")
                    
                    sanchange = int(sanity[0])
                    
                    sanchange += 15
                    
                    sanity.clear()
                    
                    sanity.append(sanchange)
                    
                    time.sleep(4)
                    
                    blankspace()
                        
                    if mapState3Check:
                        
                        interactionSave.append("bedroomKillerDead")
                        
                        print(bedroomKillerDead)
                        
                        bedroomKillerNotThere = bedroomKillerDead
                        
                        roomThree()
                    
                    elif mapState4Check:
                        
                        interactionSave.append("kitchenKillerDead")
                        
                        print(kitchenKillerDead)
                        
                        kitchenKillerNotThere = kitchenKillerDead
                        
                        roomFour()
                        
                    elif mapState5Check:
                        
                        interactionSave.append("livingRoomKillerDead")
                        
                        print(livingRoomKillerDead)
                        
                        livingRoomKillerNotThere = livingRoomKillerDead
                        
                        roomFive()
                    
                elif finishOffInp == "N":
                    
                    blankspace()
                        
                    print(colored("You leave him there, writhing in pain on the ground, and try to save yourself.", attrs=["bold"]))
                    
                    print("")
                    
                    sanchange = int(sanity[0])
                    
                    sanchange += 6
                    
                    sanity.clear()
                    
                    sanity.append(sanchange)
                    
                    time.sleep(6)
                    
                    blankspace()
                        
                    if mapState3Check:
                        
                        interactionSave.append("bedroomKillerAlive")
                        
                        print(bedroomKillerAlive)
                        
                        bedroomKillerNotThere = bedroomKillerAlive
                        
                        roomThree()
                        
                    elif mapState4Check:
                        
                        interactionSave.append("kitchenKillerAlive")
                        
                        print(kitchenKillerAlive)
                        
                        kitchenKillerNotThere = kitchenKillerAlive
                        
                        roomFour()
                        
                    elif mapState5Check:
                        
                        interactionSave.append("livingRoomKillerAlive")
                        
                        print(livingRoomKillerAlive)
                        
                        livingRoomKillerNotThere = livingRoomKillerAlive
                        
                        roomFive()
                
                else:
                    
                    print("")
                    
                    print("That isn't a valid input")
                    
                    print("")
                    
                    time.sleep(2)
                    
                    finishOff()
                    
            finishOff()
                                
        if knifeCheck:
            
            blankspace()
                
            time.sleep(4)
            
            print(colored("Direct hit, pushed in, blank mind", f"{theme}", attrs=["bold"]))
            
            print("")
            
            time.sleep(4)
            
            blankspace()
                
            print(colored("After one long, loud scream, a thud is heard.", attrs=["bold"]))
            
            print("")
            
            time.sleep(4)
            
            blankspace()
                
            print(colored("He's dropped to the floor", attrs=["bold"]))
            
            print("")
            
            time.sleep(4)
            
            blankspace()
                
            print(colored("He isn't dead", attrs=["bold"]))
            
            print("")
            
            time.sleep(4)
            
            blankspace()
                
            time.sleep(6)
            
            def finishOff():
                
                finishOffInp = input(colored("Finish him off? (Y/N): ", f"{theme}", attrs=["bold"])).upper()
                
                if finishOffInp == "Y":
                    
                    blankspace()
                        
                    time.sleep(4)
                    
                    print(colored("Eight more slashes", attrs=["bold"]))
                    
                    print("")
                    
                    time.sleep(4)
                    
                    blankspace()
                        
                    time.sleep(4)
                    
                    print(colored("His screams stop.", attrs=["bold"]))
                    
                    print("")
                    
                    sanchange = int(sanity[0])
                    
                    sanchange += 15
                    
                    sanity.clear()
                    
                    sanity.append(sanchange)
                    
                    time.sleep(6)
                    
                    blankspace()
                        
                    if mapState3Check:
                        
                        interactionSave.append("bedroomKillerDead")
                        
                        print(bedroomKillerDead)
                    
                        bedroomKillerNotThere = bedroomKillerDead
                        
                        roomThree()
                        
                    elif mapState4Check:
                        
                        interactionSave.append("kitchenKillerDead")
                        
                        print(kitchenKillerDead)
                        
                        kitchenKillerNotThere = kitchenKillerDead
                        
                        roomFour()
                        
                    elif mapState5Check:
                        
                        interactionSave.append("livingRoomKillerDead")
                        
                        print(livingRoomKillerDead)
                        
                        livingRoomKillerNotThere = livingRoomKillerDead
                        
                        roomFive()
                    
                elif finishOffInp == "N":
                    
                    blankspace()
                        
                    print(colored("You leave him there, writhing in pain on the ground, and try to save yourself.", attrs=["bold"]))
                    
                    print("")
                    
                    sanchange = int(sanity[0])
                    
                    sanchange += 6
                    
                    sanity.clear()
                    
                    sanity.append(sanchange)
                    
                    time.sleep(6)
                    
                    blankspace()
                        
                    if mapState3Check:
                        
                        interactionSave.append("bedroomKillerAlive")
                        
                        print(bedroomKillerAlive)
                        
                        bedroomKillerNotThere = bedroomKillerAlive
                        
                        roomThree()
                        
                    elif mapState4Check:
                        
                        interactionSave.append("kitchenKillerAlive")
                        
                        print(kitchenKillerAlive)
                    
                        kitchenKillerNotThere = kitchenKillerAlive
                        
                        roomFour()
                        
                    elif mapState5Check:
                        
                        interactionSave.append("livingRoomKillerAlive")
                        
                        print(livingRoomKillerAlive)
                        
                        livingRoomKillerNotThere = livingRoomKillerAlive
                        
                        roomFive()
                
                else:
                    
                    print("")
                    
                    print("That isn't a valid input")
                    
                    print("")
                    
                    time.sleep(2)
                    
                    finishOff()
                    
            finishOff()
            
    def save():
        
        inventoryUseable = str(inventory)

        interactionSaveUseable = str(interactionSave)
    
        mapStateUseable = str(mapState)
        
        saveState = open(saveStateLocation, "rt")
        
        saveSanityState = open(saveStateLocation)
        
        saveContent = saveState.read()
        
        saveSanity = saveSanityState.readlines()
        
        sancheck = int(sanity[0])
        
        # ? SANITY CHECKS ----------------------------------------------------------------------------------
        
        sanfind = saveSanity[1]
        
        sanfind = sanfind.replace("Sanity=", "")
        
        sanfind = int(sanfind)
        
        saveContent = saveContent.replace(f"Sanity={sanfind}", f"Sanity={sancheck}")
            
        saveState.close()
        
        saveState = open(saveStateLocation, "wt")
        
        saveState.write(saveContent)
        
        saveState.close()
    
        # ? INVENTORY CHECKS --------------------------------------------------------------------------------
        
        rustyNecklaceGotCheck = re.search("necklace", inventoryUseable)
        
        rustyKeyGotCheck = re.search("key", inventoryUseable)
        
        pristineKeyGotCheck = re.search("pristine", inventoryUseable)
        
        featherGotCheck = re.search("feather", inventoryUseable)
        
        paperGotCheck = re.search("paper", inventoryUseable)
        
        quillGotCheck = re.search("quill", inventoryUseable)
        
        mapGotCheck = re.search("map", inventoryUseable)
    
        knifeGotCheck = re.search("knife", inventoryUseable)
        
        pistolGotCheck = re.search("pistol", inventoryUseable)
    
        crowbarGotCheck = re.search("crowbar", inventoryUseable)
        
        handTrolleyGotCheck = re.search("hand trolley", inventoryUseable)
        
        bucketGotCheck = re.search("bucket", inventoryUseable)
        
        bronzeKeyGotCheck = re.search("bronze key", inventoryUseable)
        
        silverKeyGotCheck = re.search("silver key", inventoryUseable)
        
        goldKeyGotCheck = re.search("gold key", inventoryUseable)
        
        if crowbarGotCheck:
            
            saveContent = saveContent.replace("CrowbarGot=False", "CrowbarGot=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if handTrolleyGotCheck:
            
            saveContent = saveContent.replace("HandTrolleyGot=False", "HandTrolleyGot=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
        
        if rustyNecklaceGotCheck:
            
            saveContent = saveContent.replace("RustyNecklaceGot=False", "RustyNecklaceGot=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
        
        if rustyKeyGotCheck:
            
            saveContent = saveContent.replace("RustyKeyGot=False", "RustyKeyGot=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if pristineKeyGotCheck:
            
            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("PristineKeyGot=False", "PristineKeyGot=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if featherGotCheck:
            
            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("FeatherGot=False", "FeatherGot=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if paperGotCheck:
            
            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("PaperGot=False", "PaperGot=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if quillGotCheck:
            
            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("QuillGot=False", "QuillGot=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if mapGotCheck:
                
            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("MapGot=False", "MapGot=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
        
        if knifeGotCheck:
            
            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("KnifeGot=False", "KnifeGot=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if pistolGotCheck:
            
            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("PistolGot=False", "PistolGot=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if bucketGotCheck:
            
            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("BucketGot=False", "BucketGot=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if bronzeKeyGotCheck:
            
            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("BronzeKeyGot=False", "BronzeKeyGot=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if silverKeyGotCheck:
            
            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("SilverKeyGot=False", "SilverKeyGot=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
        
        if goldKeyGotCheck:
            
            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("GoldKeyGot=False", "GoldKeyGot=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        # ? INTERACTION CHECKS --------------------------------------------------------------------------------
        
        boxOpenedCheck = re.search("boxOpened", interactionSaveUseable)

        doorOpenedCheck = re.search("doorOpened", interactionSaveUseable)
        
        quillMadeCheck = re.search("quillMade", interactionSaveUseable)
        
        mapMadeCheck = re.search("mapMade", interactionSaveUseable)
        
        rugMovedCheck = re.search("rugMoved", interactionSaveUseable)
        
        hatchOpenedCheck = re.search("hatchOpened", interactionSaveUseable)
        
        bodyFlippedCheck = re.search("bodyFlipped", interactionSaveUseable)
        
        bedroomDrawerOpenedCheck = re.search("bedroomDrawerOpened", interactionSaveUseable)
        
        letterOpenedCheck = re.search("letterOpened", interactionSaveUseable)
        
        potLookedAtCheck = re.search("potLookedAt", interactionSaveUseable)
        
        grinderTurnedCheck = re.search("grinderTurned", interactionSaveUseable)
        
        bedroomKillerAliveCheck = re.search("bedroomKillerAlive", interactionSaveUseable)
        
        bedroomKillerDeadCheck = re.search("bedroomKillerDead", interactionSaveUseable)
        
        kitchenKillerAliveCheck = re.search("kitchenKillerAlive", interactionSaveUseable)
        
        kitchenKillerDeadCheck = re.search("kitchenKillerDead", interactionSaveUseable)
        
        livingRoomKillerAliveCheck = re.search("livingRoomKillerAlive", interactionSaveUseable)
        
        livingRoomKillerDeadCheck = re.search("livingRoomKillerDead", interactionSaveUseable)
        
        wardrobeUprightCheck = re.search("wardrobeUpright", interactionSaveUseable)
        
        handTrolleyDroppedOffCheck = re.search("handTrolleyDroppedOff", interactionSaveUseable)
        
        wardrobeMovedTrolleyCheck = re.search("wardrobeMovedTrolley", interactionSaveUseable)
        
        bucketMeltedCheck = re.search("bucketMelted", interactionSaveUseable)
        
        fireOutCheck = re.search("fireOut", interactionSaveUseable)
        
        panelOpenedCheck = re.search("panelOpened", interactionSaveUseable)
        
        bronzeKeyUsedCheck = re.search("bronzeKeyUsed", interactionSaveUseable)
        
        bronzeKeyGotInterCheck = re.search("bronzeKeyGot", interactionSaveUseable)
        
        silverKeyUsedCheck = re.search("silverKeyUsed", interactionSaveUseable)
        
        silverKeyGotInterCheck = re.search("silverKeyGot", interactionSaveUseable)
        
        goldKeyUsedCheck = re.search("goldKeyUsedCheck", interactionSaveUseable)
        
        goldKeyGotInterCheck = re.search("goldKeyGot", interactionSaveUseable)
        
        paintingMovedCheck = re.search("paintingMoved", interactionSaveUseable)
        
        safeOpenedCheck = re.search("safeOpened", interactionSaveUseable)
        
        goldKeyRugMovedCheck = re.search(r"\bgoldKeyRugMoved\b", interactionSaveUseable)
        
        goldHatchOpenedCheck = re.search(r"\bgoldHatchOpened\b", interactionSaveUseable)
        
        finalDoorOpenedCheck = re.search(r"\bfinalDoorOpened\b", interactionSaveUseable)
        
        if goldKeyRugMovedCheck:

            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("GoldKeyRugMoved=False", "GoldKeyRugMoved=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if goldHatchOpenedCheck:

            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("GoldHatchOpened=False", "GoldHatchOpened=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if finalDoorOpenedCheck:

            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("FinalDoorOpened=False", "FinalDoorOpened=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
        
        if paintingMovedCheck:

            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("PaintingMoved=False", "PaintingMoved=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if safeOpenedCheck:

            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("SafeOpened=False", "SafeOpened=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
        
        if wardrobeMovedTrolleyCheck:

            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("WardrobeMovedTrolley=False", "WardrobeMovedTrolley=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if panelOpenedCheck:

            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("PanelOpened=False", "PanelOpened=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
        
        if handTrolleyDroppedOffCheck:

            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("HandTrolleyDroppedOff=False", "HandTrolleyDroppedOff=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
        
        if boxOpenedCheck:

            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("BoxOpened=False", "BoxOpened=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if wardrobeUprightCheck:
            
            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("WardrobeUpright=False", "WardrobeUpright=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if doorOpenedCheck:
            
            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("DoorOpened=False", "DoorOpened=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if quillMadeCheck:
            
            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("QuillMade=False", "QuillMade=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if mapMadeCheck:
            
            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("MapMade=False", "MapMade=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if rugMovedCheck:
            
            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("RugMoved=False", "RugMoved=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if hatchOpenedCheck:
            
            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("HatchOpened=False", "HatchOpened=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if bodyFlippedCheck:
            
            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("BodyFlipped=False", "BodyFlipped=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
    
        if bedroomDrawerOpenedCheck:
            
            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("BedroomDrawerOpened=False", "BedroomDrawerOpened=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if letterOpenedCheck:
            
            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("LetterOpened=False", "LetterOpened=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if potLookedAtCheck:
            
            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("PotLookedAt=False", "PotLookedAt=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if grinderTurnedCheck:
            
            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("GrinderTurned=False", "GrinderTurned=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if bedroomKillerAliveCheck:
            
            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("BedroomKillerAlive=False", "BedroomKillerAlive=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if bedroomKillerDeadCheck:
            
            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("BedroomKillerDead=False", "BedroomKillerDead=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if kitchenKillerAliveCheck:
            
            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("KitchenKillerAlive=False", "KitchenKillerAlive=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if kitchenKillerDeadCheck:
            
            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("KitchenKillerDead=False", "KitchenKillerDead=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if livingRoomKillerAliveCheck:
            
            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("LivingRoomKillerAlive=False", "LivingRoomKillerAlive=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if livingRoomKillerDeadCheck:
            
            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("livingRoomKillerDead=False", "livingRoomKillerDead=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if bucketMeltedCheck:

            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("BucketMelted=False", "BucketMelted=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if fireOutCheck:

            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("FireOut=False", "FireOut=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if bronzeKeyUsedCheck:

            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("BronzeKeyUsed=False", "BronzeKeyUsed=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if bronzeKeyGotInterCheck:

            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("BronzeKeyGotInter=False", "BronzeKeyGotInter=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if silverKeyUsedCheck:

            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("SilverKeyUsed=False", "SilverKeyUsed=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if silverKeyGotInterCheck:

            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("SilverKeyGotInter=False", "SilverKeyGotInter=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if goldKeyUsedCheck:

            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("GoldKeyUsed=False", "GoldKeyUsed=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if goldKeyGotInterCheck:

            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("GoldKeyGotInter=False", "GoldKeyGotInter=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
        
        # ? MAP STATE CHECKS --------------------------------------------------------------------------------
        
        roomOneCheck = re.search("1", mapStateUseable)
        roomTwoCheck = re.search("2", mapStateUseable)
        roomThreeCheck = re.search("3", mapStateUseable)
        roomFourCheck = re.search("4", mapStateUseable)
        roomFiveCheck = re.search("5", mapStateUseable)
        
        if roomOneCheck:
            
            saveState = open(saveStateLocation, "rt")
            
            mapContent = saveState.read()
            
            comingFromTwoSave = re.search("SecondRoom=True", mapContent)
            
            comingFromThreeSave = re.search("ThirdRoom=True", mapContent)
            
            comingFromFourSave = re.search("FourthRoom=True", mapContent)

            comingFromFiveSave = re.search("FifthRoom=True", mapContent)
            
            if comingFromTwoSave:
                
                saveContent = saveContent.replace("SecondRoom=True", "SecondRoom=False")
                
            if comingFromThreeSave:
                
                saveContent = saveContent.replace("ThirdRoom=True", "ThirdRoom=False")
                
            if comingFromFourSave:
                
                saveContent = saveContent.replace("FourthRoom=True", "FourthRoom=False")
                
            if comingFromFiveSave:
                
                saveContent = saveContent.replace("FifthRoom=True", "FifthRoom=False")
                
            saveContent = saveContent.replace("FirstRoom=False", "FirstRoom=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        if roomTwoCheck:
            
            saveState = open(saveStateLocation, "rt")
            
            mapContent = saveState.read()
            
            comingFromOneSave = re.search("FirstRoom=True", mapContent)
            
            comingFromThreeSave = re.search("ThirdRoom=True", mapContent)
            
            comingFromFourSave = re.search("FourthRoom=True", mapContent)

            comingFromFiveSave = re.search("FifthRoom=True", mapContent)
            
            if comingFromOneSave:
                
                saveContent = saveContent.replace("FirstRoom=True", "FirstRoom=False")
                
            if comingFromThreeSave:
                
                saveContent = saveContent.replace("ThirdRoom=True", "ThirdRoom=False")
                
            if comingFromFourSave:
                
                saveContent = saveContent.replace("FourthRoom=True", "FourthRoom=False")
                
            if comingFromFiveSave:
                
                saveContent = saveContent.replace("FifthRoom=True", "FifthRoom=False")

            saveContent = saveContent.replace("SecondRoom=False", "SecondRoom=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()

        if roomThreeCheck:
            
            saveState = open(saveStateLocation, "rt")
            
            mapContent = saveState.read()
            
            comingFromOneSave = re.search("FirstRoom=True", mapContent)
            
            comingFromTwoSave = re.search("SecondRoom=True", mapContent)
            
            comingFromFourSave = re.search("FourthRoom=True", mapContent)

            comingFromFiveSave = re.search("FifthRoom=True", mapContent)
            
            if comingFromOneSave:
                
                saveContent = saveContent.replace("FirstRoom=True", "FirstRoom=False")
                
            if comingFromTwoSave:
                
                saveContent = saveContent.replace("SecondRoom=True", "SecondRoom=False")
                
            if comingFromFourSave:
                
                saveContent = saveContent.replace("FourthRoom=True", "FourthRoom=False")
                
            if comingFromFiveSave:
                
                saveContent = saveContent.replace("FifthRoom=True", "FifthRoom=False")
            
            saveContent = saveContent.replace("ThirdRoom=False", "ThirdRoom=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
        
        if roomFourCheck:
            
            saveState = open(saveStateLocation, "rt")
            
            mapContent = saveState.read()
            
            comingFromOneSave = re.search("FirstRoom=True", mapContent)
            
            comingFromThreeSave = re.search("ThirdRoom=True", mapContent)
            
            comingFromTwoSave = re.search("SecondRoom=True", mapContent)

            comingFromFiveSave = re.search("FifthRoom=True", mapContent)
            
            if comingFromOneSave:
                
                saveContent = saveContent.replace("FirstRoom=True", "FirstRoom=False")
                
            if comingFromThreeSave:
                
                saveContent = saveContent.replace("ThirdRoom=True", "ThirdRoom=False")
                
            if comingFromTwoSave:
                
                saveContent = saveContent.replace("SecondRoom=True", "SecondRoom=False")
                
            if comingFromFiveSave:
                
                saveContent = saveContent.replace("FifthRoom=True", "FifthRoom=False")

            saveContent = saveContent.replace("FourthRoom=False", "FourthRoom=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
        
        if roomFiveCheck:
        
            saveState = open(saveStateLocation, "rt")
            
            mapContent = saveState.read()
            
            comingFromOneSave = re.search("FirstRoom=True", mapContent)
            
            comingFromThreeSave = re.search("ThirdRoom=True", mapContent)
            
            comingFromFourSave = re.search("FourthRoom=True", mapContent)

            comingFromTwoSave = re.search("SecondRoom=True", mapContent)
            
            if comingFromTwoSave:
                
                saveContent = saveContent.replace("FirstRoom=True", "FirstRoom=False")
                
            if comingFromThreeSave:
                
                saveContent = saveContent.replace("ThirdRoom=True", "ThirdRoom=False")
                
            if comingFromFourSave:
                
                saveContent = saveContent.replace("FourthRoom=True", "FourthRoom=False")
                
            if comingFromTwoSave:
                
                saveContent = saveContent.replace("SecondRoom=True", "SecondRoom=False")
                
            saveContent = saveContent.replace("FifthRoom=False", "FifthRoom=True")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        # ? LOCATION CHECK --------------------------------------------------------------------------------
        
        interactionSaveUseable = str(interactionSave)
        
        location3Check = re.search("location3", interactionSaveUseable)
        
        location4Check = re.search("location4", interactionSaveUseable)
        
        location5Check = re.search("location5", interactionSaveUseable)
        
        if location3Check:
            
            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("Location=0", "Location=3")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        elif location4Check:
            
            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("Location=0", "Location=4")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        elif location5Check:
            
            saveState = open(saveStateLocation, "rt")
            
            saveContent = saveContent.replace("Location=0", "Location=5")
            
            saveState.close()
            
            saveState = open(saveStateLocation, "wt")
            
            saveState.write(saveContent)
            
            saveState.close()
            
        print("")
        
        print("Game saved successfully!")

        print("")
        
        mapStateUseable = str(mapState)
        
        exitCheckUseable = str(exitCheck)
        
        exitCheckCommencing = re.search("exit", exitCheckUseable)
        
        if exitCheckCommencing:
            
            exitCheck.clear()
            sys.exit()
            
        else:
                
            roomCheckOne = re.search("1", mapStateUseable)
            
            roomCheckTwo = re.search("2", mapStateUseable)
            
            roomCheckThree = re.search("3", mapStateUseable)
            
            roomCheckFour = re.search("4", mapStateUseable)

            roomCheckFive = re.search("5", mapStateUseable)
            
            if roomCheckOne:
                
                roomOne()
                
            elif roomCheckTwo:
                
                roomTwo()
                
            elif roomCheckThree:
                
                roomThree()
                
            elif roomCheckFour:
                
                roomFour()
                
            elif roomCheckFive:

                roomFive()
        
    def mapUse():
        
        inventoryUseable = str(inventory)
        
        mapMadeCheck = re.search("map", inventoryUseable)
        
        if mapMadeCheck:
            
            mapStateUseable = str(mapState)

            mapProgressionUseable = str(mapProgression)
            
            mapState1 = re.search("1", mapStateUseable)
            
            mapState2 = re.search("2", mapStateUseable)
            
            mapState3 = re.search("3", mapStateUseable)
            
            mapState4 = re.search("4", mapStateUseable)
            
            mapState5 = re.search("5", mapStateUseable)
            
            mapProgress33 = re.search("33", mapProgressionUseable)
            
            mapProgress66 = re.search("66", mapProgressionUseable) 
            
            mapProgress100 = re.search("100", mapProgressionUseable)
            
            if mapState1:

                if mapProgress33:

                    print("""
______________________
|               |    |
|               |    |
|               |    |       
|               |    |
|               |____|
|       X       \\\       
|               |----|
|               |    |
|               |    | 
|               |    |         
|               |    | 
----------------------

X = You
\\\ = Door
                    """)
                    
                    roomOne()
                    
                elif mapProgress66:
                    
                    print("""
_________________________________
|               |    |          |        
|               |    |          |        
|               |    |          |               
|               |    |  |_______|               
|               |____|\\\|_______|               
|       X       \\\              \\\                
|               |----|\\\|-------|               
|               |    |  |-------|               
|               |    |          |               
|               |    |          |               
|               |    |          |            
---------------------------------

X = You
\\\ = Door
                    """)
                    
                    roomOne()
                    
                elif mapProgress100:
                    
                    print("""
_________________________________________________
|               |    |          |               |
|               |    |          |               |
|               |    |          |               |
|               |    |  |_______|               |
|               |____|\\\|_______|               |
|       X       \\\              \\\             \\\  
|               |----|\\\|-------|               |
|               |    |  |-------|               |
|               |    |          |               |
|               |    |          |               |
|               |    |          |               |
-------------------------------------------------

X = You
\\\ = Door
                    """)
    
                    roomOne()
                    
                else:
                    
                    mapProgression.clear()
                    mapProgression.append("33")
                    mapUse()
                    
                
            elif mapState2:
                    
                if mapProgress66:
                    
                    print("""
_________________________________
|               |    |          |        
|               |    |          |        
|               |    |          |               
|               |    |  |_______|               
|               |____|\\\|_______|               
|               \\\ X            \\\                
|               |----|\\\|-------|               
|               |    |  |-------|               
|               |    |          |               
|               |    |          |               
|               |    |          |            
---------------------------------

X = You
\\\ = Door
                    """)
                    
                    roomTwo()
                    
                elif mapProgress100:
                    
                    print("""
_________________________________________________
|               |    |          |               |
|               |    |          |               |
|               |    |          |               |
|               |    |  |_______|               |
|               |____|\\\|_______|               |
|               \\\ X             \\\             \\\  
|               |----|\\\|-------|               |
|               |    |  |-------|               |
|               |    |          |               |
|               |    |          |               |
|               |    |          |               |
-------------------------------------------------

X = You
\\\ = Door
                    """)
                    
                    roomTwo()
                    
                else: 
                    
                    mapProgression.clear()
                    mapProgression.append("66")
                    mapUse()
                
            elif mapState3:

                if mapProgress66:
                    
                    print("""
_________________________________
|               |    |          |        
|               |    |     X    |        
|               |    |          |               
|               |    |  |_______|               
|               |____|\\\|_______|               
|               \\\              \\\                
|               |----|\\\|-------|               
|               |    |  |-------|               
|               |    |          |               
|               |    |          |               
|               |    |          |            
---------------------------------

X = You
\\\ = Door
                    """)
                    
                    roomThree()
                    
                elif mapProgress100:
                    
                    print("""
_________________________________________________
|               |    |          |               |
|               |    |     X    |               |
|               |    |          |               |
|               |    |  |_______|               |
|               |____|\\\|_______|               |
|               \\\              \\\             \\\  
|               |----|\\\|-------|               |
|               |    |  |-------|               |
|               |    |          |               |
|               |    |          |               |
|               |    |          |               |
-------------------------------------------------

X = You
\\\ = Door
                    """)
                    
                    roomThree()
                    
                else:
                    
                    mapProgression.clear()
                    mapProgression.append("66")
                    mapUse()
                
            elif mapState4:
                
                if mapProgress66:
                    
                    print("""
_________________________________
|               |    |          |        
|               |    |          |        
|               |    |          |               
|               |    |  |_______|               
|               |____|\\\|_______|               
|               \\\              \\\                
|               |----|\\\|-------|               
|               |    |  |-------|               
|               |    |          |               
|               |    |     X    |               
|               |    |          |            
---------------------------------

X = You
\\\ = Door
                    """)
                    
                    roomFour()
                    
                elif mapProgress100:
                    
                    print("""
_________________________________________________
|               |    |          |               |
|               |    |          |               |
|               |    |          |               |
|               |    |  |_______|               |
|               |____|\\\|_______|               |
|               \\\              \\\             \\\  
|               |----|\\\|-------|               |
|               |    |  |-------|               |
|               |    |          |               |
|               |    |     X    |               |
|               |    |          |               |
-------------------------------------------------

X = You
\\\ = Door
                    """)
                    
                    roomFour()
                
                else:
                    
                    mapProgression.clear()
                    mapProgression.append("66")
                    mapUse()

            elif mapState5:
                
                if mapProgress100:
                
                    print("""
_________________________________________________
|               |    |          |               |
|               |    |          |               |
|               |    |          |               |
|               |    |  |_______|               |
|               |____|\\\|_______|               |
|               \\\              \\\      X      \\\  
|               |----|\\\|-------|               |
|               |    |  |-------|               |
|               |    |          |               |
|               |    |          |               |
|               |    |          |               |
-------------------------------------------------

X = You
\\\ = Door
                    """)
                    
                    roomFive()
                    
                else:
                    
                    mapProgression.clear()
                    mapProgression.append("100")
                    mapUse()

        else:
            
            mapStateUseable = str(mapState)
            
            mapState1 = re.search("1", mapStateUseable)
            
            mapState2 = re.search("2", mapStateUseable)
            
            mapState3 = re.search("3", mapStateUseable)
            
            mapState4 = re.search("4", mapStateUseable)
            
            mapState5 = re.search("5", mapStateUseable)
            
            print("")
            
            print("You don't have a map")
            
            print("")
            
            if mapState1:
                
                roomOne()
            
            elif mapState2:
                
                roomTwo()
                
            elif mapState3:
                
                roomThree()
                
            elif mapState4:
                
                roomFour()
                
            elif mapState5:
    
                roomFive()
            
    def load():
        
        saveState = open(saveStateLocation, "r")
        
        saveSanityState = open(saveStateLocation)
    
        saveContent = saveState.read()
        
        saveSanity = saveSanityState.readlines()
        
        sanfind = saveSanity[1]
        
        sanfind = sanfind.replace("Sanity=", "")
        
        sanfind = int(sanfind)
        
        sanity.clear()
        
        sanity.append(sanfind)
        
        rustyNecklaceGotCheck = re.search("RustyNecklaceGot=True", saveContent)

        rustyKeyGotCheck = re.search("RustyKeyGot=True", saveContent)
        
        pristineKeyGotCheck = re.search("PristineKeyGot=True", saveContent)
        
        featherGotCheck = re.search("FeatherGot=True", saveContent)
        
        paperGotCheck = re.search("PaperGot=True", saveContent)
        
        quillGotCheck = re.search("QuillGot=True", saveContent)
        
        mapGotCheck = re.search("MapGot=True", saveContent)
        
        knifeGotCheck = re.search("KnifeGot=True", saveContent)
        
        pistolGotCheck = re.search("PistolGot=True", saveContent)
        
        crowbarGotCheck = re.search("CrowbarGot=True", saveContent)
        
        handTrolleyGotCheck = re.search("HandTrolleyGot=True", saveContent)
        
        bucketGotCheck = re.search("BucketGot=True", saveContent)
        
        bronzeKeyGotCheck = re.search("BronzeKeyGot=True", saveContent)
        
        silverKeyGotCheck = re.search("SilverKeyGot=True", saveContent)
        
        goldKeyGotCheck = re.search("GoldKeyGot=True", saveContent)
        
        boxOpenedCheck = re.search("BoxOpened=True", saveContent)

        doorOpenedCheck = re.search("DoorOpened=True", saveContent)
        
        quillMadeCheck = re.search("QuillMade=True", saveContent)
        
        mapMadeCheck = re.search("MapMade=True", saveContent)
        
        rugMovedCheck = re.search("RugMoved=True", saveContent)
        
        hatchOpenedCheck = re.search("HatchOpened=True", saveContent)
        
        bodyFlippedCheck = re.search("BodyFlipped=True", saveContent)
        
        bedroomDrawerOpenedCheck = re.search("BedroomDrawerOpened=True", saveContent)
        
        letterOpenedCheck = re.search("LetterOpened=True", saveContent)
        
        potLookedAtCheck = re.search("PotLookedAt=True", saveContent)
        
        grinderTurnedCheck = re.search("GrinderTurned=True", saveContent)
        
        bedroomKillerAliveCheck = re.search("BedroomKillerAlive=True", saveContent)
        
        bedroomKillerDeadCheck = re.search("BedroomKillerDead=True", saveContent)
        
        kitchenKillerAliveCheck = re.search("KitchenKillerAlive=True", saveContent)
        
        kitchenKillerDeadCheck = re.search("KitchenKillerDead=True", saveContent)
        
        livingRoomKillerAliveCheck = re.search("LivingRoomKillerAlive=True", saveContent)
        
        livingRoomKillerDeadCheck = re.search("LivingRoomKillerDead=True", saveContent)
        
        wardrobeUprightCheck = re.search("WardrobeUpright=True", saveContent)
        
        handTrolleyDroppedOffCheck = re.search("HandTrolleyDroppedOff=True", saveContent)
        
        wardrobeMovedTrolleyCheck = re.search("WardrobeMovedTrolley=True", saveContent)
        
        bucketMeltedCheck = re.search("BucketMelted=True", saveContent)
        
        fireOutCheck = re.search("FireOut=True", saveContent)
        
        panelOpenedCheck = re.search("PanelOpened=True", saveContent)
        
        bronzeKeyUsedCheck = re.search("BronzeKeyUsed=True", saveContent)
        
        bronzeKeyGotInterCheck = re.search("BronzeKeyGotInter=True", saveContent)
        
        silverKeyUsedCheck = re.search("SilverKeyUsed=True", saveContent)
        
        silverKeyGotInterCheck = re.search("SilverKeyGotInter=True", saveContent)
        
        goldKeyUsedCheck = re.search("GoldKeyUsed=True", saveContent)
        
        goldKeyGotInterCheck = re.search("GoldKeyGotInter=True", saveContent)
        
        paintingMovedCheck = re.search("PaintingMoved=True", saveContent)
        
        safeOpenedCheck = re.search("SafeOpened=True", saveContent)
        
        goldKeyRugMovedCheck = re.search(r"\bGoldKeyRugMoved=True\b", saveContent)
        
        goldHatchOpenedCheck = re.search(r"\bGoldHatchOpened=True\b", saveContent)
        
        finalDoorOpenedCheck = re.search(r"\bFinalDoorOpened=True\b", saveContent)
        
        roomOneCheck = re.search("FirstRoom=True", saveContent)
        
        roomTwoCheck = re.search("SecondRoom=True", saveContent)
        
        roomThreeCheck = re.search("ThirdRoom=True", saveContent)
        
        roomFourCheck = re.search("FourthRoom=True", saveContent)
        
        roomFiveCheck = re.search("FifthRoom=True", saveContent)
        
        location3Check = re.search("Location=3", saveContent)
        
        location4Check = re.search("Location=4", saveContent)
        
        location5Check = re.search("Location=5", saveContent)
        
        if paintingMovedCheck:
            
            interactionSave.append("paintingMoved")
            
        if goldKeyRugMovedCheck:
            
            interactionSave.append("goldKeyRugMoved")
        
        if goldHatchOpenedCheck:
            
            interactionSave.append("goldHatchOpened")
        
        if finalDoorOpenedCheck:
            
            interactionSave.append("finalDoorOpened")
            
        if safeOpenedCheck:
            
            interactionSave.append("safeOpened")
        
        if wardrobeMovedTrolleyCheck:
        
            interactionSave.append("wardrobeMovedTrolley")
            
        if panelOpenedCheck:
            
            interactionSave.append("panelOpened")
            
        if rustyNecklaceGotCheck:
            
            inventory.append("rusty necklace")
        
        if rustyKeyGotCheck:
            
            interactionSave.append("keyGot")
            inventory.append("rusty key")
            
        if pristineKeyGotCheck:
            
            inventory.append("pristine key")
            
        if featherGotCheck:
            
            interactionSave.append("featherGot")
            inventory.append("feather")
            
        if paperGotCheck:
            
            interactionSave.append("paperGot")
            inventory.append("paper")
            
        if quillGotCheck:
            
            inventory.append("quill")
            
        if mapGotCheck:
            
            inventory.append("map")
        
        if knifeGotCheck:
            
            interactionSave.append("knifeGot")
            inventory.append("knife")
            
        if pistolGotCheck:
            
            interactionSave.append("pistolGot")
            inventory.append("pistol")
            
        if crowbarGotCheck:
            
            inventory.append("crowbar")
            interactionSave.append("crowbarGot")
            
        if handTrolleyGotCheck:
            
            inventory.append("hand trolley")
            interactionSave.append("handTrolleyPickedUp")
            
        if bucketGotCheck:
            
            inventory.append("bucket")
            
        if bronzeKeyGotCheck:
            
            inventory.append("bronze key")
            
        if silverKeyGotCheck:
            
            inventory.append("silver key")
        
        if goldKeyGotCheck:
            
            inventory.append("gold key")    
        
        if handTrolleyDroppedOffCheck:
            
            interactionSave.append("handTrolleyDroppedOff")
            
            if handTrolleyGotCheck:
            
                findHandTrolley = inventory.index("hand trolley")
                inventory.pop(findHandTrolley)
                
            else:
                
                pass
            
        if boxOpenedCheck:
            
            interactionSave.append("boxOpened")
            
        if doorOpenedCheck:
            
            interactionSave.append("doorOpened")
            
        if quillMadeCheck:
            
            interactionSave.append("quillMade")
            
        if mapMadeCheck:
            
            interactionSave.append("mapMade")
            
        if rugMovedCheck:
            
            interactionSave.append("rugMoved")
            
        if hatchOpenedCheck:
            
            interactionSave.append("hatchOpened")
            
        if bodyFlippedCheck:
            
            interactionSave.append("bodyFlipped")
        
        if bedroomDrawerOpenedCheck:
            
            interactionSave.append("bedroomDrawerOpened")
            
        if letterOpenedCheck:
            
            interactionSave.append("letterOpened")
            
        if potLookedAtCheck:
            
            interactionSave.append("potLookedAt")
            
        if grinderTurnedCheck:
            
            interactionSave.append("grinderTurned")
            
        if bedroomKillerAliveCheck:
            
            interactionSave.append("bedroomKillerAlive")
            
        if bedroomKillerDeadCheck:
            
            interactionSave.append("bedroomKillerDead")
        
        if kitchenKillerAliveCheck:
            
            interactionSave.append("kitchenKillerAlive")
            
        if kitchenKillerDeadCheck:
            
            interactionSave.append("kitchenKillerDead")
            
        if livingRoomKillerAliveCheck:
            
            interactionSave.append("livingRoomKillerAlive")
            
        if livingRoomKillerDeadCheck:
            
            interactionSave.append("livingRoomKillerDead")
            
        if wardrobeUprightCheck:
            
            interactionSave.append("wardrobeUpright")
            
        if bucketMeltedCheck:
            
            interactionSave.append("bucketMelted")
            
        if fireOutCheck:
            
            interactionSave.append("fireOut")
            
        if bronzeKeyUsedCheck:
            
            interactionSave.append("bronzeKeyUsed")
            
        if bronzeKeyGotInterCheck:
            
            interactionSave.append("bronzeKeyGot")
            
        if silverKeyUsedCheck:
            
            interactionSave.append("silverKeyUsed")
            
        if silverKeyGotInterCheck:
            
            interactionSave.append("silverKeyGot")
        
        if goldKeyUsedCheck:
            
            interactionSave.append("goldKeyUsed")
            
        if goldKeyGotInterCheck:
            
            interactionSave.append("goldKeyGot")
        
        if roomOneCheck:
            
            mapState.clear()
            mapState.append("1")
            roomOne()
            
        if roomTwoCheck:
            
            mapState.clear()
            mapState.append("2")
            roomTwo()
            
        if roomThreeCheck:
            
            mapState.clear()
            mapState.append("3")
            roomThree()
            
        if roomFourCheck:
            
            mapState.clear()
            mapState.append("4")
            roomFour()
            
        if roomFiveCheck:
            
            mapState.clear()
            mapState.append("5")
            roomFive()    
            
        if location3Check:
            
            interactionSave.append("location3")
            
        if location4Check:
            
            interactionSave.append("location4")
            
        if location5Check:
            
            interactionSave.append("location5")
    
    saveState = open(saveStateLocation)
    
    saveContent = saveState.read()
    
    continueCheck = re.search("True", saveContent)
    
    if continueCheck:
        load()
    
    # ? Room one function is called to begin the game after everything has been defined
    roomOne()
            
# ? Define the function called "options" which is called when the user selects the option to change options
def options():
    
    theme = str(themeArray[0])
    
    blankspace()
    
    print(colored("""
    1) Theme
    0) Back
    """, attrs=["bold"]))
    
    optionsInput = str(input(colored("What do you want to do? (Input the number of the selection): ", f"{theme}", attrs=["bold"])))
    
    if optionsInput == "1":

        blankspace()
        
        def themefunc():
            
            theme = str(themeArray[0])

            print(colored("""
        1) Red
        2) Blue
        3) Green
        4) Yellow
        5) Magenta
        0) Back
            """, attrs=["bold"]))
            
            themeInput = str(input(colored("What theme do you want to use or what do you want to do? (Input the number of the selection): ", f"{theme}", attrs=["bold"])))
            
            # ? Applying red theme
            if themeInput == "1":
                
                themeArray.clear()
                
                themeArray.append("red")
                
                print("")
                
                print(colored("Red theme applied to game!", "red", attrs=["bold"]))
                
                print("")
                
                # ? ------------------------------Saving Red Theme-------------------------------------------------

                saveState = open(saveStateLocation, "rt")
                
                saveContent = saveState.read()
                
                findblue = re.search("Theme=Blue", saveContent)
                
                findgreen = re.search("Theme=Green", saveContent)
                
                findyellow = re.search("Theme=Yellow", saveContent)
                
                findmagenta = re.search("Theme=Magenta", saveContent)
                
                if findblue:
                    
                    saveContent = saveContent.replace("Theme=Blue", "Theme=Red")
                    
                    saveState.close()
                    
                    saveState = open(saveStateLocation, "wt")
                    
                    saveState.write(saveContent)
                    
                    saveState.close()
                    
                elif findgreen:
                    
                    saveContent = saveContent.replace("Theme=Green", "Theme=Red")
                    
                    saveState.close()
                    
                    saveState = open(saveStateLocation, "wt")
                    
                    saveState.write(saveContent)
                    
                    saveState.close()

                elif findyellow:
                    
                    saveContent = saveContent.replace("Theme=Yellow", "Theme=Red")
                    
                    saveState.close()
                    
                    saveState = open(saveStateLocation, "wt")
                    
                    saveState.write(saveContent)
                    
                    saveState.close()

                elif findmagenta:
                    
                    saveContent = saveContent.replace("Theme=Magenta", "Theme=Red")
                    
                    saveState.close()
                    
                    saveState = open(saveStateLocation, "wt")
                    
                    saveState.write(saveContent)
                    
                    saveState.close()
                
                time.sleep(1.5)
                
                blankspace()
                
                themefunc()
                
            # ? Applying Blue Theme
            elif themeInput == "2":
                
                themeArray.clear()
                
                themeArray.append("blue")
                
                print("")
                
                print(colored("Blue theme applied to game!", "blue", attrs=["bold"]))
                
                print("")
                
                # ? ------------------------------Saving Blue Theme-------------------------------------------------
                
                saveState = open(saveStateLocation, "rt")
                
                saveContent = saveState.read()
                
                findred = re.search("Theme=Red", saveContent)
                
                findgreen = re.search("Theme=Green", saveContent)
                
                findyellow = re.search("Theme=Yellow", saveContent)
                
                findmagenta = re.search("Theme=Magenta", saveContent)
                
                if findred:
                    
                    saveContent = saveContent.replace("Theme=Red", "Theme=Blue")
                    
                    saveState.close()
                    
                    saveState = open(saveStateLocation, "wt")
                    
                    saveState.write(saveContent)
                    
                    saveState.close()
                    
                elif findgreen:
                    
                    saveContent = saveContent.replace("Theme=Green", "Theme=Blue")
                    
                    saveState.close()
                    
                    saveState = open(saveStateLocation, "wt")
                    
                    saveState.write(saveContent)
                    
                    saveState.close()
                    
                elif findyellow:
                    
                    saveContent = saveContent.replace("Theme=Yellow", "Theme=Blue")
                    
                    saveState.close()
                    
                    saveState = open(saveStateLocation, "wt")
                    
                    saveState.write(saveContent)
                    
                    saveState.close()
                    
                elif findmagenta:
                    
                    saveContent = saveContent.replace("Theme=Magenta", "Theme=Blue")
                    
                    saveState.close()
                    
                    saveState = open(saveStateLocation, "wt")
                    
                    saveState.write(saveContent)
                    
                    saveState.close()
                
                time.sleep(1.5)
                
                blankspace()
                
                themefunc()
                
            # ? Applying Green Theme
            elif themeInput == "3":
                
                themeArray.clear()
                
                themeArray.append("green") 
                
                print("")
                
                print(colored("Green theme applied to game!", "green", attrs=["bold"]))
                
                print("")
                
                # ? ------------------------------Saving Green Theme-------------------------------------------------
                
                saveState = open(saveStateLocation, "rt")
                
                saveContent = saveState.read()
                
                findblue = re.search("Theme=Blue", saveContent)
                
                findred = re.search("Theme=Red", saveContent)
                
                findyellow = re.search("Theme=Yellow", saveContent)
                
                findmagenta = re.search("Theme=Magenta", saveContent)
                
                if findblue:
                    
                    saveContent = saveContent.replace("Theme=Blue", "Theme=Green")
                    
                    saveState.close()
                    
                    saveState = open(saveStateLocation, "wt")
                    
                    saveState.write(saveContent)
                    
                    saveState.close()
                    
                elif findred:
                    
                    saveContent = saveContent.replace("Theme=Red", "Theme=Green")
                    
                    saveState.close()
                    
                    saveState = open(saveStateLocation, "wt")
                    
                    saveState.write(saveContent)
                    
                    saveState.close()
                    
                elif findyellow:
                    
                    saveContent = saveContent.replace("Theme=Yellow", "Theme=Green")
                    
                    saveState.close()
                    
                    saveState = open(saveStateLocation, "wt")
                    
                    saveState.write(saveContent)
                    
                    saveState.close()
                    
                elif findmagenta:
                    
                    saveContent = saveContent.replace("Theme=Magenta", "Theme=Green")
                    
                    saveState.close()
                    
                    saveState = open(saveStateLocation, "wt")
                    
                    saveState.write(saveContent)
                    
                    saveState.close()
                
                time.sleep(1.5)
                
                blankspace()
                
                themefunc()
                
            # ? Applying Yellow Theme
            elif themeInput == "4":
                
                themeArray.clear()
                
                themeArray.append("yellow") 
                
                print("")
                
                print(colored("Yellow theme applied to game!", "yellow", attrs=["bold"]))
                
                print("")
                
                # ? ------------------------------Saving Yellow Theme-------------------------------------------------
                
                saveState = open(saveStateLocation, "rt")
                
                saveContent = saveState.read()
                
                findblue = re.search("Theme=Blue", saveContent)
                
                findred = re.search("Theme=Red", saveContent)
                
                findgreen = re.search("Theme=Green", saveContent)
                
                findmagenta = re.search("Theme=Magenta", saveContent)
                
                if findblue:
                    
                    saveContent = saveContent.replace("Theme=Blue", "Theme=Yellow")
                    
                    saveState.close()
                    
                    saveState = open(saveStateLocation, "wt")
                    
                    saveState.write(saveContent)
                    
                    saveState.close()
                    
                elif findred:
                    
                    saveContent = saveContent.replace("Theme=Red", "Theme=Yellow")
                    
                    saveState.close()
                    
                    saveState = open(saveStateLocation, "wt")
                    
                    saveState.write(saveContent)
                    
                    saveState.close()
                    
                elif findgreen:
                    
                    saveContent = saveContent.replace("Theme=Green", "Theme=Yellow")
                    
                    saveState.close()
                    
                    saveState = open(saveStateLocation, "wt")
                    
                    saveState.write(saveContent)
                    
                    saveState.close()
                    
                elif findmagenta:
                    
                    saveContent = saveContent.replace("Theme=Magenta", "Theme=Yellow")
                    
                    saveState.close()
                    
                    saveState = open(saveStateLocation, "wt")
                    
                    saveState.write(saveContent)
                    
                    saveState.close()
                
                time.sleep(1.5)
                
                blankspace()
                
                themefunc()
                
            # ? Applying Magenta Theme
            elif themeInput == "5":
                
                themeArray.clear()
                
                themeArray.append("magenta")
                
                print("")
                
                print(colored("Magenta theme applied to game!", "magenta", attrs=["bold"]))
                
                print("")
                
                # ? ------------------------------Saving Magenta Theme-------------------------------------------------
                
                saveState = open(saveStateLocation, "rt")
                
                saveContent = saveState.read()
                
                findblue = re.search("Theme=Blue", saveContent)
                
                findred = re.search("Theme=Red", saveContent)
                
                findgreen = re.search("Theme=Green", saveContent)
                
                findyellow = re.search("Theme=Yellow", saveContent)
                
                if findblue:
                    
                    saveContent = saveContent.replace("Theme=Blue", "Theme=Magenta")
                    
                    saveState.close()
                    
                    saveState = open(saveStateLocation, "wt")
                    
                    saveState.write(saveContent)
                    
                    saveState.close()
                    
                elif findred:
                    
                    saveContent = saveContent.replace("Theme=Red", "Theme=Magenta")
                    
                    saveState.close()
                    
                    saveState = open(saveStateLocation, "wt")
                    
                    saveState.write(saveContent)
                    
                    saveState.close()
                    
                elif findgreen:
                    
                    saveContent = saveContent.replace("Theme=Green", "Theme=Magenta")
                    
                    saveState.close()
                    
                    saveState = open(saveStateLocation, "wt")
                    
                    saveState.write(saveContent)
                    
                    saveState.close()
                    
                elif findyellow:
                    
                    saveContent = saveContent.replace("Theme=Yellow", "Theme=Magenta")
                    
                    saveState.close()
                    
                    saveState = open(saveStateLocation, "wt")
                    
                    saveState.write(saveContent)
                    
                    saveState.close()
                
                time.sleep(1.5)
                
                blankspace()
                
                themefunc()
                
            elif themeInput == "0":
                
                options()
                
            else:
                
                print("")
                
                print("That is not an option!")
                
                print("")
                
                time.sleep(1)
                
                blankspace()
                
                themefunc()
                
        themefunc()
        
    elif optionsInput == "0":
        
        startMenu()
            
    else:
        
        print("")
        
        print("That is not an option!")
        
        print("")
        
        time.sleep(1)
        
        blankspace()
        
        options()
        
# ? Define the function called "credits" which is called when the user selects the option to view the credits
def credits():
    
    # ? Print a series of blank space to clear away previous results
    blankspace()
        
    # ? Print the credits series of text
    print(colored(f"""

    This game was created and designed by:
        
                                        /$$                    
                                       | $$                    
           /$$  /$$$$$$   /$$$$$$  /$$$$$$$  /$$$$$$  /$$$$$$$ 
          |__/ /$$__  $$ /$$__  $$/$$__  $$ /$$__  $$| $$__  $$
           /$$| $$  \ $$| $$  \__/ $$  | $$| $$  \ $$| $$  \ $$
          | $$| $$  | $$| $$     | $$  | $$| $$  | $$| $$  | $$
          | $$|  $$$$$$/| $$     |  $$$$$$$|  $$$$$$/| $$  | $$
          | $$ \______/ |__/      \_______/ \______/ |__/  |__/
     /$$  | $$                                                 
    |  $$$$$$/                                                 
     \______/
     
    Github: https://github.com/octantx
     
    Version: {ver} | {date}  
    
    Ascii Text: http://www.patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
    Ascii Art: https://www.asciiart.eu & https://ascii.co.uk/art
    """, "magenta", attrs=["bold"]))
    
    # ? Wait 3 seconds
    time.sleep(4)
    
    # ? Go back to the start menu
    startMenu()

# ? Define the function called "startMenu" which is called when the game is started
def startMenu():
    
    theme = str(themeArray[0])
    
    saveState = open(saveStateLocation, "r")
    
    saveContent = saveState.read()
    
    saveState.close()
    
    continueCheck = re.search("True", saveContent)
    
    # ? Print a series of whitespace in the terminal to rid of previous tests (mainly for testing)
    blankspace()
    
    # ? Print the title and subtitle of the game in a cool ascii font with red colouring
    print(colored(f"""
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
                            -       {ver}       - 
    """, f"{theme}", attrs=["bold"]))
    
    if continueCheck:
        
        print(colored("""
        1) Continue game
        2) Start new game
        3) Options
        4) Credits
        0) Exit
        """, attrs=["bold"]))
        
        # ? Get input from the user as to what they want to do
        startInp = input((colored("What do you want to do? (Input the number of the selection): ", f"{theme}", attrs=["bold"])))
        
            
        if startInp == "1":
            game()
            
        elif startInp == "2":
            
            overwrite()
            
            game()
            
        elif startInp == "3":
            options()
            
        elif startInp == "4":
            credits()
            
        elif startInp == "0":
            print("")
            sys.exit()
                
        elif startInp == "telltale":
            
            blankspace()
            
            print(colored("""
                
            ████████╗       ████████╗
            ╚══██╔══╝       ╚══██╔══╝
               ██║             ██║   
               ██║             ██║   
               ██║             ██║   
               ╚═╝             ╚═╝   

                     ██████╗ 
                    ██╔════╝ 
                    ██║  ███╗
                    ██║   ██║
                    ╚██████╔╝
                    ╚═════╝ 
                    
                    
            """, "yellow", attrs=["bold"]))
            
            time.sleep(0.7)
            startMenu()
        
        elif startInp == "john bongos":
            
            blankspace()
            
            print("*tim allen face*")
            
            print("")
            
            print("EUGH!!???? YOU'RE JOHN BONGOS???!!! TTTHHHEEE JOHN BONGOS??????!!!!! EEEEUUUUUGGGGHHHHH!!!!!!???????")
            
            print("")
            
            time.sleep(1.7)
            
            startMenu()
        
        else:
            
            print("")
            print("That is not a valid selection!")
            print("")
            
            time.sleep(0.43)
            
            print(colored(".", f"{theme}", attrs=["bold"]))
            
            time.sleep(0.43)
            
            print(colored(".", f"{theme}", attrs=["bold"]))
            
            time.sleep(0.43)
            
            print(colored(".", f"{theme}", attrs=["bold"]))
            
            time.sleep(0.43)

            startMenu()
            
    else:
    
        print(colored("""
        1) Start
        2) Options
        3) Credits
        0) Exit
        """, attrs=["bold"]))
        
        # ? Get Input from the user as to what they want to do
        startInp = input((colored("What do you want to do? (Input the number of the selection): ", f"{theme}", attrs=["bold"])))
        
        if startInp == "1":
            game()
            
        elif startInp == "2":
            options()
            
        elif startInp == "3":
            credits()
            
        elif startInp == "0":
            print("")
            sys.exit()
            
        elif startInp == "telltale":
            
            blankspace()
            
            print(colored("""
                
            ████████╗       ████████╗
            ╚══██╔══╝       ╚══██╔══╝
               ██║             ██║   
               ██║             ██║   
               ██║             ██║   
               ╚═╝             ╚═╝   

                     ██████╗ 
                    ██╔════╝ 
                    ██║  ███╗
                    ██║   ██║
                    ╚██████╔╝
                    ╚═════╝ 
                    
                    
            """, "yellow", attrs=["bold"]))
            
            time.sleep(0.7)
            startMenu()
            
        elif startInp == "john bongos":
            
            blankspace()
            
            print("*tim allen face*")
            
            print("")
            
            print("EUGH!!???? YOU'RE JOHN BONGOS???!!! TTTHHHEEE JOHN BONGOS??????!!!!! EEEEUUUUUGGGGHHHHH!!!!!!???????")
            
            print("")
            
            time.sleep(1.7)
            
            startMenu()
        
        else:
            
            print("")
            print("That is not a valid selection!")
            print("")
            
            time.sleep(0.43)
            
            print(colored(".", f"{theme}", attrs=["bold"]))
            
            time.sleep(0.43)
            
            print(colored(".", f"{theme}", attrs=["bold"]))
            
            time.sleep(0.43)
            
            print(colored(".", f"{theme}", attrs=["bold"]))
            
            time.sleep(0.43)

            startMenu()
    
# ? Call the start menu function, which runs all of the code in the function
startMenu()
