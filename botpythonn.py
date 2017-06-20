s = input ("Hallo :")

s = input ("Ich möchte mich mit dir unterhalten :")

s=input ("Gibt es etwas, dass du mit absoluter Leidenschaft tust? :")
if "ja" in s:
    print("hört sich ja gut an")
elif "nein" in s:
    print("schade")

s = input ("Was machst du so? :")
if "ich esse gerade" in s:
    print ("guten Appetit")
elif "ich mache nichts" in s:
    print ("ohh")

s = input ("Magst du irgendwelche Serien? :")
if "Ja" in s:
    print ("Ich auch")
elif "nein" in s:
    print ("du bist aber langweilig")

s = input ("Wie war eigentlich dein Urlaub?  :")
if "Sehr gut" in s:
    print ("Freut mich.Meiner auch.")
elif "nicht so gut" in s:
    print ("tja, pech gehabt")

s = input ("Tschüss :")
if "tschüss" in s:
    print ("bye")
    exit ()
elif "wieso" in s:
    print ("Darum")
    exit ()
