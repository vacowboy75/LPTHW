#This is an attempt at a text-based survival game game.  I'm really not sure how it is going to work out.

def start():
	print("""Your airplane was struck by a missle and you have crash-landed on a mountain side.  Your communications were destroyed.  Everyone onboard has perished except for you and your 11 year-old son.  After looking through the rubble, you were able to secure enough food to last three days at the most.  You have no means to alert anyone of your whereabouts.  How will you survive?  Will your son make it, or will you leave him fend for himself?\n\nAbout 150 yards ahead, you see something unusual.  As you and your son slowly stagger towards the site, you determine that it is a cave.  What will you do?  Will you go in or stay outside?""")
	
	choice = input("Do you want to go in or stay outside?  > ")
	if choice == "go in":
		 #or "Go In" or "Go in":
		print("The ground tremors and rocks seal you in separating you from your son.  While he can barely hear you, you tell him to hang tight and try to find help.")
		#decide()
	elif choice == "stay outside":
		death("How are you going to survive if you do nothing?  You lose!")
	else:
		death("Don't play yourself!  Your choices are to go in or stay outside.  Bye LOSER!")
	
#def decide():
	
	
def death(how):
	print(how)
	print("Would you like to try again?  Enter 1 for Yes or 2 for No.")
	
	#try:
	choice = input("> ")
	#	choice = int(input("> "))
		
	#except:
	#	print("Enter 1 for Yes or 2 for No.")	
	print("Enter 1 for Yes or 2 for No.")
		
	#print(">>>", choice)
	
	#if choice == 1:  #I tried try: and except: but it didn't work.
	#	start()
	#elif choice == 2:
	#	print("Thanks for playing.  Good-bye!")	
	if choice.isdigit() == 1:  #I tried try: and except: but it didn't work.
		start()
	elif choice.isdigit() == 2:
		print("Thanks for playing.  Good-bye!")
	elif choice.isdigit() != 1 or 2:
		print("Not an option. ")
	else:
		print("You obviously do not want to play.  Ciao!")
	
		
	
#	finally:
		#print("You must be tired and need a break!  Good-bye!")

#	def goForward(steps):
#	print(f"You took {steps} forward.  Now what would you like to do?")

start()
#dead("You have made a horrible decision and you have failed as father.  Your number one job is to keep your son alive even at your own expense.")