room_1 = "baguette_room"
room_2 = "gaming_room # joke i dont have a gaming room :("
room_3 = "back-to-basics"
room = ""
i = 0

game_runtime = True
while game_runtime:
   i += 1
   if room == "" or room == "room_1":
      if i==1:
         print ("You enter a new environment, almost, almost as if it was by that program you clicked 'run'")
         print ("Welcome to Baguette's room! You look around and see loads of books that he never reads :?", end='/n')
         print ("Do you want to explore further?")
      else:
         print ("Welcome Back to Baguette's room :> I guess you like exploring huh")
         print ("Anyways, Best of luck! :)", "Number of Instances ran :", i)

      arg = input("Enter 'yes' to continue or 'no' to finish the program! >")
      if arg == 'Yes'or arg == 'yes' :
         print ("Loading....", end='\n')
         room = room_2

      elif arg == 'no'or arg == 'No' :
         print ("You wish to quit the loop and the program follows your command :)")
         game_runtime = False
      else:
         print ("Wrong Input :(", "Restarting...", sep='\n')
   elif room == room_2:
      print ("You enter Baguette's gaming room!")
      print ("A game in the corner of the room starts!")
      

