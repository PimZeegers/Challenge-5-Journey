
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

directions = ["east","west","north","south"]   #(!!) Heeft momenteel geen actieve functie in het script                                                    #Een array ( lijst ) met keuzes
print("You start your journey in a forest. You are lost and do not know where to go.")          #toon op het scherm wat tussen de haakjes staat 
print("The only direction you know is that you have to go North to reach your destination.")    #toon op het scherm wat tussen de haakjes staat
print("")                                                                                       #zorg voor een spatie tussen de teksten                                  
print("Options: North/East/South/West")                                                         #toon op het scherm wat tussen de haakjes staat

second = ("Dit is een test")
dog = ("You come across an abandoned home, would you like to look inside?")                     #Stel de vraag d.m.v het te printen op het scherm                     
choice = random.choice([dog,second ])    
                                                          


put = input()

if put == "North" or put == "East" or put == "South" or put == "West":
    print (choice)

if choice == dog:                                                                                   #zorgt voor een loop
    userInput = input()                                                                         #Slaat de input(ingevoerde tekst ) op in de variable "userInput"
    if userInput == "North":
        print("north")        
        print("Het verhaal gaat verder...")
        print("")
        print("You come across an abandoned home, would you like to look inside?") # Stel de vraag d.m.v het te printen op het scherm
        print("Options: Yes or No")  
        abcd = input("") # Beantwoord de bovenstaande vraag met een input 

        if abcd == "No":
            print("")
            print("You leave the house and decide to not risk going in")
            
        else:
            print("voer aub een geldig antwoord in00")
            
            if abcd == "Yes":
                print("")
                print("The entire house is burned down and you see animals living in here now.")
                print("You see 2 corpses of the people that probably lived here a long time ago.")
                print("You find a bag that looks like a gift for someone, it reads: “for Paul”.")
                print("")
                print("What do you want to do?")
                print("Choose between:  Bury the corpses and leave and Take the present and leave ")
        
                question = input("")
                if question == "1. Bury the corpses and leave":
                    print("")
                    print("You decide that everyone deserves a burial when they die.")
                    print("You put the present that was for Paul on their grave so that they know the present is still safe and sound")
                    
                else:
                    print("Voer aub een geldig antwoord in1")

                if question == "Take the present and leave ":
                    print("You decide that Paul is probably dead and you as an alive person deserve the present more. You rip the present open and you find 20 gold bars inside.")  
                    print("")  
                    
                else:
                    print("Voer aub een geldig antwoord in2")

if put == "North" or put == "East" or put == "South" or put == "West":
    print (choice)

if choice == second:
    print("")