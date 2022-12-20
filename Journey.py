
print("░░░░░██╗░█████╗░██╗░░░██╗██████╗░███╗░░██╗███████╗██╗░░░██╗")
print("░░░░░██║██╔══██╗██║░░░██║██╔══██╗████╗░██║██╔════╝╚██╗░██╔╝")
print("░░░░░██║██║░░██║██║░░░██║██████╔╝██╔██╗██║█████╗░░░╚████╔╝░")
print("██╗░░██║██║░░██║██║░░░██║██╔══██╗██║╚████║██╔══╝░░░░╚██╔╝░░")
print("╚█████╔╝╚█████╔╝╚██████╔╝██║░░██║██║░╚███║███████╗░░░██║░░░")
print("░╚════╝░░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝░░░╚═╝░░░")


print("█▀▄▀█ ▄▀█ █▀▄ █▀▀   █▄▄ █▄█   ▄▀█ █▀█ █ ▄▀█ █▄░█   ▄▀█ █▄░█ █▀▄   █▀█ █ █▀▄▀█")
print("█░▀░█ █▀█ █▄▀ ██▄   █▄█ ░█░   █▀█ █▀▄ █ █▀█ █░▀█   █▀█ █░▀█ █▄▀   █▀▀ █ █░▀░█")

start = input("Press ENTER to start your story!")                                               #Gebruik een input als een "stop" en ga door wanneer er op enter wordt geklikt.
print("")                                                                                       #zorg voor een spatie tussen de teksten
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
                                                          


put = input()
if put == "North" or put == "East" or put == "South" or put == "West":              #put als variable en in het geval dat het gelijk staat aan North,East,South of West
    print (choice)                                                                     #Als het bovenstaande positief is, dan print hij de ( random ) gekozen keuze
if choice == dog:                                                                                        
        print("")
        print("You come across an abandoned home, would you like to look inside?") # Stel de vraag d.m.v het te printen op het scherm
        print("Options: Yes or No") 

        abcd = input("") # Beantwoord de bovenstaande vraag met een input 

        if abcd == "No" or "no" or "n" or "N" or "No":
            print("")
            print("You leave the house and decide to not risk going in")
            
        if abcd == "Yes" or "yes" or "y" or "ye" or "Y" or "Ye":
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
            if question == "A" or "a":
                print("")
                print("You decide that everyone deserves a burial when they die.")
                print("You put the present on the grave where all the corpses are burried")
                print("You do this because it gives you a good feeling to know that the present is on the grave.")

            if question == "B" or "b":
                print("You think that Paul has probably already died just like the rest of them..")
                print("You think that you, as an alive person deserve the present.")
                print("You rip the present open and you find 20 gold bars inside.")  
                print("You look shocked, These gold bars are worth some real money!..")
                print("The people that used to live here must have been very rich..")
                print("") 

if choice == second:
    print("You are walking in the direction you chose..")
    print("but then suddenly you come across a wolf protecting her wolf cub...")
    print("What would you like to do?")
    print("Choose between:")
    print("A. Kill her ")
    print("B. Give her some food ")
    print("C. Leave her ")
    decision=input("")
    
    if decision == "A" or "a":
        print("You decide that you don't need to leave these savage beasts alive,")
        print("you should put them out of their misery.")

    if decision == "B" or "b":
        print("Every beast deserves to have a chance at survival,")
        print ("you decide to give the wolfs something to eat because you feel bad for them.") 
        print ("The mother is defensive and bites you, but you continue despite the pain and still decide to give them the food.")

    if decision == "C" or "c": 
        lijst = [] # Maak een lijst, voor de gevechts-status in op te slaan.
        print("when you turn your back to them the mother jumps at your back and attacks you.")
        time.sleep(15) # Wacht 15 seconden
        print("Make yourself ready..")
        time.sleep(5) # Wacht 1 seconde
        print("Short explanation: When certain letters appear on the screen you will have to press them quickly, otherwise you will lose the battle and die.") # Uitleg voor de mini-game.
        time.sleep(3) # Wacht 3 seconde 
        eerste = input("Q") # Vraag naar de eerste letter
        if eerste == ("q"): # controleer de ingevoerde letter
            lijst.append("50") # Als de ingevoerde letter klopt, voeg "50" toe aan de lijst.
            print("You damaged the wolf with 50HP")  # Damage de wolf
        else: # Als de letter niet klopt, dan gaat de else statement actief en dan pak je zelf damage.
            print("You have taken damage yourself")
        time.sleep(0.5)
        Tweede = input("W")                             #(!) Spel werkt, de inputs moeten alleen nog door "geforceerd" worden, want de bedoeling is dat je in die 0,5 seconde een antwoord geeft, nu heb je oneindig de tijd.
        if Tweede == ("w"):                             #(!) Antwoorden moeten nog geoptimaliseerd worden. Nu worden enkel kleine letters doorgevoerd
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
    if lijst == [50,50,50,50] or [50,50] or [50,50,50]: #Uitleg: Voor te winnen moet je minimaal 2x een goed antwoord geven
        print("Je hebt gewonnen!")                      #Bij een goed antwoord wordt er in de variable "lijst" een 50 toegevoegd.
    else:                                               #Dit betekend dat bij 2x 50 of meer je gewonnen hebt, en anders velies je want,
        print("Je hebt verloren!")                      #Dan ga je automatisch naar de "else" statement.



