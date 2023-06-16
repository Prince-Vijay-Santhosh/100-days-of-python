print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /

                                                                           
  ,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba, ,adPPYba,
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8 a8P_____88
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88         8PP""""""" 
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88         "8b,   ,aa
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88          `"Ybbd8"'
                                                                           
                                                                                     HUNT          
    
*******************************************************************************
''')
print("\nWelcome to Treasure Island.")
print("\nYour mission is to find the treasure.") 
print("\nAmidst the crashing waves and the salty air, a worn-out map led the adventurous souls to the fabled Treasure Island. Whispers of untold riches and hidden secrets lingered in the hearts of those brave enough to embark on this perilous journey. The traveler stood at the crossroads, torn between two diverging paths. To the left, a narrow trail disappeared into the dense undergrowth, whispering tales of hidden treasure and boundless riches. To the right, a treacherous path led to an ominous hole, a gateway to certain doom.")
a = input("\nChoose ""RIGHT"" or ""LEFT"" Path : \n")
a_fin = a.lower()
if(a_fin == "right"):
  print("\nIgnoring the warning signs, he stepped towards it, oblivious to the lurking danger. With a sudden jolt, the ground crumbled beneath him, and he plummeted into a dark, bottomless hole. The echoes of his cries faded into silence as the game cruelly declared, Game Over, leaving his quest for treasure forever unfinished. \n *** GAME OVER *** ")
else:
  print("\nWith unwavering resolve, he chose the path to the left, venturing deeper into the island's secrets. The trail led him through dense forests and treacherous terrains, testing his every step. Yet, he persevered, overcoming obstacles and solving enigmatic puzzles. And as the sun dipped below the horizon, he emerged victorious, his spirit undaunted, ready for the next leg of his extraordinary journey.")
  print("\nUndeterred by the obstacles on land, the intrepid traveler chose a different approach. With a determined glint in his eyes, he stripped off his gear and dove into the crystal-clear waters surrounding the island. Stroke by stroke, he swam against the currents, exploring the island's hidden depths. The shimmering underwater world revealed a secret entrance, leading him to a mysterious cavern concealed from sight. With a sense of anticipation, he emerged from the water, ready to uncover a new chapter in his quest for treasure.")
  b = input("\nChoose ""SWIM"" or ""WAIT"" near river : \n")
  b_fin = b.lower()
  if(b_fin == "swim"):
    print("\nAs the traveler plunged into the cool depths, unaware of the perils that lay beneath, the serene underwater world transformed into a realm of danger. Suddenly, a school of menacing trout swarmed around him, their sharp teeth glinting with malice. Despite his desperate attempts to fend them off, the relentless assault overwhelmed him. Overpowered and outnumbered, his fate was sealed. The game ominously declared, Game Over, leaving his treasure-seeking ambitions forever submerged. \n ***GAME OVER***")
  else:
    print("\nAs the traveler stood at the crossroads of uncertainty, he chose patience as his ally. Time passed in eerie stillness until, like magic, three mysterious doors materialized before him. The red door beckoned with fiery allure, the blue door whispered secrets of the unknown, and the yellow door shimmered with golden promises. Aware of the treachery that lurked, he weighed his instincts. With cautious optimism, he took a leap of faith and opened the blue door, revealing the pathway to treasure, victory, and the sweet taste of triumph.")
    c = input("\nChoose ""Red"" (or) ""Blue"" (or) ""Yellow"" Door : \n")
    c_fin = c.lower()
    if(c_fin == "red"):
      print("\nIn the face of uncertainty, the traveler's curiosity got the better of him, drawing him towards the crimson allure of the red door. With a trembling hand, he pushed it open, only to be greeted by an inferno of scorching flames. The searing heat consumed him, leaving no chance for escape. As the flames licked at his skin, the game abruptly declared, Game Over, extinguishing his dreams of treasure in a blaze of finality. \n ***GAME OVER***")
    elif(c_fin == "blue"):
      print("\nIntrigued by the enigmatic allure of the blue door, the traveler cautiously stepped inside, hoping for a path to his coveted treasure. Yet, his hopes were shattered as he found himself in the lair of savage beasts. Their primal growls echoed through the air, their hunger unquenchable. With fangs bared and claws poised, they pounced upon him, tearing away any glimmer of hope. The game unceremoniously declared, Game Over, leaving his dreams devoured by the ferocious creatures. \n ***GAME OVER***")
    elif(c_fin == "yellow"):
      print("\nWith a measured breath, the traveler summoned the courage to step through the beckoning threshold of the yellow door. As it swung open, a radiant light enveloped him, revealing a chamber adorned with gleaming treasures. Gasps of awe escaped his lips as he beheld the long-lost riches he had sought. Victory embraced him, his triumph resounding as the game declared, Congratulations! You have found the treasure, and your quest is complete.")
    else:
      print("Game Over")
