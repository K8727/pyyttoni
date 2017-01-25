#Miikka Mutanen
#25.1.2017
#tehtävä 2-3 
#Grade calculator
#tehvävänanto:
#Ask two grades from the user:
#a) exam point   (0-24)
#b) demo points  (0-12)
#and calculate the total based on the following table: 
#
#	>= 33 	=> 5
#	>= 29 	=> 4
#	>= 25 	=> 3
#	>= 21 	=> 2
#	>= 18 	=> 1
#	< 18   	=> 0
#Palauttaa koepisteiden ja demopisteiden perusteella lasketun arvosanan
def grade_calculator(exam,demo):
	summa=(exam+demo)
	grade=0
	if summa>=33:
		grade=5
	elif summa>=29:
		grade=4
	elif summa>=25:
		grade=3
	elif summa>=21:
		grade=2
	elif summa>=18:
		grade=1
	else :
		grade=0
	print("With total points %d, the final grade was %d"%(summa,grade))

grade_calculator(21,6)