print("PRIMO ASSEGNAMENTO PYTHON: \n Dalmasso Noemi, n.dalmasso1@studenti.unipi.it \n Ferrara Gaia Federica Francesca, g.ferrara23@studenti.unipi.it \n")


#funzione che controlla che il parametro inserito sia una stringa,
#in caso contrario stampa a schermo un messaggio di errore
def controllastr(stringa):
    if type(stringa) is not str:
        print("l'elemento", stringa, "deve essere una stringa")
        return False
    else:
        return True




#funzione che controlla che il parametro inserito (la matricola) sia un intero e sia un numero positivo,
#in caso contrario stampa a schermo un messaggio di errore
def controllamatricola(matricola):
    if type(matricola) is not int:
        print("la matricola", matricola, "deve essere un intero positivo")
        return False
    if not matricola >= 0:
        print("la matricola", matricola, "deve essere un intero positivo")
        return False
    else:
        return True




#funzione che controlla che il parametro inserito (il voto) sia un intero e sia nel range 0-33,
#in caso contrario stampa a schermo un messaggio di errore
def controllavoto(voto):
    if type(voto) is not int:
        print("il voto", voto, "deve essere un intero")
        return False
    if not 0 <= voto <= 33:
        print("il voto", voto, "deve rientrare nel range 0 - 33")
        return False
    else:
        return True




#funzione che esegue i controlli richiesti sugli elementi
#che compongono listaesami; da invocare nella funzione inserisci
def controllatupla(lista):
    for esame in lista:   #ad esame deve corrispondere la coppia (codice, voto)
        if type(esame) is not tuple:   #in caso di inserimenti errati, per esame si intende l'elemento singolo inserito nella lista
            print("l'elemento", esame, "deve essere una tupla composta da (codice, voto)")
            return False
        if len(esame) != 2:
            print("la tupla", esame, "deve essere composta da due elementi")
            return False
        if not controllastr(esame[0]) or not controllavoto(esame[1]):
            return False
    return True



#nella funzione inserisci, tutte le invocazioni delle funzioni precedenti
#servono a controllare se i parametri inseriti sono del tipo corretto
print("Funzione: inserisci")
stud = {}
def inserisci(stud,cognome,nome,matricola,listaesami,note=""):
    flag = False
    if controllastr(cognome):
        if controllastr(nome):
            if controllamatricola(matricola) and matricola not in stud:
                if listaesami == [] or (listaesami != [] and controllatupla(listaesami)):
                    if note == "" or controllastr(note):
                        stud[matricola] = (cognome, nome, matricola, listaesami, note)
                        flag = True

    return flag


print(inserisci(stud, "Rossi", "Mario", 123456, []))
print(inserisci(stud, "Ferrara", "Gaia", 234567, [("235AF", 27), ("987II", 24), ("633UP", 26)]))
print(inserisci(stud, "Bianchi", "Giulia", 111123, [("456MP", 18)]))
print(inserisci(stud, "Genti", "Luigi", 555352, [("987II", 25)], "da convalidare"))
print(inserisci(stud, "De Micheli", "Marta", 987342, [("633UP", 16)], "CSTR"))
print(inserisci(stud, "Venchi", "Francesco", 734251, []))
print(inserisci(stud, "Dalmasso", "Noemi", 233621, [("633UP", 27), ("235AF", 25)]))
print(inserisci(stud, "Ferrero", "Alessia", 109011, [], "studentessa trasferita"))
print(inserisci(stud, "Verdi", "Paolo", 666777, [("633UP", 21)]))
print(inserisci(stud, "Costa", "Sara", 876444, []))




print("\nFunzione: serializza")
def serializza (stud):
    s = ""  #creazione di una stringa vuota a cui aggiungere, con il ciclo for, le righe del dizionario
    for k in stud:
        v = stud.get(k)     #assegniamo alla variabile v la vista dei valori (cognome, nome, matricola, listaesami, note) associati alla chiave k
        mat = str(v[2])
        listaesami = v[3]
        note = v[4]
        if listaesami == []:
            esami = "no"
        else:
            esami = str(listaesami)     #genera una rappresentazione come stringa delle tuple che compongono listaesami
        if note == "":
            note = "no"

        a = (v[0], v[1], "MAT:", mat, "ESAMI:", esami, "NOTE:",  note, '\n')
        glue = " "
        s = s + glue.join(a)    #schema di accumulazione per concatenare a s la stringa dello studente
    return s

