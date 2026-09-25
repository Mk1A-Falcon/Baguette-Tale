room_1 = "baguette_room"
room_2 = "gaming_room # joke i dont have a gaming room :("
room_3 = "back-to-basics"
room = ""
i = 0
coin = 0

game_runtime = True
while game_runtime:
   i += 1
   if room == "" or room == "room_1":
      if i==1:
         print ("You enter a new environment, almost, almost as if it was by that program you clicked 'run'")
         print ("Welcome to Baguette's room! You look around and see loads of books that he never reads :?", end='/n')
         print ("Collect 3 Coins to unlock special ending!")
         print ("Do you want to explore further?")
      else:
         print ("Welcome Back to Baguette's room :> I guess you like exploring huh")
         print ("Anyways, Best of luck! :)", "Number of Instances ran :", i)

      arg = input("Enter 'yes' to continue or 'no' to finish the program -->")
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
      print ("") #Idk bruh either I suck at python of end="\n" isn't working :(
      print ("Welcome to Baguette Counter!")
      print ("")
      print ("Timmy had 23 baguettes, he gave 5 to his sister and stole 10 from his friends. He also travells by a bus everyday on his way to school! If he gave away 12 baguettes on the bus stop, How many baguettes does he have :?")

      while game_runtime:
         try:
            answer = int(input("Enter Answer:"))
            if answer == 16:
               print ("Yay you answered it correctly! ")
               coin += 1
               print ("Added one coin. Total coins =", coin)
               break
            else: 
               print (":( Wrong Answer!")
         except:
            print ("Please enter a numerical value :(")
