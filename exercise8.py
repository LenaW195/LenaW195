def vokon_zählen(x): # funktion definieren
    vokale = "aeiou" # definieren der Vokale, Python versteht das als einzelne Teile wie eine Liste, könnte auch vokale = ["a", "e",..]
    x_lower = x.lower() # input x wird jetzt klein geschrieben
    
     # 2 list komprehensions, 1 liste sind Buchstaben
    buchstaben = [i for i in x_lower if i.isalpha()] # i steht für ein element, das jedes dort durchgegangen wird, kännte auch jeder andere Buchstabe genommen werden
    # geprüft ob jedes element in der list x_lower ist ein Buchstabe, beide also konsonanten und vokale sind in dieser Lilste gespeichert
    vokale = [i for i in buchstaben if i in vokale] #speicher alle elemente(i) ub buchstaben listen in vokale wenn i einer der vorher definierten vokale ist
   
    #return [len(buchstaben), len(vokale)]

#print(vokon_zählen("HI,&%/ BerliN!!"))   # konsonante sind hier differenz aus buchstaben und vokale
  
 #Abwandlung

    print(f"Es gibt {len(vokale)} Vokale und {len(buchstaben) - len(vokale)} Konsonanten.")
     # zum interaktiven Verbinden der Bestandteile, im String is jetzt code drin in "  "
     
vokon_zählen("HallO,&%/ BerliN!!")
     