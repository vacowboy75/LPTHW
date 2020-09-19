#This is an attempt at a text-based survival game game.  I'm really not sure how it is going to work out.

def start():
	print("""Your airplane was struck by a missle and you have crash-landed on a mountain side.  Your communications were destroyed.  Everyone onboard has perished except for you and your 11 year-old son.  After looking through the rubble, you were able to secure enough food to last three days at the most.  You have no means to alert anyone of your whereabouts.  How will you survive?  Will your son make it, or will you leave him to fend for himself?\n\nAbout 150 yards ahead, you see something unusual.  As you and your son slowly stagger towards the site, you determine that it is a cave.  What will you do?  Will you GO in or STAY outside?""")
	
	choice = input("Do you want to go in or stay outside?  > ")
	if choice == "go in":
		print("The ground tremors and rocks seal you in separating you from your son.  While he can barely hear you, you tell him to hang tight and try to find help.")
		stepForward()
	elif choice == "stay outside":
		death("How are you going to survive if you do nothing?  You lose!")
	else:
		death("Don't play yourself!  Your choices are to go in or stay outside.  Bye LOSER!")   
		
def tryAgain():
	print("Would you like to try again?  Enter 1 for Yes or 2 for No.")	
	while True:
		try:
			choice = int(input("> "))
			if choice == 1:
				start()
			elif choice == 2:
				print("Thanks for playing.  Good-bye.")
			break
		except ValueError:
			print("Invalid selection!!  Enter 1 for Yes or 2 for No.")
              	
	
def death(how):
	print(how)
	#print("Would you like to try again?  Enter 1 for Yes or 2 for No.")
	tryAgain()
	#while True:
	#	try:
	#		choice = int(input("> "))
	#		if choice == 1:
	#			start()
	#		elif choice == 2:
	#			print("Thanks for playing.  Good-bye.")
	#		break
	#	except ValueError:
	#		print("Invalid selection!!  Enter 1 for Yes or 2 for No.")
			
def stepForward():
	print("Slow is smooth, smooth is fast.  Going too fast in an unstable structure will cause it to crumble.  You have no light and you have no idea what is in front of you.  Do you wish to continue?  Enter Y or N.")
	choice = input("> ")
	if "Y" in choice or "y" in choice:
		while True:
			try:
				steps = int(input("How many steps forward do you wish to take?\n>"))
				if steps == 1:
					print("You took one step forward and you reach out and feel for rocks ahead of you.")
				elif steps > 1:
					death("You walked into the edge of a sharp rock and gouged your eye out.  You lose!")
				break # if either of the conditions above are met, the loop is broken.  Otherwise, the loop will continue as long as the user keeps entering something other than an integer.
			except ValueError:
				print("Please enter a number.")
		findWeapon()
	else:
		#print("Upper case letters only please.")
		death("You must push ahead to save yourself and your son.  You lose!  Try again?")
		
def findWeapon():
	print("You can feel the rocks ahead, and one of them seems quite sharp.  Perhaps, if you can grab hold of that rock, you can use it as a tool or weapon.  However, if you grab that rock and could bring certain and instanenous death.  What will you do?  Will you YANK the rock, slowly SHIMMY the rock, or PRAY for miracle?")
	choice = input("> ")
	if choice == "yank":
		print("More rocks crumble around you, but you manage to survive.  Now you have a rock that you can use to aid in your escape.  To your right, you notice that the rocks seem looser than the others and you decide to slowly dig your way to freedom.")
		batsSnakes()
	elif choice == "shimmy":
		death("Moving the rock made the structure more stable and the cave collapses on you!  You're dead.")
	elif choice == "PRAY":
		death("I believe in the power of prayer, but your son's survival is dependent upon you doing something for yourself.  You died while praying.")
	else:
		death("C'mon Man!")
		
def batsSnakes():
	print("You have spent the last hour digging through rubble and you have created a tunnel that leads to a clearing.  While you still can't see, you can feel that no more rocks are immediately ahead of you.  Here, you decide to take a much needed break.\n\nAfter a few minutes, you hear something hissing that sounds like the hiss of a snake.  Your heart rate elevates, but you refuse to panic.  Your prior military training kicks in and you quickly remember that your son's survival is dependant upon you getting through this situation.  You decide to use your rock to poke at that the snake.  However, the sharp edge of the rock was dulled because you used it to dig this point.  What will you do?  Do you THROW the ROCK and hope that you hit the snake, or do you POKE at the SNAKE and hope you have enough of a sharp edge to kill it?")
	
	choice = input("> ")
	if choice == "throw rock":
		death("You threw the rock but landed only a glancing blow on the snake.  The snake lurches at you and bites you.  It administers a lethal dose of venom and kills you within a matter of minutes.  You died.")
	elif choice == "poke snake":
		print("How many times do you need think you need to poke the snake in order to kill it?")
		attempts = int(input ("> "))
		#print (">>>>", attempts)
		while attempts <= 7:
			if attempts == 0:
				print("How are you doing to kill the snake if you don't even poke at it?  The snakes bites and kills you.")
				pokeAgain()
				break
			elif attempts == 1:
				print("You poke at the snake", attempts, "time but miss.")
				pokeAgain()
				break
			elif 2 <= attempts <= 4:
				print("You strike the snake", attempts, "times but not enough to do kill it!")
				pokeAgain()
				break
			elif 5 <= attempts <= 6:
				print("You strike the snake", attempts, "times, and you dealt a crippling blow!")
				pokeAgain()
				break
			elif attempts == 7:
				print("You strike the snake", attempts, "times, and you killed it!")
				break
			else:
				print("Invalid Number:")
			break
		if attempts > 7:
			death("You have worn yourself poking and missing at the snake.  The snake bites and kills you!")
	else: 
		#else:
		#	death("I don't know what that means.")
			
		print("With the snake dead and you exhausted, you decide to sit down and take another break!  Well deserved.")
	
def pokeAgain():
	print("Would you like to try and poke the snake again?  Enter 1 for Yes or 2 for No.")	
	while True:
		try:
			choice = int(input("> "))
			if choice == 1:
				batsSnakes()
			elif choice == 2:
				print("Thanks for playing.  Good-bye.")
			break
		except ValueError:
			print("Invalid selection!!  Enter 1 for Yes or 2 for No.")
	
start()