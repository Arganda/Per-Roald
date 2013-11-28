from sys import exit
from random import randint

class Scene(object):

	def enter(self):
		print ""
		exit(1)
		
class Engine(object):
	
	def __init__(self, scene_map):
		self.scene_map = scene_map
		
	def play(self):
		current_scene = self.scene_map.opening_scene()
		
		while True:
			print "\n--------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
			
class Death(Scene):

	quips = [
		"Losers go home"
	]
		
	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)
		
class SchoolYard(Scene):

    def enter(self):
        print "It is the first day of school"
        print "The big school yard is in front of you"
        print "You have arrived without your books, money and computer."
        print "You must now survive the without these assets, unless you "
        print "manage to steal them."
        print "\n"
        print "You're running down the school yard to the nerdy kids when"
        print "one of them takes out their new computer"
        print "You like it"
        print "Are you going to steal, leave or stab'n'steal"
		


        action = raw_input("> ")

        if action == "steal":
            print "You take his computer from his arms."
            print "He is stronger than you could ever imagine"
            print "He wrestles you off and you get angry"
            print "You try to destroy the computer"
            print "He defends it with his life, and you fail"
            print "You are now the biggest loser in school."
            return 'death'

        elif action == "leave":
            print "You walk towards the nerds."
            print "They are talking about something interesting."
            print "Suddenly one of them tackles you"
            print "You fall and the entire school laughs at you."
            print "You rise again, but you walk away with your tail between your legs."
            print "You are now the biggest loser in school."
            return 'death'

        elif action == "stab'n'steal":
            print "You are a nerveous person, and brought a knife."
            print "You pull the knife and walk determined toward the nerd with the new computer"
            print "You stab him in the back and takes his computer"
            print "The other kids screams as they realize what you have done"
            print "They run away from you in fear"
            print "You proceed to the classroom"
            return 'classroom'

        else:
            print "DOES NOT COMPUTE!"
            return 'School_Yard'
			
class ClassRoom(Scene):

    def enter(self):
        print "You walk into the classroom"
        print "Most classmates greet you normally."
        print "You still need the books for the course"
        print "One lonely kid has all the books"
        print "He is mentally retarded and only communicate with codes"
        print "If you tell him the right code, he will give you the books"
        print "The code is two digits between 1 and 3"
        code = "%d%d" % (randint(1,3), randint(1,3))
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print "wrong!"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "That is the right combination for me to give you these books"
            print "Here you are, they are all yours"
            print "Now you study and get perfect grades"
            return 'cafeteria'
        else:
            print "He is tired of you trying different codes"
            print "Because each one triggers an action from him."
            print "After making him scream, dance and eat, the others think you are a bully"
            print "Your are now the biggest loser in school"
            return 'death'



class Cafeteria(Scene):

    def enter(self):
        print "After a successful lecture you want some food from the cafeteria "
        print "Without money this is a problem"
        print "You see many kids eating food, but you want it fresh"
        print "You walk towards the cafeteria"
        print "You think about stealing food or money"
        print "Do you steal money from students or food from cafeteria."

        action = raw_input("> ")

        if action == "steal food":
            print "You walk up to the disk and place a sandwich"
            print "in your pocket and walks away"
            print "You get an arm around you and you are caught."
            print "as punishment you are placed in a pillory."
            print "Other students throw tomatoes and cabbage at you."
            print "You are now the biggest loser in school"
            return 'death'

        elif action == "steal money":
            print "You see a group of younger students at one table"
            print "You walk to them and says they have to give you their money."
            print "At first they resist, but you use brute force and they yield."
            print "They start taking their money out of their pockets."
            print "After earning 100 bucks,"
            print "you buy yourself a big meal with lots of meat."
            print "It tastes good,"
            print "and when you are done it is time to go home."
            return 'way_home'
        else:
            print "DOES NOT COMPUTE!"
            return "cafeteria"


class WayHome(Scene):

    def enter(self):
        print "There are 4 ways home"
        print "But three of them are blocked by angry people"
        print "One is blocked by the friends of the nerd you stabbed"
        print "One by the parents of the retarded kid you took the books from"
        print "One by the kids you stole money from"
        print "You have to take a chance where to go"
        print "Which one do you take?"

        good_way = randint(1,4)
        guess = raw_input("[ways #]> ")


        if int(guess) != good_way:
            print "You take way %s and it is blocked." % guess
            print "The angry mob hates you and beats you "
            print "They set fire to your clothes and you get first degree burns"
            print "You are now the biggest loser in school."
            return 'death'
        else:
            print "You take way %s and it is clear" % guess
            print "You walk home with no hard feelings"
            print "It is survival of the fittest"
            print "In addition you are now an owner of a brand new"
            print "Computer and curriculum books"
            print "You managed to get through the day!"


            return 'finished'
			
class Map(object):

	scenes = {
		'school_yard': SchoolYard(),
		'classroom': ClassRoom(),
		'cafeteria': Cafeteria(),
		'way_home': WayHome(),
		'death': Death()
	}
	
	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)
		
a_map = Map('school_yard')
a_game = Engine(a_map)
a_game.play()