# -*- coding: utf-8 -*-
import random

print "**************************************************************"
print "******    Programação II -  2º Ciclo Jogos Digitais     ******"
print "******   Nome Magno Gouveia          RA 1430961321027   ******"
print "******   Programa : Forca                                ******"
print "**************************************************************"



lifes = 4
winRoad = 0

fruitList = ["uva", "pera", "limao"]
chosen = random.choice(fruitList)
size = len(chosen)
mistakes = []
rights = []

i=0
while( i < size):
    rights.append("_")
    i+=1

while(lifes > 0) and (winRoad < size):
    
    if(mistakes):
        print "você ja errou estas letras: "  + ' '.join(mistakes)
    else:
        print "você ainda não possui erros"
            
    print ' '.join(rights)
    print ""
    print "você possui " + str(lifes)+ " vidas"
    playerChoice = raw_input("Digite uma letra")
    
    
    if(playerChoice == ""):
        print "por favor digite uma letra."
    elif(playerChoice in chosen):
        winRoad+=1
        print "acertou a letra: " + playerChoice
        rights.pop(chosen.index(playerChoice))
        rights.insert(chosen.index(playerChoice),playerChoice)
    else:
        lifes-= 1
        print "errou, não tem essa letra, perdeu uma vida"
        mistakes.append(playerChoice)
        
    if(lifes == 0):
        print "você não possui mais vidas, você perdeu"
    if(winRoad >= size):
        print "parabens! você ganhou!"

