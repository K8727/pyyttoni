#Miikka Mutanen
#23.1.2017
#tehtävä 2-4
#Ohjelma laskee käyttäjän antamat komentorivi
#arkumentit yhteen ja tulostaa ne
#hylkää epäkelvot arkumentit
import doctest #testausta varten
import sys

#Summaa listan luvut
#return summa
def sum(lista):
	'''
	>>> sum([1,2,3,4,5])
	15
	>>> sum([0,0,0,0,0])
	0
	>>> sum([1.5,0,1.5,0,0])
	3.0
	>>> sum([-1.5,0,-1.6,0,0])
	-3.1
	>>> sum([-1.5,0,10.5,0,0])
	9.0
	>>> sum([1.5,0,1,0,0])
	2.5
	>>> sum([])
	0
	'''
	summa=0
	for i in lista:
		summa+=i
	return summa

lista=[]
for i in sys.argv[1:]:
	try:
		lista.append(int(i))
	except ValueError:
		print("Anna pelkästään kokonaislukuja")
	
print("Total sum for args is "+str(sum(lista)))

doctest.testmod()
	