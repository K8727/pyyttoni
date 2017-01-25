#Miikka Mutanen
#19.1.2017
#tehtävä 2-2
#funktio muuttaa bitit->kilobiteiksi, megoiksi ja gigoiksi
#Tulostaa tuloksen
#Example output tehtävänannosta:
#Give your input in bytes: 1563200
#bytes  1563200 B
#Kilobytes  1526.5625 KB
#Megabytes  1.49078369140625 MB
#Gigabytes  0.001455843448638916 GB
def muunna_bitteja(luku):
	print("Bytes "+str(luku)+" B")
	print("Kilobytes "+str(luku/2**10)+" KB")
	print("Megabytes "+str(luku/2**10/2**10)+" MB")
	print("Gigabytes "+str(luku/2**10/2**10/2**10)+" GB")
	
#muunna_bitteja(1563200)
muunna_bitteja(int(input("Anna bittien määrä>")))