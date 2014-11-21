from sys import exit
from os import system
from time import sleep


#Retarded ideas
#Bedre inventory
inventory = []
inventory.append("knife")
global plank_in_place
plank_in_place = 1
global hole
hole = 0

def start_room():
	system('cls')

	print "You are in a black empty room with a metallic rimmed door to" 
	print "the left and a wooden door to the right."
	print""
	
	print"What do you do?"

	while True:
		
		next = raw_input("> ")
		if next in ["walk left","go left","left","move left","go to the left","metallic door","go to the metallic door","go metallic door","go metallic door","go to metal","go metal"]:
			print("You open the door.")
			sleep(1)
			system('cls')
			pit_room()
		elif next in ["walk right","go right","right","move right","go to the right"]:  
			print("You open the door.")
			sleep(1)
			system('cls')
			Plank_room()
	#Cheat ;)
		elif next == "bear":
			bear_room()
		
		elif next == "spear":
			inventory.append("spear")
		
		### TEST INVENTORY ###
		elif next == "inventory":
			print ("Inventory:\n %r ") % (inventory)

		else:
			dead("You walk around the room in confusion until you starve.")

def dead(why):
	system('COLOR 0C')
	print why, "Good job!"
	raw_input("")
	system('COLOR 07')
	exit(0)


def pit_room():
	global hole

	if hole == 0:
		print "You close the door behind you."
		print "\n\n"
		print "There is a huge hole in the"
		print "floor from one end of the room to the other."
		print ""
		print "It's not possible to cross." 
		print ""
		print "You see a door on the other side. "
		print ""
		print item_in_room("pit_room")
	else:
		print "You close the door behind you."
		print "You see a huge hole in the"
		print "floor from one end of the room to the other."
		print "You have already placed a plank there."


	while True:
		next = raw_input("\n> ")

		if next in ["plank","place plank","use plank","place plank on hole","place plank hole"]:
			
			if "plank" in inventory and hole == 0:
				hole = 1
				print ("You place the plank on the hole.")
				inventory.remove("plank")
				print ("You can go up to the next room now.")#Explain how,
			
			elif hole == 0:
				print ("Yes, maybe there is a plank somewhere... but not here")	
			else:
				print "You have already placed a plank there"
				
		elif next == "go back" or next == "back":
			print "You open the door and go back"
			sleep(1)
			system('cls')
			start_room()
		
		### TEST INVENTORY ###
		elif next == "inventory":
			print ("Inventory:\n %r ") % (inventory)
		
		#REMOVE_CHEAT
		elif next == "cheatplank":
			inventory.append("plank")

		elif next in ["cross plank","walk across plank","walk over plank","move over plank","cross","walk plank","walk plank"]:
			if hole == 1:
				print "You carefully walk over the plank and move to the next room."
				sleep(3)
				system('cls')
				Treassure_room()

			else:
				print ("I can't make the jump over that hole.")

		elif next in ["jump","jump over"]:
			y = raw_input("Are you sure you want to jump over? The hole is very deep...\n> ")

			if y in ["Yes","yes","I'm sure","Absolutely","absolutely","y","ye","yup","yeah"]:
				dead("You try to jump over the hole, but it's to wide. You fall and get stabbed \n by the spears at the bottom.")
			else:
				print("You changed your mind.")

		elif next in ["pick up plank",] and plank_in_place == 0:
			print ("You pick the plank up again and place it in your inventory")
			plank_in_place = 1

		elif next in ["cut plank"] and "plank" in inventory and 'knife' in inventory:
			print("You cut the plank into a spear")
			inventory.remove("plank")
			inventory.append("spear")

		else:
			print("I have no idea what %r means.") % next


def item_in_room(floor):
	if floor == "pit_room":
		print ("Right so far")
	if floor == "plank_room":
		print ("That is correct")


def Plank_room():
	global plank_in_place
	if plank_in_place == 1:
		print """This room looks empty. There is a window 
		with some light shining through, and a loose plank on the ground."""
		print item_in_room("plank_room")
	
	else:
		print("""This room looks empty. There is a window 
		with some light shining through.""")


	while True:
		next = raw_input("> ")
		if next in ["take plank","pick up plank","pick plank","plank"] and plank_in_place == 1:
			print("You pick up the plank and placed it in your inventory.")
			inventory.append("plank")
			plank_in_place = 0

		elif next in ["take plank","pick up plank","pick plank","plank"] and plank_in_place == 0 and "plank" in inventory:
			print ("You already got that in your inventory.")

		elif next in ["take plank","pick up plank","pick plank","plank"] and plank_in_place == 0 and not "plank" in inventory:
			print ("You already placed the plank on the hole.")

		elif next in ["back","go back"]:
			system('cls')
			start_room()

		else:
			print("I have no idea what %r means.") % next


def Treassure_room():
	bear_room()
	#print ("You win")
	#print ("Game is over.. for now. I'll be adding more later. Hopefully.")
	#exit(0)


#### lage et spyd av planken for aa drepe bjornen. Eller snike forbi den med mulighet til aa feile underveis.

def bear_room():
	x = 0
	print "Going through the door you enter a deep and dimly lit cave."
	print "But you can see a huge sleeping bear right right in the middle of the caveroom.!"
	print "You don't know if it is aggressive but do you take the risk?"
	print "Do you approach him, or try to sneak by carefully?"


	while True:
		next = raw_input(">")
		
		if next in ["approach","approach him","approach it"]:
			print ("You approach it")
			bear_approach()
		elif next in ["sneak","sneak by"]:
			bear_sneak()
		#Nikos Ide
		elif next in ["climb","mount"]:
			print("%r what") % (next)
			q = raw_input(">")

			
			if q in ["bear","mount bear","climb bear"]:
				print ("You do that fuck you.")
			else:
				pass

		elif next in ["stab the bear with spear","stab bear","stab",] and 'spear' in inventory:
			print("You kill the bear")
			print("He is now dead.")

		elif next in ["mount the bear","mount bear","jump on bear","ride bear","ride the bear","slap"]:	
			print ("You mount the bear")
			print("It wakes up")	
			print ("")
			dead("It licks your little nick.")


		elif next in["back","go back"]:
			print ("You go back through the door.")
			sleep(2)
			pit_room()

		else:
			if x < 3:
				print ("You don't have time to fool around! Tell me what to do before it's too late.")
				x += 1
		
			else:
				dead("The bear wakes up and aggressively rips your head off.")	


def bear_approach():
	print ("You approach the bear...")
	sleep(1)
	print("")
	
		
		
			

def bear_sneak():
	print("You try to sneak by the bear")
	print ("...")
	sleep(3)
	print("......")
	sleep(2)
	check = raw_input("The bear snores loudly, do you continue to walk or stop?\n> ")

	if check == "continue":
		print("You continue to sneak")
		print("The bear wakes up and rips your head off.")
		dead("Yep")
	else:
		print("You stop")
		print("The bear takes a deep breath and snore some more.")
		print("You: Pheew!")
start_room()