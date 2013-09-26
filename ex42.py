## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass
	
## is-a relationsip, a dog is an animal. 
class Dog(Animal):
	
	def __init__(self, name):
		## has-a relationship, self has a name. 
		self.name = name
		
## is-a relationship, a cat is an animal
class Cat(Animal):

	def __init__(self, name):
		## has-a relationship, self has a name.
		self.name = name

## is-a relationship
class Person(object):

	def __init__(self, name):
	## has-a relationship
	self.name = name
	
	## Person has-a pet of some kind
	self.pet = None

## is-a relationship
class Employee(Person):

	def __init__(self, name, salary):
		## is-a relationship, hmm what is this strange magic
		super(Employee, self).__init__(name)
		## has-a relationship
		self.salary = salary

## is-a relationship
class Fish(object):
	pass
	
## is-a relationship
class Salmon(Fish):
	pass
	
## is-a relationship
class Halibut(Fish):
	pass
	
	
## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## Mary is-a person
mary = Person("Mary")

## Mary has-a pet named Satan
mary.pet = satan

## Frank is-a Employee
frank = Employee("Frank", 120000)

## Frank has-a pet named Rover
frank.pet = rover

## Flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## Harry is-a Halibut
harry = Halibut()