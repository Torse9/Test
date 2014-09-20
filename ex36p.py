from sys import exit
from os import system
from time import sleep


#Retarded ideas
#Bedre inventory
inventory = []
global plank_in_place
plank_in_place = 1
global crack
crack = 0

def start_room():
	system('cls')
	print "You find yourself in an empty black painted room with a metallic rimmed door to" 
	print "the left and one wooden door to the right."
	print""
	print"What do you do?"
	
	while True:
		
		next = raw_input("> ")
		if next in ["walk left","go left","left","move left","go to the left"]:
			system('cls')
			pit_room()
		elif next in ["walk right","go right","right","move right","go to the right"]:  
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
	print why, "Good job!"
	exit(0)


def pit_room():
	global crack

	if crack == 0:
		print "As you close the door behind you, you see a huge crack in the"
		print "floor from one end of the room to the other." 
		print "You can also see a door on the other side. "
		print "There got to be something you can use to cross."
		print "But the room is empty..."
	else:
		print "As you close the door behind you, you see a huge crack in the"
		print "floor from one end of the room to the other."
		print " But you have already placed a plank there."


	while True:
		next = raw_input("\n> ")

		if next in ["plank","place plank","use plank","place plank on crack","place plank crack"]:
			
			if "plank" in inventory and crack == 0:
				crack = 1
				print ("You place the plank on the crack.")
				inventory.remove("plank")
				print ("You can go up to the next room now.")#Explain how,
			
			elif crack == 0:
				print ("Yes, maybe there is a plank somewhere... but not here")	
			else:
				print "You have already placed a plank there"
				
		elif next == "go back" or next == "back":
			print "You open the door and go back"
			sleep(2)
			system('cls')
			start_room()
		
		### TEST INVENTORY ###
		elif next == "inventory":
			print ("Inventory:\n %r ") % (inventory)
		
		#REMOVE_CHEAT
		elif next == "cheatplank":
			inventory.append("plank")

		elif next in ["cross plank","walk across plank","walk over plank","move over plank","cross","walk plank","walk plank"]:
			if crack == 1:
				print "You carefully walk over the plank and move to the next room."
				sleep(3)
				system('cls')
				Treassure_room()

			else:
				print ("I can't make the jump over that crack.")

		elif next in ["jump","jump over"]:
			y = raw_input("Are you sure you want to jump over? The crack is very deep...\n> ")

			if y in ["Yes","yes","I'm sure","Absolutely","absolutely","y","ye","yup","yeah"]:
				dead("You try to jump over the crack, but it's to wide. You fall and get stabbed \n by the spears at the bottom.")
			else:
				print("You changed your mind.")

		elif next in ["pick up plank",] and plank_in_place == 0:
			print ("You pick the plank up again and place it in your inventory")
			plank_in_place = 1

		elif next in ["cut plank"] and "plank" in inventory:
			print("You cut the plank into a spear")
			inventory.remove("plank")
			inventory.append("spear")

		else:
			print("I have no idea what %r means.") % next


def Plank_room():
	global plank_in_place
	if plank_in_place == 1:
		print """This room looks empty. There is a window 
	with some light shining through, and a loose plank on the ground."""
	else:
		print("""This room looks empty. There is a window 
	with some light shining through. 
	All of a sudden, you smell an aweful stench! You wonder what it is about....""")


	while True:
		next = raw_input("> ")
		if next in ["take plank","pick up plank","pick plank","plank"] and plank_in_place == 1:
			print("You pick up the plank and placed it in your inventory.")
			inventory.append("plank")
			plank_in_place = 0

		elif next in ["take plank","pick up plank","pick plank","plank"] and plank_in_place == 0 and "plank" in inventory:
			print ("You already got that in your inventory.")

		elif next in ["take plank","pick up plank","pick plank","plank"] and plank_in_place == 0 and not "plank" in inventory:
			print ("You already placed the plank on the crack.")

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
	print "This is a test of the new room."
	print "Going through the door you enter a deep and dimly lit cave."
	print "But you can see a huge sleeping bear right right in the middle of the caveroom.!"
	print "You don't know if it is aggressive but do you take the risk?"
	print "Do you approach him, or try to sneak by carefully?"


	while True:
		next = raw_input(">")
		
		if next in ["approach","approach him","approach it"]:
			print ("You approach him")
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
	print ("You approach the bear, but the bear....")
	
		
		
				





def bear_sneak():
	print("You try to sneak by the bear")
	print ("...")
	sleep(3)
	print("......")
	sleep(2)


start_room()