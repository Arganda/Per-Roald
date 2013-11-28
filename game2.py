class Scene(object):
	
	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
		exit(1)
	
class Engine(object):#Sørger for at spillet kjøres, nesten som handlers i Assignment 3. 
	
	def __init__(self, scene_map):
		self.scene_map = scene_map
		
	def play(self):#Denne funksjonen blir utført når man starter spillet. Sørger for at man starter på første scene. 
		current_scene = self.scene_map.opening_scene()
		
		while True:#Bytter til neste scene når kravet har blitt innfridd. 
			print "\n--------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
			
class Death(Scene):#Styrer hva som skjer når man dør i spillet. 
	
	quips = [
		"You died. You kinda suck at this, dude.",  #En artig beskjed man får når man dør. 
		"I have a small puppy that's better at this.",
		"You died. Now the Empire of Man will be overrun by murderous megaspiders. Thanks alot!"
		]
		
	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)