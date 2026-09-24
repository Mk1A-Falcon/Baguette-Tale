room_1 = "baguette_room"
room_2 = "gaming_room # joke i dont have a gaming room :("
room_3 = "back-to-basics"
room = ""
i = 0

game_runtime = True
while game_runtime:
   i += 1
   print ("You enter a new environment, almost, almost as if it was by that program you clicked 'run'")
   print ("Welcome to Baguette's room! You look around and see loads of books that he never reads :?", end='\n')
   print ("Do you want to explore further? :>")
   arg = input("Enter 'yes' to continue or 'no' to finish the program! >")
   if arg == 'Yes'or arg == 'yes' :
      print ("Loading....", end='\n')
      room = room_2
   elif arg == 'no'or arg == 'No' :
      print ("You wish to quit the loop and the program follows your command :)")

