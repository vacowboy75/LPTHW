#This is an attempt at a text-based survival game game.  I'm really not sure how it is going to work out.

def start():
	choice = input("""Your airplane was struck by a missle and you have crash-landed on a mountain side.  Your communications were destroyed.  Everyone onboard has perished except for you and your 11 year-old son.  After looking through the rubble, you were able to secure enough food to last three days at the most.  You have no means to alert anyone of your whereabouts.  How will you survive?  Will your son make it, or will you leave him to fend for himself?\n\nAbout 150 yards ahead, you see something unusual.  As you and your son slowly stagger towards the site, you determine that it is a cave.  What will you do?  Will you GO in or STAY outside?\n """).strip().upper()

	#acceptableWordsGo = ["GO", "go in", "Go In", "go"] # make options a list variable as opposed to a constant
	#acceptableWordsStay = ["STAY", "stay outside", "STAY outside"]
	#choice = input("Do you want to go in or stay outside?  > ")
	if choice == "GO":
		print("The ground tremors and suddenly rocks fall and seal you in separating you from your son.  You yell out trying to determine whether your son is ok.  While he can barely hear you, you tell him to hang tight and try to find help.")
		stepForward()
	elif choice == "STAY":
		death("How are you going to survive if you do nothing?  You lose!")
	else:
		death("Don't play yourself!  Your choices are to GO in or STAY outside.  Bye LOSER!")

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
			else:
				("Invalid selection!!  Enter 1 for Yes or 2 for No.")
			#break
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
	print("Slow is smooth, smooth is fast.  Going too fast in an unstable structure will cause it to crumble.  You have no light and you have no idea what is in front of you.  You begin to truly feel the gravity of your situation and fear begins paralyze your body.  Do you wish to continue?  Enter Y or N.")
	choice = input("> ")
	if "Y" in choice or "y" in choice:
		try:
			while True:
				steps = int(input("How many steps forward do you wish to take?\n>"))
				if steps == 1:
					print("You face your fear and take one step forward while reaching out to feel for rocks ahead of you.")
					break
				elif steps > 1:
					death("You walked into the edge of a sharp rock and gouged your eye out.  You lose!")
				#break # if either of the conditions above are met, the loop is broken.  Otherwise, the loop will continue as long as the user keeps entering something other than an integer.
		except ValueError:
			print("Please enter either Y or N.")
		findWeapon()
	else:
		#print("Upper case letters only please.")
		death("You must push ahead to save yourself and your son.  You lose!")

def findWeapon():
	choice = input("You can feel the rocks ahead, and one of them seems quite sharp.  Perhaps, if you can grab hold of that rock, you can use it as a tool or weapon.  However, if you grab that rock and could bring certain and instanenous death.  What will you do?  Will you YANK the rock, slowly SHIMMY the rock, or PRAY for miracle?\n\n>").strip().upper()
	#acceptableYank = ["YANK", "yank"]  Is it worth changing the code for two a list variable as opposed to leaving the constants?
	#choice = input("> ")
	if choice == "YANK": #in choice or "yank" in choice:
		print("More rocks crumble around you, but you manage to survive.  Now you have a rock that you can use to aid in your escape.  To your right, you notice that the rocks seem looser than the others and you decide to slowly dig your way to freedom.")
		pokeSnakes()
	elif choice == "SHIMMY": #in choice or "shimmy" in choice:
		death("Shimmying the rock made the structure unstable and the cave collapses on you!  You're dead.")
	elif choice == "PRAY": #"pray" in choice or "PRAY" in choice:
		death("I believe in the power of prayer, but your son's survival is dependent upon you doing something for yourself.  Don't you know faith without works is dead?  You died while praying.")
	else:
		death("C'mon Man!  You shoud know better by now.")

