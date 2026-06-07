from stud import *
from testMy import *

def controllo():
    #contiamo i test falliti
    testFalliti = 0 #variabile di accumulazione inizializzata a 0

    #test di controllo stringhe
    print("\n \n ==========> Test aggiuntivo controllo stringa")
    testFalliti += testEqual(controllastr("stringa"), True)
    testFalliti += testEqual(controllastr("ciao"), True)
    testFalliti += testEqual(controllastr(456), False) #int, quindi False
    testFalliti += testEqual(controllastr(23.5), False) #float, quindi False
    testFalliti += testEqual(controllastr(-453.46), False) #float negativo, quindi False
    testFalliti += testEqual(controllastr(("ciao", 1)), False) #tupla, quindi False

    #test di controllo della matricola
    #la matricola deve essere un intero positivo
    print("\n \n ==========> Test aggiuntivo controllo matricola")
    testFalliti += testEqual(controllamatricola(12), True)
    testFalliti += testEqual(controllamatricola(469372), True)
    testFalliti += testEqual(controllamatricola(13.5), False) #float, quindi False
    testFalliti += testEqual(controllamatricola("SLPJHB"), False) #str, quindi False
    testFalliti += testEqual(controllamatricola(-1235), False) #int negativo, quindi False
    testFalliti += testEqual(controllamatricola(("ciao", 1)), False) #tupla, quindi False

    #test di controllo del voto
    #il voto deve essere un intero positivo nel range 0-33
    print("\n \n ==========> Test aggiuntivo controllo voto")
    testFalliti += testEqual(controllavoto(33), True)
    testFalliti += testEqual(controllavoto(17), True)
    testFalliti += testEqual(controllavoto(-1), False) #fuori dal range, quindi False
    testFalliti += testEqual(controllavoto(67), False) #fuori dal range, quindi False
    testFalliti += testEqual(controllavoto(24.6), False) #float, quindi False
    testFalliti += testEqual(controllavoto("dodici"), False) #str, quindi False
    testFalliti += testEqual(controllavoto(("ciao", 1)), False) #tupla, quindi False

    #test controllo tuple
    print("\n \n ==========> Test aggiuntivo controllo tupla")
    testFalliti += testEqual(controllatupla([("235AF", 27), ("987II", 24), ("633UP", 26)]), True)
    testFalliti += testEqual(controllatupla([("777UU", 12), ("765PP", 22), ("888MI", 29)]), True)
    testFalliti += testEqual(controllatupla([-234, ("633UP", 26), ("235AF", 27)]), False) #il primo elemento è un int negativo
    testFalliti += testEqual(controllatupla([("235AF", 27), 12, ("633UP", 26)]), False) #il secondo elemento è un int
    testFalliti += testEqual(controllatupla([("CIAO", -234), ("633UP", 26), ("235AF", 27)]), False) #il secondo elemento della prima tupla non è nel range
    testFalliti += testEqual(controllatupla([("633UP", 2, 6)]), False) #la tupla ha 3 elementi
    testFalliti += testEqual(controllatupla([(13, 27), ("987II", 24), ("633UP", 26)]), False) #la prima tupla è composta da 2 interi


    # abbiamo finito ?
    if testFalliti == 0:
        print("\t****Test completati -- effettuare la consegna come da README")
    else:
        print("Test falliti: ", testFalliti)


# eseguo i test automatici
controllo()

