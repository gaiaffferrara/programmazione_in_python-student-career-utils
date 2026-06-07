print("SECONDO ASSEGNAMENTO PYTHON: \n 682849 - Dalmasso Noemi, n.dalmasso1@studenti.unipi.it \n 684957 - Ferrara Gaia Federica Francesca, g.ferrara23@studenti.unipi.it \n")

import ast

class Studente:

    def __init__(self, cognome, nome, matricola):
        if type(cognome) is not str:
            raise TypeError("il cognome deve essere una stringa")
        else:
            self.cognome = cognome
        if type(nome) is not str:
            raise TypeError("il nome deve essere una stringa")
        else:
            self.nome = nome
        if type(matricola) is not int:
            raise TypeError("la matricola deve essere un intero")
        if matricola < 0:
            raise ValueError("la matricola deve essere positiva")
        else:
            self.matricola = matricola
            self.listaesami = []    #inizializziamo la lista esami con lista vuota

    def get_cognome(self):
        return self.cognome

    def set_cognome(self, cognome):
        if type(cognome) is not str:
            raise TypeError("il cognome deve essere una stringa")
        else:
            self.cognome = cognome

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        if type(nome) is not str:
            raise TypeError("il nome deve essere una stringa")
        else:
            self.nome = nome

    def get_matricola(self):
        return self.matricola

    def set_matricola(self, matricola):
        if type(matricola) is not int:
            raise TypeError("la matricola deve essere un intero")
        if matricola < 0:
            raise ValueError("la matricola deve essere positiva")
        else:
            self.matricola = matricola

    def set_listaesami(self, listaesami):
        if listaesami == []:
            self.listaesami = listaesami
        else:
            for esame in listaesami: #"esame" è la tupla (codice, voto) in listaesami
                if type(esame) is not tuple:
                    raise TypeError("l'elemento deve essere una tupla composta da (codice, voto)")
                if len(esame) != 2:
                    raise ValueError("la tupla deve essere composta da due elementi")
                if type(esame[0]) is not str:
                    raise TypeError("il codice dell'esame deve essere una stringa")
                if type(esame[1]) is not int:
                    raise TypeError("il voto dell'esame deve essere un intero")
                if not 18 <= esame[1] < 33:
                    raise ValueError("il voto dell'esame deve essere compreso nel range 18-33")
            self.listaesami = listaesami

    def get_listaesami(self):
        return self.listaesami

    def get_voto(self,codice):
        listaesami = self.listaesami
        for esame in listaesami:
            if codice in esame:
                voto = esame[1]
                return voto
        return None

    def __str__(self):
        listaesami = self.listaesami
        if listaesami == []:
            listaesami = "no"
        return self.nome + " " + self.cognome + " mat: " + str(self.matricola) + " esami: " + str(listaesami)

    def __eq__(self, altroStudente):
        return self.cognome == altroStudente.get_cognome() and self.nome == altroStudente.get_nome() and self.matricola == altroStudente.get_matricola()

    def registra_esame(self,codice,voto):
        listaesami = self.listaesami
        for esame in listaesami:    #esame è la tupla (codice,voto)
            if codice == esame[0]:
                return False
        if type(codice) is not str:
            return False
        if type(voto) is not int:
            return False
        if voto < 18 or voto >= 33:
            return False
        else:
            nuovo_esame = (codice, voto)
            listaesami.append(nuovo_esame)
            return True

    def modifica_voto(self,codice,voto):
        listaesami = self.listaesami
        if type(voto) is int and 18 <= voto < 33:
            for i in range(0, len(listaesami)):
                if codice in listaesami[i]:     #listaesami[i] è la coppia (codice,voto) in posizione i
                    listaesami[i] = listaesami[i][:1] + (voto,) #costruiamo una nuova tupla concatenando il codice di quella vecchia con il nuovo voto
                    return True
            return False
        else:
            return False

    def cancella_esame(self,codice):
        listaesami = self.listaesami
        for i in range(0, len(listaesami)):
            if codice in listaesami[i]:
                del listaesami[i]
                return True
        return False

    def media(self):
        somma = 0   #inizializziamo la variabile di accumulazione a 0
        listaesami = self.listaesami
        if listaesami != []:
            for esame in listaesami:
                voto = esame[1]
                somma = somma + voto
            f = somma / len(listaesami)
            return f
        else:
            return None


##################################

