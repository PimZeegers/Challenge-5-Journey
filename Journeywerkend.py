
print("░░░░░██╗░█████╗░██╗░░░██╗██████╗░███╗░░██╗███████╗██╗░░░██╗")
print("░░░░░██║██╔══██╗██║░░░██║██╔══██╗████╗░██║██╔════╝╚██╗░██╔╝")
print("░░░░░██║██║░░██║██║░░░██║██████╔╝██╔██╗██║█████╗░░░╚████╔╝░")
print("██╗░░██║██║░░██║██║░░░██║██╔══██╗██║╚████║██╔══╝░░░░╚██╔╝░░")
print("╚█████╔╝╚█████╔╝╚██████╔╝██║░░██║██║░╚███║███████╗░░░██║░░░")
print("░╚════╝░░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝░░░╚═╝░░░")


print("█▀▄▀█ ▄▀█ █▀▄ █▀▀   █▄▄ █▄█   ▄▀█ █▀█ █ ▄▀█ █▄░█   ▄▀█ █▄░█ █▀▄   █▀█ █ █▀▄▀█")
print("█░▀░█ █▀█ █▄▀ ██▄   █▄█ ░█░   █▀█ █▀▄ █ █▀█ █░▀█   █▀█ █░▀█ █▄▀   █▀▀ █ █░▀░█")

start = input("Press ENTER to start your story!")                                               #Gebruik een input als een "stop" en ga door wanneer er op enter wordt geklikt.
print("")                                                                                    #zorg voor een spatie tussen de teksten
print("You are a viking named Jormungander, looking for a place to settledown")                 #toon op het scherm wat tussen de haakjes staat
print("You want to stop the killing and live a good life without the need of slaughter...")     #toon op het scherm wat tussen de haakjes staat
print("")
import random
import time     #(!) Zorg ervoor dat het script tijd kan meten. 
time.sleep(1)   #zorg ervoor dat het script 2 seconden wacht voordat het de code hervat 

   #(!!) Heeft momenteel geen actieve functie in het script                                                    #Een array ( lijst ) met keuzes
print("You start your journey in a forest. You are lost and do not know where to go.")          #toon op het scherm wat tussen de haakjes staat 
print("The only direction you know is that you have to go North to reach your destination.")    #toon op het scherm wat tussen de haakjes staat
print("")                                                                                       #zorg voor een spatie tussen de teksten                                  
print("Options: North/East/South/West")                                                         #toon op het scherm wat tussen de haakjes staat

second = ("")
dog = ("Het verhaal gaat verder....")                                       
choice = random.choice([dog,second ])    
inventory = []                          #De inventory lijst
lijst = []

put = input()
if put == "North" or put == "East" or put == "South" or put == "West":              #put als variable en in het geval dat het gelijk staat aan North,East,South of West
    print (choice)                                                                     #Als het bovenstaande positief is, dan print hij de ( random ) gekozen keuze
if choice == dog:                                                                                        
        print("")
        print("You come across an abandoned home, would you like to look inside?") # Stel de vraag d.m.v het te printen op het scherm
        print("Options: Yes or No") 

        abcd = input("") # Beantwoord de bovenstaande vraag met een input 

        if abcd == "No":
            print("")
            print("You leave the house and decide to not risk going in")
            
        if abcd == "Yes":
            print("")
            print("The entire house is burned down and you see animals living in here now.")
            print("You see 2 corpses of the people that probably lived here a long time ago.")
            print("You find a bag that looks like a gift for someone, it reads: “for Paul”.")
            print("")
            print("What do you want to do?")
            print("Choose between:")
            print("A. Bury the corpses and leave")
            print("B. Take the present and leave")
        
            question = input("")
            if question == "A":
                print("")
                print("You decide that everyone deserves a burial when they die.")
                print("You put the present on the grave where all the corpses are burried")
                print("You do this because it gives you a good feeling to know that the present is on the grave.")
            if question == "B":
                print("You think that Paul has probably already died just like the rest of them.. You think that you, as an alive person deserve the present. You rip the present open and you find 20 gold bars inside.")  
                print("You look shocked, These gold bars are worth some real money!.. The people that used to live here must have been very rich..")
                print("") 
                #Tweede verhaal
if choice == second:    #Als het random getal in het begin uit komt op second, dan begint die in dit gedeelte van het script.
    print("You are walking in the direction you chose.. but then suddenly you come across a wolf protecting her wolf cub... What would you like to do?")
    print("Choose between:")
    print("A. Kill her ")
    print("B. Give her some food ")                 
    print("C. Leave her ")
    decision=input("") # Vraag om antwoord van de bovenstaande vragen.
    if decision == "A" or "a": # Als je A antwoord, ga door naar onderstaande statements.
        print("You decide that you don't need to leave these savage beasts alive, you should put them out of their misery.  ")
        print("test")
    if decision == "B": # Als je B antwoord, ga door naar onderstaande statements.
        print("test")
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
        if Tweede == ("w"):
            lijst.append("50")
            print("You damaged the wolf with 50HP")
        else:
            print("You have taken damage yourself")
        time.sleep(0.5)
        derde = input("E")
        if derde == ("e"):
            lijst.append("50")
            print("You damaged the wolf with 50HP")
        else:
            print("You have taken damage yourself")
        time.sleep(0.5)
        vierde = input("R")
        if vierde == ("r"):
            lijst.append("50")
            print("You damaged the wolf with 50HP")
        else:
            print("You have taken damage yourself")
        time.sleep(0.5)
    if lijst == [50,50,50,50]:
        print("Je hebt gewonnen!")
    else:
        print("Je hebt verloren!")



