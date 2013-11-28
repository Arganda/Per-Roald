from game2 import Scene, Death, Engine

from sys import exit
from random import randint

#Det som er markert oransje, blir importert fra game2. 
"""class Scene(object):
	
	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
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
		"You died. You kinda suck at this, dude.",
		"I have a small puppy that's better at this.",
		"You died. Now the Empire of Man will be overrun by murderous megaspiders. Thanks alot!"
		]
		
	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1) 
"""		
class RedFlats(Scene):

	def enter(self):
		print "You're the only remaining Space Marine of the expedition crew sent to this planet."
		print "You have to finish the mission before you can return back to your flagship, the Speartip, with the Drop-Pod."		
		print "There is a hive nearby, where the Arachnids breed and give birth to their young."
		print "It must be destroyed, lest the Arachnids will overrun the Galactic Empire of Man!"
		print "The hives are beyond the Red Flats and deep into the jungle to the west."
		print "\n"
		print "You start running west, towards the hives, with your chainsword and bolter at the ready."
		print "You almost reach the jungle when you suddenly hear a trampling noise, followed by a gigantic Arachnid bursting through "
		print "the trees and out into the Red Flats. The Arachnid has seen you, and it's coming straight for you, "
		print "with its front pincers ready to bite your head off!"
		print "Take action now, Soldier!"
		
		action = raw_input("> ")
		
		if action == "charge!":
			print "You immediately charge the Arachnid, with your chainsword in hand, and the warcry of the Luna Wolves "
			print "rings out across the open area. Lupercal!"
			print "As you close up on the Arachnid, it shoots a blob of goo straight in your face, making you blind."
			print "You try to remove your helmet, but the goo act as cement and has sealed the helmet together with your breastplate."
			print "You hear the sound of the Arachnids pincers coming closer, before everything turns black."
			return 'death'
		
		elif action == "shoot!":
			print "Without a split-second doubt, you yank out your Bolter and start shooting at the oncoming Arachnid."
			print "The Arachnid is unbelievably fast, jumping from left to right, all the while closing up on you."
			print "You start scoring hits with your bolter as the Arachnid comes closer; and suddenly it falls to the ground, "
			print "most of its legs are gone. It screams in pain as it lies on the ground, its body spasming."
			print "You take out your Chainsword and chop its head off in one clean cut."
			return 'jungle'
			
		else:
			print "DOES NOT COMPUTE! (charge! or shoot!)"
			return 'red_flats'
			
class Jungle(Scene):

	def enter(self):
		print "After taking care of the Arachnid, you move into the jungle, glad that you finally have some cover."
		print "After only a few minutes you find the Arachnid hive, an enormous hollow with see-through egg-sacs dotting the ground."
		print "You seek cover behind a small hill, and look down at the hollow."
		print "A few Arachnids are patrolling around their eggs, watching over them. They are not aware of your presence. Yet."
		print "You have to eliminate the Arachnids to successfully plant the dynamite in the hive." 
		print "What do you do?"
		
		action = raw_input("> ")
		
		if action == "charge!":
			print "You draw out your chainsword with a loud rasping noise that catch the immediate attention of the Arachnids."
			print "They turn toward the source of the sound, just as you come charging down the hill with great speed, and into the hollow."
			print "You cut off the head of the first Arachnid before they even realize what is happening."
			print "Three other Arachnids are in the hollow, and now they start circling you, closing in on every side, leaving no escape route."
			print "You yell out your battlecry as the first Arachnid attacks you with its deadly pincers, but you manage to deflect the attack, "
			print "before delivering a crushing blow to the head."
			print "No sooner than the first of the three Arachnids lay dead at your feet, the other two pierce you with their pincers, "
			print "through your armour like a warm knife through butter."
			print "Your vision starts to fade, as you manage to register an immense pain from your chest; the Arachnids are sucking out your organs."
			return 'death'
			
		elif action == "shoot!":
			print "You crawl up to the edge of the hill, gazing down on the four Arachnids guarding over their eggs."
			print "You pull out your bolter from your belt holster, and start unloading the clip on the horrifying creatures."
			print "The first Arachnid is killed instantly by a shot to the head, its four pincer-arms flailing in its last life-spasms."
			print "Through years of training, your bolter-skills are second to none, as you routinely blast two more Arachnids to the ground."
			print "The last Arachnid comes charging up the hill towards you, just as you're out of ammunition in your bolter."
			print "You toss it aside and pull out your chainsword, deflecting a multitude of attacks from the enraged Arachnid."
			print "With immense strength, you manage to get on the offensive, dealing blow after blow until your sword finally hits home."
			print "The Arachnid screams a wicked painful scream as it falls to the ground. You finish it off with the Mercy-Strike, cutting off its head."
			
		else:
			print "DOES NOT COMPUTE! (charge! or shoot!)"
			return 'drop_pod'
			
class Drop_pod(Scene):

		def enter(self):
			print "The Hive is bombed to smitherines, and you've reached back to your drop-pod."
			print "You get in your seat and close the door, now the drop-pod looks like a giant seed."
			print "The engines power up easily, and you shoot through the sky, out into space, the way now open to you after you destroyed the Hive."
			print "After arriving at your flagship, you pop a flask of champagne with your fellow soldiers, another mission accomplished."
			print "Gratz mate, you won!"
			return 'finished'
			
class Map(object):

	scenes = {
		'RedFlats': RedFlats(),
		'Jungle': Jungle(),
		'Drop_pod': Drop_pod(),
		'Death': Death()
		}
		
	def __init__(self, start_scene):
			self.start_scene = start_scene
			
	def next_scene(self, scene_name):
			return Map.scenes.get(scene_name)
			
	def opening_scene(self):
			return self.next_scene(self.start_scene)
			
a_map = Map('RedFlats')
a_game = Engine(a_map)
a_game.play()