class Archivio:

    def __init__(self):
        self.stud = {}     #abbiamo inizializzato l'archivio con un dizionario vuoto

    def inserisci(self, studente, note=""):
        if studente.matricola not in self.stud and type(note) is str:   #controlliamo che lo studente non sia già presente nel dizionario e che le note siano del tipo corretto
            self.stud[studente.matricola] = (studente, note)    #inseriamo lo studente nel dizionario (chiave -> matricola; valore -> tupla composta da (oggetto studente, note))
            return True
        else:
            return False

    def elimina(self,matricola):
        if matricola not in self.stud:
            return False
        else:
            del self.stud[matricola]
            return True

    def get_note(self,matricola):
        if matricola not in self.stud:
            return None
        else:
            valori = self.stud[matricola]   #accesso ai valori(oggetto studente, note) attraverso la chiave corrispondente
            note = valori[1]
            return note

    def get_studenti(self):
        lista_stud = []
        for matricola in self.stud:
            lista_stud.append(matricola)
        return lista_stud

    def modifica_note(self,matricola,nota):
        if matricola not in self.stud or type(nota) is not str:
            return False
        else:
            valori = self.stud[matricola]
            nuovi_valori = valori[:1] + (nota,)  #costruiamo una nuova tupla concatenando l'oggetto studente di quella vecchia con le nuove note
            self.stud[matricola] = nuovi_valori #abbiamo riassegnato ai valori della matricola la nuova riga di valori
            return True

    def __str__ (self):
        stringa = ""
        for matricola in self.stud:
            ogg_stud = self.studente(matricola)     #recuperiamo l'oggetto studente attraverso il metodo "studente" che ha come parametro la matricola
            str_agg = ogg_stud.__str__() + '\n'     #applichiamo il metodo "__str__" della classe Studente su ogg_stud
            stringa += str_agg  #aggiorniamo la stringa con la stringa dello studente successivo
        return stringa

    def studente(self,matricola):
        if matricola not in self.stud:
            return None
        else:
            valori = self.stud[matricola]
            s = valori[0]
            return s

    def registra_esame(self,matricola,codice,voto):
        if matricola in self.stud and type(codice) is str and type(voto) is int and 18 <= voto < 33:
                ogg_stud = self.studente(matricola)
                return ogg_stud.registra_esame(codice, voto)    #utilizziamo il metodo "registra_esame" della classe Studente su ogg_stud
        else:
            return False

    def modifica_voto(self,matricola,codice,voto):
        if matricola in self.stud and type(codice) is str and type(voto) is int and 18<= voto < 33:
                ogg_stud=self.studente(matricola)
                return ogg_stud.modifica_voto(codice,voto)  #utilizziamo il metodo "modifica_voto" della classe Studente su ogg_stud
        else:
            return False

    def cancella_esame(self,matricola,codice):
        if matricola in self.stud and type(codice) is str:
                ogg_stud = self.studente(matricola)
                return ogg_stud.cancella_esame(codice)  #utilizziamo il metodo "cancella_esame" della classe Studente su ogg_stud
        else:
            return False

    def media(self, matricola):
        if matricola in self.stud:
            ogg_stud = self.studente(matricola)
            return ogg_stud.media()     #utilizziamo il metodo "media" della classe Studente su ogg_stud
        else:
            return None

    def lista_studenti_promossi(self,codice,soglia=18):
        lista_promossi = []
        if type(codice) is str:
            for matricola in self.stud:
                ogg_stud = self.studente(matricola)
                voto = ogg_stud.get_voto(codice)    #utilizziamo il metodo "get_voto" della classe Studente su ogg_stud
                if voto is not None and voto >= soglia:
                    cognome = ogg_stud.cognome
                    lista_promossi.append(cognome)
            return lista_promossi

    def conta_studenti_promossi(self, codice, soglia=18):
        n = 0
        if type(codice) is str:
            for matricola in self.stud:
                ogg_stud = self.studente(matricola)
                voto = ogg_stud.get_voto(codice)    #utilizziamo il metodo "get_voto" della classe Studente su ogg_stud
                if voto is not None and voto >= soglia:
                    n += 1
            return n

    def lista_studenti_media(self, soglia=18):
        lista_media = []
        for matricola in self.stud:
            ogg_stud = self.studente(matricola)
            cognome = ogg_stud.cognome
            media_studente = ogg_stud.media()   #utilizziamo il metodo "media" della classe Studente su ogg_stud
            if media_studente is not None and media_studente >= soglia:
                lista_media.append(cognome)
        return lista_media

    def salva(self,nomefile):
        try:
            with open(nomefile, 'w') as file:
                for matricola in self.stud:
                    ogg_stud = self.studente(matricola)
                    note = self.get_note(matricola)
                    dataline = ogg_stud.cognome + ":" + ogg_stud.nome + ":" + str(ogg_stud.matricola)
                    if ogg_stud.listaesami != []:               #se la lista esami ha degli elementi la si aggiunge alla stringa 'dataline'
                        dataline = dataline + ":" + str(ogg_stud.listaesami)
                        if note != "" :                         #se ci sono note le si aggiunge alla stringa 'dataline'
                            dataline = dataline + ":" + note
                    else:                                       #gestisce la situazione in cui la listaesami è vuota ma ci sono note da aggiungere alla stringa 'dataline'
                        if note != "":
                            dataline = dataline + ":" + ":" + note

                    file.write(dataline + '\n')
                return True
        except IOError as e:
            print(nomefile,": ",e)
            return False
        except ValueError as e:
            print(nomefile,": ",e)
            return False

    def carica(self,nomefile):
        try:
            with open(nomefile, 'r') as file:
                file_tot = file.read()          #file_tot è l'intero file come stringa
                lines = file_tot.split("\n")        #lines è la lista che racchiude le singole linee del file
                for line in lines:
                    if not line.strip():    #se la linea è vuota esegue il comando continue
                        continue            #questo comando fa passare il programma all'iterazione successiva (cioè riparte il ciclo for per la linea del file successiva, senza eseguire le altre istruzioni nel ciclo sulla linea corrrente vuota)
                    values = line.split(":")    #values è la lista creata dai inseriti nel file (nomefile) prendendo ':' come separatore
                    if len(values) >= 3:
                        matricola = int(values[2])
                        studente= Studente(values[0], values[1], matricola)
                        if len(values) >= 4 and values[3]!= "":     #specifico che il campo lista esami non debba esere vuoto (nei file è impostato ="" se lo studente ha le note ma non esami)
                            studente.listaesami = ast.literal_eval(values[3])       #valuta la stringa (importata dal file di testo) come una struttura di dati Python, restituendo quindi una lista di tuple
                        else:
                            studente.listaesami = []
                        if len(values) == 5:
                            note = values[4]
                        else:
                            note = ""
                        self.inserisci(studente, note)
                    else:
                        raise Exception("Ci devono essere almeno cognome, nome e matricola")
            return True
        except IOError as e:
            print(nomefile,": ",e)
            return False
        except ValueError as e:
            print(nomefile,": ",e)
            return False
