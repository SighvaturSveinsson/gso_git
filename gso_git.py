#GSÖ verkefni
#Sighvatur Sveinsson
#25.1.2017

#Forritið býr til skrá
skra = input("Hvað á skráin að heita ")
skraNafn = skra + ".txt"

minSkra = open(skraNafn, "w")

#Skrifa í skránna og loka henni
minSkra.write("Ég elska pepsi max" + "\n")
minSkra.close()

#Opna skránna aftur, skrifa amk 3 línur og loka henni
minSkra = open(skraNafn, "a")
for i in range(3):
    lina = input("Skráðu nýja línu í skránna ")
    minSkra.write(lina + "\n")
minSkra.close()