def pokeSnakes():
	choice = input("You have spent the last hour digging through rubble and you have created a tunnel that leads to a clearing.  While you still can't see, you can feel that no more rocks are immediately ahead of you.  Here, you decide to take a much needed break.\n\nAfter a few minutes, you hear something hissing that sounds like the hiss of a snake.  Your heart rate elevates, but you refuse to panic.  Your prior military training kicks in and you quickly remember that your son's survival is dependant upon you getting through this situation.  You consider using the rock to poke at the snake.  However, the sharp edge of the rock was dulled because you used it to dig through the rubble to get to this point.  What will you do?  Do you THROW the rock and hope that you hit the snake, or do you POKE at the snake and hope you have enough of a sharp edge to kill it?\n> ").strip().upper()

	#acceptableThrow = ["THROW ROCK", "throw rock", "Throw rock", "Throw the Rock"]
	#acceptablePoke = ["Poke Snake", "Poke the Snake", "POKE SNAKE"]

	#choice = input("> ")
	#if choice in acceptableThrow:
	if choice == "THROW":
		death("You threw the rock but landed only a glancing blow on the snake.  The snake lurches at you and bites you.  It administers a lethal dose of venom and kills you within a matter of minutes.  You died.")
	#elif choice in acceptablePoke:
	elif choice == "POKE":
		attempts = int(input("How many times do you think you need to poke the snake in order to kill it?\n\n>"))
		#attempts = int(input ("> "))
		#print (">>>>", attempts)
	try:
		while True:
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
				print("You strike the snake", attempts, "times, and you dealt a crippling blow, but still not enough to kill it!")
				pokeAgain()
				break
			elif attempts == 7:
				print("You strike the snake", attempts, "times, and you killed it!")
				break
			elif attempts > 7:
				death("You have worn yourself poking at the snake and missing.  The snake bites you, injecting toxic amounts of venom into your blood stream.  You're dead!")
			else:
				print("Invalid Number:")
	except ValueError:
			print("Please enter an integer value.")
			pokeSnakes()
	else:
		print("Not an option!  The options are THROW or POKE.\n\n")
		pokeSnakes()

#Eelse:
		#else:
		#	death("I don't know what that means.")

		print("With the snake dead and you exhausted, you decide to sit down and take another break!  Well deserved.\n\n\n\n")

def bats():
	print("As you sit down and begin to relax, your realize how worn out you actually are, you can't help it and your eyes begin to close.  Out of nowhere you hear the screeches of bats.  You suddenly jump up and grab the rock that you had.  You throw the rock as hard as you can in the direction of the screeching sounds, hit one of the bats flush.  The bat falls to the ground with a thud that you can hear over the screeches of the other bats.  Unfortunately you cannot tell how many bats remain, but you know that there is more than one bat headed in your direction.  How many rocks do you pick up and throw at the bats? ")

	rocks = int(input("> "))
	if rocks < 5:
		print("You do not have enough to kill all of the bats.")
		death("You piss off one of the bats and it bites you and gives you rabies.  You die from rabies!")
	elif rocks == 5:
		print("Somehow, by the grace of God, you blindly hit one of the screeching bats and neutralize the threat.")
		#escape()
	elif rocks > 5:
		print("Because of your age, your arm gives out and you can't throw anything! You are swarmed by the colony of bats.  One of them bites you and you die of rabies!")
	else:
		print("You do no")

def pokeAgain():
	print("Would you like to try and poke the snake again?  Enter 1 for Yes or 2 for No.")
	while True:
		choice = int(input("> "))
		try:
			if choice == 1:
				pokeRepeat()
			elif choice == 2:
				print("Thanks for playing.  Good-bye.")
			else:
				print("Invalid selection!!\n\n  Enter 1 for Yes or 2 for No.")
		except ValueError:
			print("Enter 1 for Yes or 2 for No.")
		#break
def pokeRepeat():
	print("How many times do you think you need to poke the snake in order to kill it?")
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
			print("You strike the snake", attempts, "times, and you dealt a crippling blow, but still not enough to kill it!")
			pokeAgain()
			#break
		elif attempts == 7:
			print("You strike the snake", attempts, "times, and you killed it!")
			break
		else:
			print("Invalid Number:")
		break
	if attempts > 7:
		death("You have worn yourself poking at the snake and missing.  The snake bites you, injecting toxic amounts of venom into your blood stream.  You're dead!")


start()
