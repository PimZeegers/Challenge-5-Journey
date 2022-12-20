
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

        if abcd == "No" or "no" or "n":
            print("")
            print("You leave the house and decide to not risk going in")
            
        if abcd == "Yes" or "yes" or "y":
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
    if decision == "B" or "a":
        print("Every beast deserves to have a chance at survival,")
        print ("you decide to give the wolfs something to eat because you feel bad for them.") 
        print ("The mother is defensive and bites you, but you continue despite the pain and still decide to give them the food.")
        print("when you turn your back to them the mother jumps at your back and attacks you.")