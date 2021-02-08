from random import randint as rand
from matplotlib import pyplot as plt 
import numpy as np
def game(sw):

    print("The Monty Hall Problem: \n")
    print("Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, Do you want to pick door No. 2? Is it to your advantage to switch your choice?")
    #Init
    doors = {1:False , 2:False , 3:False} # 3 doors , False = Lion, True = Treasure
    doors[rand(1,3)] = True               # The money is behind a random door
    print("[DEBUG] doors = " ,doors)      # Print the backstage view (just to insure the game is running) 
    
    #Game
    choice=rand(1,3)                      # Bot_Player random chose a door
    for d in range(1,4):                  # Reveal the door which is not the Money door (and ofcoursenot the Bot_player choice door)
        if not d == choice:         
            if doors[d] == False:    
                r = d
                break
    print("choice = ",choice)
    print(f"The revealed door {r} is {doors[r]}" )
    print("Do you want to switch ? ",sw)
    if sw:                                # Define the third door (Not the Bot_player choice door and not the reveald one)
        for d in range(1,4):
            if not d == choice:
                if not d == r:    
                    choice = d
                    break
    if doors[choice] == True:
        print(f" Your Door {choice} is Car")
    if doors[choice] == False:
        print(f" Your Door {choice} is Goat")
    print("--------")
    return doors[choice] # True or False
print("----------------------")
NumberOfTries = int(input("Enter the number of times you want to simulate: "))
switch=0          
for _ in range(NumberOfTries):
     r = game(True)
     if r :
        switch+=1

dont=0
for _ in range(NumberOfTries):
     r = game(False)
     if r :
        dont+=1

print('\n\n\n')
print('Results of the simulation:')
print("If the bot switches its choice, the result is :    " , switch*100/(switch+dont) , ' % of the trials the bot wins Car || i.e.',switch," times per ",NumberOfTries,"attempts" )
print("If the bot doesn't switch its choice, the result is : " , dont*100/(switch+dont)   , ' % of the trials times the bot wins Goat || i.e. ',dont," times per ",NumberOfTries,"attempts" )
print('Visualization: \n')
label = ['Swithcing the choice','Not Switching the choice']
data = [switch*100/(switch+dont),dont*100/(switch+dont)]
myexplode = [0.2,0]
#Plot
plt.pie(data, labels = label,autopct='%1.1f%%',explode = myexplode,shadow = True)
plt.title('Visualization of Monty Hall Problem using Python')
plt.show()