print(serializza(stud))




print("Funzione: studente")
def studente(stud,matricola):
    if controllamatricola(matricola):
        v = stud.get(matricola)
        return v

print(studente(stud,234567))




print("\nFunzione: registra esame")
def registra_esame(stud,matricola,codice,voto):
    flag = False
    if controllamatricola(matricola) and matricola in stud:
        if controllastr(codice) and controllavoto(voto):
            v = stud.get(matricola)
            listaesami = v[3]
            i = 0
            while i < len(listaesami):      #ciclo per controllare che il parametro codice inserito non sia uguale a un codice già presente in lista
                if listaesami[i][0] == codice:  #essendo listaesami[i] la coppia (codice,voto) in posizione i, ne controlliamo l'elemento con indice 0
                    return False
                else:
                    i = i + 1
            nuovo_esame = (codice, voto)
            listaesami.append(nuovo_esame)
            flag = True

    return flag

print(registra_esame(stud, 234567, "567FA", 24))




print("\nFunzione: media")
def media(stud, matricola):
    somma = 0
    if controllamatricola(matricola) and matricola in stud:
        v = stud.get(matricola)
        listaesami = v[3]
        if listaesami != []:
            for esame in listaesami:
                voto = esame[1]
                somma = somma + voto
            f = somma / len(listaesami)
            return f
    else:
        return None

print (media(stud, 234567))




print("\nFunzione: modifica voto")
def modifica_voto(stud,matricola,codice,voto):
    flag = False
    if controllamatricola(matricola) and matricola in stud:
        if controllastr(codice) and controllavoto(voto):
            v = stud.get(matricola)
            listaesami = v[3]
            for i in range(0, len(listaesami)):
                if listaesami[i][0] == codice:              #listaesami[i] è la coppia (codice, voto) in posizione i
                    listaesami[i] = listaesami[i][:1] + (voto,) #concatenazione di una parte della vecchia tupla (il codice) con il nuovo voto
                    flag = True
    return flag

print(modifica_voto(stud, 234567, "235AF", 28))




print("\nFunzione: cancella esame")
def cancella_esame(stud,matricola,codice):
    flag = False
    if controllamatricola(matricola) and matricola in stud:
        if controllastr(codice):
            v = stud.get(matricola)
            listaesami = v[3]
            i = 0
            while i < len(listaesami):
                if listaesami[i][0] == codice:
                    del listaesami[i]
                    flag = True
                else:
                    i += 1

    return flag

print(cancella_esame(stud, 234567, "235AF"))




print("\nFunzione: lista studenti promossi")
def lista_studenti_promossi(stud,codice,soglia=18):
    lista_promossi = []
    if controllastr(codice):
        for k in stud:
            v = stud.get(k)
            listaesami = v[3]
            cognome_nome = v[0] + " " + v[1]
            i = 0
            while i < len(listaesami):
                if listaesami[i][0] == codice:
                    if listaesami[i][1] >= soglia:
                        lista_promossi.append(cognome_nome)
                i += 1
        return lista_promossi

print(lista_studenti_promossi(stud, "633UP"))




print("\nFunzione: conta studenti promossi")
def conta_studenti_promossi(stud, codice, soglia=18):
    n_promossi = 0
    if controllastr(codice):
        for k in stud:
            v = stud.get(k)
            listaesami = v[3]
            i = 0
            while i < len(listaesami):
                if listaesami[i][0] == codice:
                    if listaesami[i][1] >= soglia:
                        n_promossi = n_promossi + 1
                i += 1
        return n_promossi

print(conta_studenti_promossi(stud, "633UP"))




print("\nFunzione: lista studenti media")
def lista_studenti_media (stud, soglia=18):
    lista_media = []
    for k in stud:
        v = stud.get(k)
        cognome_nome = v[0] + " " + v[1]
        a = media(stud, k)               #richiamiamo la funzione media(stud,matricola)
        if a!= None and a >= soglia:     #applichiamo i controlli ad a, ossia al valore di ritorno di media(stud,matricola)
            lista_media.append(cognome_nome)
    return lista_media

print(lista_studenti_media(stud))
