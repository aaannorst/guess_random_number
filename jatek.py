import random

print("szamjatek")
nev = input("Mi a neved?\n")
print("Üdv, {}".format(nev))
print("Gondoltam egy számra 1 és 100 közt, találd ki!")

uj_jatek = input("Van-e kedved játszani? [y/n]\n")
if uj_jatek != "y":
	print("Viszlát, {}!".format(nev))
	exit(0)
print("Játék kezdődik!\n")

random.seed(432)
n_random = random.randint(1,100)

tip = 0
while tip != n_random:
	tip_str = input("Mi a tipped?\n")
	tip = int(tip_str)
	if tip < n_random:
		print("Nagyobb számra gondoltam\n")
	elif tip > n_random:
		print("Kisebb számra gondoltam\n")
print("Eltaláltad!\n")
