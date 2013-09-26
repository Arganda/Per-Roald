from sys import argv

script, filename = argv
#Definerer åpning av fil. Se linje 8.  
txt = open(filename)
#En linje som printer, en som åpner tekstfila. 
print "here's your file %r:" % filename
print txt.read()
#Sender forespørsel en gang til.
print "Type the filename again:"
file_again = raw_input("> ")
#Kaller på fila.
txt_again = open(file_again)
#Skriver ut fila.
print txt_again.read()