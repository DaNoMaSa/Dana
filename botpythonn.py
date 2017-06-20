name = "botpythonn"
lesezeichen = 0

def sprich(mensch):
    global lesezeichen
    lesezeichen = +1
    if lesezeichen == 1:
        return ("Buenas noches")
    if lesezeichen == 2:
        return ("Wie gehts")
    if lesezeichen == 3:
        return ("Du bist schön")        
    
    chatbot2 = input ("Ich möchte mich mit dir unterhalten :")

    chatbot2 = input ("Gibt es etwas, dass du mit absoluter Leidenschaft tust? :")
    if "ja" in s:
        print("hört sich ja gut an")
    elif "nein" in s:
        print("schade")

"""
chatbot2 = input ("Was machst du so? :")
if "ich esse gerade" in s:
    print ("guten Appetit")
elif "ich mache nichts" in s:
    print ("ohh")

chatbot2 = input ("Magst du irgendwelche Serien? :")
if "Ja" in s:
    print ("Ich auch")
elif "nein" in s:
    print ("du bist aber langweilig")

chatbot2 = input ("Wie war eigentlich dein Urlaub?  :")
if "Sehr gut" in s:
    print ("Freut mich.Meiner auch.")
elif "nicht so gut" in s:
    print ("tja, pech gehabt")

chatbot2 = input ("Tschüss :")
if "tschüss" in s:
    print ("bye")
    exit ()
elif "wieso" in s:
    print ("Darum")
    exit ()
"""
