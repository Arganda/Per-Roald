"""Her er en haug med kode som jeg har sett igjennom og rettet 
en del skrivefeil.
"""

def break_words(words):
	"""This function will break up words for us."""
	words = words.split(' ')
	return words
	
def sort_words(words):
	"""Sorts the words."""
	return sorted(words)
	
def print_first_word(words): #Satt inn kolon. 
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print word
	
def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1) #Satt inn parantes. 
	print word
	
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)
	
def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
	
def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
	
print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
\twith logic so firmly planted
\tcannot discern the needs of love
\tnor comprehend passion from intuition
\tand requires an explantion
\twhere there is none.
"""
							#Diktet ser bedre ut, fjernet en del linebreaks.

print "--------------"
print poem
print "--------------"

six = 10 - 2 + 3 - 5
print "This should be six: %s" % six	#Endret fra 'five' til 'six'. Her kunne jeg endret regnestykket ved å bytte ut tallvariablene istedet.

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000		#feil slash.
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point) #satt inn en parantes på slutten.


sentence = "All good things come to those who wait."	#fikset noen grammatikkfeil og fjernet tabs.

words = break_words(sentence)
sorted_words = sort_words(words)

print_first_word(words)
print_last_word(words)				#En del skrivefeil og syntaxfeil her som jeg fikset, fra linje 78 til 90.
print_first_word(sorted_words)		
print_last_word(sorted_words)
sorted_words = sort_sentence(sentence)
print sorted_words

print_first_and_last(sentence)

print_first_and_last_sorted(sentence)
