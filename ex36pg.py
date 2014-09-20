from sys import exit
from os import system
from Room_Info import room_info

inventory = []
global plank_in_place
plank_in_place = 1



def start_room(): 	
	system('cls')
	room_info("""You find yourself in an empty room with one door to the 
	left and one door to the right.""")

	next = raw_input("> ")

	if next in ['left', 'go left', 'walk left']:
		system('cls')
		pit_room(first)
	elif next in ['right', 'go right', 'walk right']
		system('cls')
		Plank_room()
	else:
		dead("You walk around the room in confusion until you starve.")

def dead(why):
	print why, "Good job!"
	exit(0)


def pit_room():
	print "As you close the door behind you, you see a huge crack in the"
	print "floor from one end of the room to the other. There is sharp spears on the bottom." 
	print "You can also see a door on the other side. "
	print "There got to be something you can use to cross."
	print "But the room is empty..."
	crack = 0
	while True:
		next = raw_input("\n> ")

		if next in ["plank","place plank"]:
			
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
			system('cls')
			start_room()
		
		#REMOVE_CHEAT
		elif next == "cheatplank":
			inventory.append("plank")

		elif next == "door" or next == "go up":
			if crack == 1:
				print "You carefully walk over the plank and move to the next room."
				system('cls')
				Treassure_room()

			else:
				print ("I can't make the jump over that crack.")

		elif next in ["jump","jump over"]:
			dead("You try to jump over the crack, but it's to wide. You fall and get stabbed \n by the spears at the bottom.")
		
		else:
			print("I have no idea what %r means.") % next


def Plank_room():
	global plank_in_place
	if plank_in_place == 1:
		print """This room looks empty. There is a window 
	with some light shining through, and a loose plank on the ground."""
	else:
		print("""This room looks empty. There is a window 
	with some light shining through.""")


	while True:
		next = raw_input("> ")
		if next == "take plank" and plank_in_place == 1:
			print("You pick up the plank and placed it in your inventory.")
			inventory.append("plank")
			plank_in_place = 0

		elif next == "take plank" and plank_in_place == 0 and "plank" in inventory:
			print ("You already got that in your inventory.")

		elif next == "take plank" and plank_in_place == 0 and not "plank" in inventory:
			print ("You already placed the plank on the crack.")

		elif next in ["back","go back"]:
			system('cls')
			start_room()

		else:
			print("I have no idea what %r means.") % next


def Treassure_room():
	print ("As you walk  ")
	exit(0)

start_room()
