print("szamjatek")
nev = input("Mi a neved?\n")
print("Üdv, {}".format(nev))
print("Gondoltam egy számra 1 és 100 közt, találd ki!")
uj_jatek = input("Van-e kedved játszani? [y/n]\n")
if uj_jatek != "y":
	print("Viszlát, {}!".format(nev))
	exit(0)
print("Játék kezdődik!\n")

