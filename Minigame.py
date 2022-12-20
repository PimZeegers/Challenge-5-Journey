

#(!!!) Dit is een Test-File voor de minigame in de hoofd-game.
#Let op: Deze file is niet gesyncroniseerd met de main file, de game kan hier dus nog buggen of anders werken omdat deze anders geprogrammeerd is.


import time 
lijst = []
start = input("druk om enter om de test te starten.")
if start == start:   #Als het random getal in het begin uit komt op second, dan begint die in dit gedeelte van het script.
    print("You are walking in the direction you chose.. but then suddenly you come across a wolf protecting her wolf cub... What would you like to do?")
    print("Choose between:")
    print("A. Kill her ")
    print("B. Give her some food ")                 
    print("C. Leave her ")
    decision=input("") # Vraag om antwoord van de bovenstaande vragen.
    if decision == "A": # Als je A antwoord, ga door naar onderstaande statements.
        print("You decide that you don't need to leave these savage beasts alive, you should put them out of their misery.  ")
    if decision == "B": # Als je B antwoord, ga door naar onderstaande statements.
        print("Every beast deserves to have a chance at survival, you decide to give the wolfs something to eat because you feel bad for them. The mother is defensive and bites you, but you continue despite the pain and still decide to give them the food. They start licking you and letting you pet them. They are very happy. ")
    if decision == "C": # Als je C antwoord, ga door naar onderstaande statements.
        print("when you turn your back to them the mother jumps at your back and attacks you. You lose 10 health and have to prepare for battle....")
        time.sleep(1) # Wacht 1 seconde
        print("Make yourself ready..")
        time.sleep(1) # Wacht 1 seconde
        print("Short explanation: When certain letters appear on the screen you will have to press them quickly, otherwise you will lose the battle and die.") # Uitleg voor de mini-game.
        time.sleep(3) # Wacht 3 seconde 
        eerste = input("Q") # Vraag naar de eerste letter
        if eerste == ("q"): # controleer de ingevoerde letter
            lijst.append("50") # Als de ingevoerde letter klopt, voeg "50" toe aan de lijst.
            print("You damaged the wolf with 50HP")  # Damage de wolf
        else: # Als de letter niet klopt, dan gaat de else statement actief en dan pak je zelf damage.
            print("You have taken damage yourself")
        time.sleep(0.5)
        Tweede = input("W")
        if Tweede == ("w" or "W"):
            lijst.append("50")
            print("You damaged the wolf with 50HP")
        else:
            print("You have taken damage yourself")
        time.sleep(0.5)
        derde = input("E")
        if derde == ("e" or "E"):
            lijst.append("50")
            print("You damaged the wolf with 50HP")
        else:
            print("You have taken damage yourself")
        time.sleep(0.5)
        vierde = input("R")
        if vierde == ("r" or "R"):
            lijst.append("50")
            print("You damaged the wolf with 50HP")
        else:
            print("You have taken damage yourself")
        time.sleep(0.5)
        print(lijst)
    if lijst == [50,50,50,50]:#Minimaal 2x het goede cijfer invullen, of anders ben je dood.
        print("Je hebt gewonnen!")
    else:
        print("Je hebt verloren!")