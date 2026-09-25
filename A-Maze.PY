room_1 = "baguette_room"
room_2 = "gaming_room # joke i dont have a gaming room :("
room_3 = "back-to-basics"
room_4 = "ball required"
room = ""
i = 0
r = 0 #room_3 mechanics
coin = 0

game_runtime = True
while game_runtime:
   if coin == 3:
      print ("It seems you have collected all 3 coins!")
      op = input ("Trigger Special Ending? (Y/N) >")
      if op == 'Y' or op == 'y':
         print ("")
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
         print ("Number of Coins", coin)

      arg = input("Enter 'yes' to continue or 'no' to finish the program --> ")
      print ("")
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
      print ("")
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
      r = 0
      print ("You have entered Baguette's Studio Room :yay:")
      print ("This is where Baguette works on his new ysws(back-to-basics) :3")
      print ("")
      print ("Do you know what ysws, this program is being submitted too :$")
      while True:
         r += 1
         ab = input("Enter Answer :3 -->")
         print ("")
         if ab == "folktale" or ab == "Folktale" or ab == "FOLKTALE":
            print ("CORRECT ANSWER :LESSGOO:")
            coin += 1
            if r == 1: 
               print ("It looks like you got it first try :3")
               print ("Do you want to enter the secret room?? (prize=2coins)")
               arw = input("Enter (y/n) >")
               if arw == 'y' or arw == 'Y':
                  print ("Loading Secret Room :)")
                  print ("")
                  room = room_4
                  break
               else:
                  print ("Oke, No entry for you :(")
                  print ("Refreshing Program...")
                  print ("")
                  room = room_1
                  break
            else:
               print("Total coins,",coin)
               print("Resetting program...")
               print("")
               room = room_1
               break
         else:
            print ("Wrong answer :( Try Again?")
   elif room == room_4:
      print ("Alas explorer, you reach the secret room!")
      print ("Many have tried, but failed to enter this room")
      print ("Winning this next game will give you 2 Coins, but losing will reset it to 0!")
      print ("Do you wish to continue??")
      print("")
      
      while True: 
         aj = input("Enter Your Decision(y/n) >")
         print("")
         if aj == 'y' or aj == "Y":
            print ('Starting game....')
            print ("")
            print ("Question: Who Founded Hack Club?")
            print ("A. Brendan (I mean he could tbh he is goated)")
            print ("B. *Zach Latta* :3")
            print ("C. Orpheus")
            print ("D. Daven (Oh God, not the planet Destroyer)")
            arww=input("Enter your answer(A/B/C/D) >")
            if arww == "A" or arww == 'a':
               print ("Well, Not the correct answer but Yk :SHRUG3D:")
               coin = 0
               print ("Deducted all coins! Total coins left >", coin)
               print ("Resetting the entire program..")
               print ("")
               i = 0
               room = room_1
               break
            elif arww == 'b' or arww == "B" :
               print ("Correct Answer!")
               coin +=2
               print ("Added 2 coins! Total coins =", coin)
               print ("Redirecting to Main Room :)")
               room = room_1
               break
            else: 
               print ("Wrong Answer :(")
               coin = 0
               print ("Deducted all coins! Total coins left >", coin)
               print ("Resetting the entire program..")
               print ("")
               i=0
               room = room_1
               break
         elif aj == "n" or aj == "N":
            print ("I see you play safe, Well not everyone is brave enough to take the risk!")
            print ("Refreshing Program...")
            print ("")
            room = room_1
            break
         else: 
            print ("Wrong input, try again.")
            print ("")