room_1 = "baguette_room"
room_2 = "gaming_room # joke i dont have a gaming room :("
room_3 = "back-to-basics"
room = ""
i = 0
coin = 0

game_runtime = True
while game_runtime:
   if room == "" or room == room_1:
      i += 1
      if i==1:
         print ("You enter a new environment, almost, almost as if it was by that program you clicked 'run'")
         print ("Welcome to Baguette's room! You look around and see loads of books that he never reads :?", end='\n')
         print ("Collect 3 Coins to unlock special ending!")
         print ("Do you want to explore further?")
      else:
         print ("Welcome Back to Baguette's room :> I guess you like exploring huh")
         print ("Anyways, Best of luck! :)", "Number of Instances ran :", i)

      arg = input("Enter 'yes' to continue or 'no' to finish the program -->")
      if arg == 'Yes'or arg == 'yes' :
         print ("Well you are a tough explorer aren't you :)")
         print ("1st Room is Baguette's Gaming Room :3c:")
         print ("2nd Room is Baguette's Studio :3c:")
         print ("3rd Room is a secret one >?")
         print ("")
         ab = input("Enter Room to enter!(1/2)")
         if ab == '1':
            room = room_2
         elif ab == '2':
            room = room_3
         elif ab == '3':
            print ("Hint: Secret Room opens through Room_2 :3")
         else: 
            print ("Error Occured -- > Wrong Datatype :(")
            print ("Restarting Program...")
            print ("")

      elif arg == 'no'or arg == 'No' :
         print ("You wish to quit the loop and the program follows your command :)")
         game_runtime = False
      else:
         print ("Wrong Input :(", "Restarting...", sep='\n')
   elif room == room_2:
      print ("You enter Baguette's gaming room!")
      print ("A game in the corner of the room starts!")
      print ("") #Idk bruh either I suck at python of end="\n" isn't working :(
      print ("GAME_1: Welcome to Baguette Counter!")
      print ("")
      print ("Timmy had 23 baguettes, he gave 5 to his sister and stole 10 from his friends. He also travells by a bus everyday on his way to school! If he gave away 12 baguettes on the bus stop, How many baguettes does he have :?")
      a = True
      while a:
         try:
            answer = int(input("Enter Answer:"))
            if answer == 16:
               print ("Yay you answered it correctly! ")
               coin += 1
               print ("Added one coin. Total coins =", coin)
               print ("Transferring to main room :?")
               print ("")
               room = room_1
               break
            else: 
               print (":( Wrong Answer!")
         except:
            print ("Please enter a numerical value :(")
   elif room == room_3:
      print ("You have entered Baguette's Studio Room :yay:")
      print ("This is where Baguette works on his new ysws(back-to-basics) :3")
      print ("")
      print ("Do you know what ysws, this program is being submitted too :$")

