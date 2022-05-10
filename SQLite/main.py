#menu system
# from pip import main
import readSongs
import createSongs
import updateSongs
import deleteSongs
import search

# create a function for the menu

def menuOptions() :
    options = 0 #flag variable

    # check for the variable with the value not equal to zero 
    while options not in ["1","2","3","4","5","6"]:
        print("Songs Menu Options:\n1. Print.\n2. Add.\n3. Update.\n4. Delete.\n5. Search.\n6. Exit")
        # re-assign the options variable to an input function
        options = input("\nEnter one of the options above: ")
        if options not in ["1","2","3","4","5","6"]:
            print(f"{options} is not a valid choice")
    return options

#create a boolean variable and set the value to True
mainProgram = True

while mainProgram == True: #check value held in main program with the boolean value True
    #pass menuOptions to mainMenu variable
    mainMenu = menuOptions()

    if mainMenu == "1":
        readSongs.readSongs()
    elif mainMenu == "2":
        createSongs.addSongs()
    elif mainMenu == "3":
        updateSongs.updateSongs()
    elif mainMenu == "4":
        deleteSongs.deleteSongs()
    elif mainMenu == "5":
        search.searchSong()
    else:
        mainProgram = False 
input("Press Enter to Exit")
    
