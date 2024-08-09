import numpy as np

def matrix():
    temp = ["O"]*100; temp = np.array(temp); temp = temp.reshape(10,10); return temp

def kontrol(table):
    global game_won
    for i in table:
        if "X" in i:
            game_won=False
            return game_won
    print("GAME ENDED! \n"  + str(table))
    game_won=True; return game_won

bf1_D = matrix(); bf2_D = matrix(); bf1_A = matrix(); bf2_A = matrix()

player_names=["Egemen","Atakan"]
"""for i in range(2):name=screen.textinput("Enter your name: "); player_names.append(name)"""

print("Always state your left top corner as a (x,y) then state your direction as in vertical and horizental")

"""
bf1_D3=input("Enter your 3 long ship: ").split(","); bf1_D4=input("Enter your 4 long ship: ").split(","); bf1_D5=input("Enter your 5 long ship: ").split(",")
bf2_D3=input("Enter your 3 long ship: ").split(","); bf2_D4=input("Enter your 4 long ship: ").split(","); bf2_D5=input("Enter your 5 long ship: ").split(",")
"""

bf1_D3=[1,3,"vertical"]; bf1_D4=[0,4,"horizental"]; bf1_D5=[2,5,"vertical"]; bf2_D3=[1,3,"vertical"]; bf2_D4=[5,3,"horizental"]; bf2_D5=[1,3,"vertical"]
player1_ships=[bf1_D3,bf1_D4,bf1_D5]; player2_ships=[bf2_D3,bf2_D4,bf2_D5]; player_ships=[player1_ships,player2_ships]
player_def=[bf1_D,bf2_D]; player_attack=[bf1_A,bf2_A]

for i in player_ships:
    index = player_ships.index(i)
    repeat=0
    for j in i:
        column=int(j[0]); row=int(j[1]); direction=str(j[2])
        player_def[index][column,row] = "X"
        if direction.capitalize() =="Vertical":
            for x in range(2+repeat):
                column = column + 1
                player_def[index][column,row] = "X"
            repeat+=1
        elif direction.capitalize() == "Horizental":
            for x in range(2+repeat):
                row = row + 1
                player_def[index][column,row] = "X"
            repeat+=1
    repeat=0

#ship placement is done, time for the attack

game_won = False; round = 1 
while game_won==False:
    attacker = player_attack[round%2] #saldıran kişi
    print(attacker)
    guess = input(f"\n Guess a location to send your rockets {player_names[round%2]}:").split(",")
    column = int(guess[0]); row = int(guess[1]); round += 1; defender = player_def[round % 2]
    if defender[column,row]=="X":
        print("\n You hit one of his ships!")
        attacker[column,row] = "H";defender[column,row] = "S"
    else:
        print("\n You missed :(")
        attacker[column,row] = "M"
    kontrol(defender)