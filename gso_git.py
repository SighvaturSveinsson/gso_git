#GSÖ verkefni
#Sighvatur Sveinsson
#25.1.2017

#Forritið býr til skrá
skra = input("Hvað á skráin að heita ")
skraNafn = skra + ".txt"

minSkra = open(skraNafn, "w+")

#Skrifa í skránna og loka henni
minSkra.write("Ég elska pepsi max")
minSkra.close()