print("""
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/
/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/______/
/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_____/
/______/______/______/______/_____"=.o|o_.--""______/______/______/______/__
*******************************************************************************
""")

print("Welcome to the Treasure Island.\nYour mission is to find the treasure.")
choice1 = input("You're at a crossword, where do you want to go? \nType 'left' or 'right'.")
if choice1 == "left":
    choice2 = input("You've come to a lake.\nThere is an island in the middle of the lake. \nType 'wait' to wait for the boat. Type 'swim' to swim across.")
    if choice2 == "wait":
        choice3 = input("You've arrived at an island unharmed.\nThere's a house with three doors. One red,\nOne yellow and One blue.\nWhich colour do you ant to chose?")
        if choice3=="yellow":
            print("""
               ___________
              '._==_==_=_.'  
              .-\\:      /-.
             | (|:.     |) |
              '-|:.     |-'
                \\::.    /
                 '::. .'
                   ) (
                 _.' '._
                `"""""""`

            🏆 You found the treasure! YOU WIN! 🏆
                        """)
        elif choice3=="blue":
            print("You enter a room full of beasts!!\nGame over!!")
        elif choice3=="red" :
            print("It's a room full of fire\nGame Over!!")
        else:
            print("You chose the room that doesn't exist!")
    else:
        print("You're attacked by an angry trout.\nGame over!!")
else:
    print("You fell into a hole!!\nGame Over!!")


