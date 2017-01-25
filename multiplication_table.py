#Miikka Mutanen
#23.1.2017
#tehtävä 2-5
#Ohjelma tulostaa kertotaulun
#käyttäjän antaman kertojan ylärajan perusteella
'''
esim
Example output:

upper limit>4
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
'''

#tulostaa 1-10 kertotaulun kertojan rajaan asti
def tulosta_kertotaulu(raja):
	kantaluku=0
	summa=0
	if raja>10: raja=10 #estetään tulostus liian suurilla kertojilla
	while kantaluku<10:
		kantaluku+=1
		for i in range(1,raja+1):
			summa=kantaluku*i
			print("%d * %d = %d" %(kantaluku, i, summa))
		
while True:
	try:
		tulosta_kertotaulu(int(input("Anna luku ")))
		break
	except ValueError:
		print("Anna kokonaisluku")