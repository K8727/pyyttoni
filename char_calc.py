#Miikka Mutanen
#19.1.2017
#tehtävä 2-1
#Laskee annetusta merkkijonosta annetut kirjaimet ja muutkin merkit
#tulostaa tuloksen
#Tulostus eroaa tehtävänannon esimerkistä
import doctest
def laske_kirjaimia(kirjaimet, jono):
	'''
	>>> laske_kirjaimia(['a'],"aaaAAbbCC")
	Kirjainta a oli 3kpl
	>>> laske_kirjaimia(['a','A',' '],"a aaAAbbCC")
	Kirjainta a oli 3kpl
	Kirjainta A oli 2kpl
	Kirjainta   oli 1kpl
	>>> laske_kirjaimia([],"aaaAAbbCC")
	
	>>>
	'''
	i=0
	for k in kirjaimet:
		i=0
		for c in jono: 
			if k==c: i+=1
		#print("Merkkijonossa '"+jono+"'")
		print("Kirjainta "+k+ " oli "+str(i)+"kpl")
	
laske_kirjaimia(['a','A','e','E'],input("Anna merkkijono>"))
doctest.testmod()