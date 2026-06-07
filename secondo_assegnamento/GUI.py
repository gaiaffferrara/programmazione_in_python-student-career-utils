print("SECONDO ASSEGNAMENTO PYTHON: \n 682849 - Dalmasso Noemi, n.dalmasso1@studenti.unipi.it \n 684957 - Ferrara Gaia Federica Francesca, g.ferrara23@studenti.unipi.it \n")


from archivio import *
import tkinter as tk
from tkinter import messagebox


class myApp:

    def __init__ (self,root):
        self.root = root
        self.dizionario = Archivio()

    #Aspetto

        self.root.title("Gestionale Archivio Studenti")

        #frame istruzioni
        self.frame_istr = tk.Frame(self.root,relief=tk.RAISED, borderwidth=1, background="light grey")
        self.frame_istr.pack(side= tk.TOP, expand=True, fill=tk.X)       #fill=tk.X la rende responsive orizzontalmente

        #label fisse istruzioni
        self.label_fissa = tk.Label(self.frame_istr, background="light grey", text="ISTRUZIONI: \n 1. Cliccare sull'operazione desiderata \n 2. Inserire i dati richiesti \n 3. Premere 'invio' per eseguirla")
        self.label_fissa.pack(side = tk.TOP, expand=True, padx=5, pady=5)

        self.label_fissa2 = tk.Label(self.frame_istr, background="tomato", text="Se viene richiesto più di un dato usare  ':' come separatore")
        self.label_fissa2.pack(side = tk.TOP, expand=True, padx=5, pady=5)

        #frame dove avvengono le azioni
        self.frame_azione = tk.Frame(self.root,relief=tk.RAISED, borderwidth=1)
        self.frame_azione.pack(side = tk.RIGHT, expand=True, fill=tk.X)

        #label per le info
        self.info_var = tk.StringVar()
        self.label_info = tk.Label(self.frame_azione, width=100, textvariable=self.info_var)
        self.label_info.pack( expand=True, fill = tk.X, padx=5, pady=5)

        #entry
        self.entry = tk.Entry(self.frame_azione, width=100)
        self.entry.pack(expand=True, fill=tk.X,  padx=15, pady=5)
        self.entry.bind("<Return>", self.funzioni)      #bind che collega il tasto 'invio' al metodo 'funzioni' (che gestisce i metodi delle azioni principali)

        self.funzioni_var=tk.StringVar()        #variabile il cui valore determina, nel metodo funzioni, il metodo da eseguire

        #label mostra risultati
        self.archivio_var = tk.StringVar()
        self.label_mostra = tk.Label(self.frame_azione, width=100, background="light grey", textvariable=self.archivio_var)
        self.label_mostra.pack(side=tk.BOTTOM, expand=True,  fill=tk.X, padx=15, pady=5)

        #frame bottoni
        self.frame_bottoni = tk.Frame(self.root,relief=tk.RAISED, borderwidth=1)
        self.frame_bottoni.pack(side = tk.LEFT)

        #vari bottoni
        self.btn_visualizza = tk.Button(self.frame_bottoni, text="Visualizza Archivio",background="light green",width=25)
        self.btn_visualizza.pack( padx=5, pady=5)
        self.btn_visualizza.bind("<Button-1>", self.visualizza)

#da qua la bind non è con il metodo che esegue l'azione ma con il metodo che mostra le istruzioni di compilazione e setta le variabili
        self.btn_visualizza_note = tk.Button(self.frame_bottoni, text="Visualizza Note Studente",background="light green",width=25)
        self.btn_visualizza_note.pack( padx=5, pady=5)
        self.btn_visualizza_note.bind("<Button-1>", self.info_visualizza_note)

        self.btn_inserisci = tk.Button(self.frame_bottoni,text="Inserisci Nuovo Studente",background="light green",width=25)
        self.btn_inserisci.pack(padx=5, pady=5)
        self.btn_inserisci.bind("<Button-1>", self.info_inserisci_stud)

        self.btn_modifica_cognome = tk.Button(self.frame_bottoni, text="Modifica Cognome Studente",background="light green",width=25)
        self.btn_modifica_cognome.pack(padx=5, pady=5)
        self.btn_modifica_cognome.bind("<Button-1>", self.info_mod_cognome)

        self.btn_modifica_nome = tk.Button(self.frame_bottoni, text="Modifica Nome Studente",background="light green",width=25)
        self.btn_modifica_nome.pack(padx=5, pady=5)
        self.btn_modifica_nome.bind("<Button-1>", self.info_mod_nome)

        self.btn_aggiungi_esame = tk.Button(self.frame_bottoni, text="Aggiungi Esame",background="light green",width=25)
        self.btn_aggiungi_esame.pack( padx=5, pady=5)
        self.btn_aggiungi_esame.bind("<Button-1>", self.info_aggiungi_esame)

        self.btn_modifica_voto = tk.Button(self.frame_bottoni, text="Modifica Voto Esame",background="light green",width=25)
        self.btn_modifica_voto.pack( padx=5, pady=5)
        self.btn_modifica_voto.bind("<Button-1>", self.info_mod_voto)

        self.btn_elimina_esame = tk.Button(self.frame_bottoni, text="Elimina Esame",background="light green",width=25)
        self.btn_elimina_esame.pack( padx=5, pady=5)
        self.btn_elimina_esame.bind("<Button-1>", self.info_elimina_esame)

        self.btn_modifica_note = tk.Button(self.frame_bottoni, text="Modifica Note Studente",background="light green",width=25)
        self.btn_modifica_note.pack(padx=5, pady=5)
        self.btn_modifica_note.bind("<Button-1>", self.info_mod_note)

        self.btn_cancella = tk.Button(self.frame_bottoni, text="Cancella Studente",background="light green",width=25)
        self.btn_cancella.pack(padx=5, pady=5)
        self.btn_cancella.bind("<Button-1>", self.info_cancella_stud)

        self.btn_media = tk.Button(self.frame_bottoni, text="Calcola Media Voti",background="light green",width=25)
        self.btn_media.pack(padx=5, pady=5)
        self.btn_media.bind("<Button-1>", self.info_calcola_media)

        self.btn_carica = tk.Button(self.frame_bottoni, text="Carica Archivio",background="light green",width=25)
        self.btn_carica.pack(padx=5, pady=5)
        self.btn_carica.bind("<Button-1>", self.info_carica_arch)

        self.btn_salva = tk.Button(self.frame_bottoni, text="Salva Archivio",background="light green",width=25)
        self.btn_salva.pack(padx=5, pady=5)
        self.btn_salva.bind("<Button-1>", self.info_salva_arch)

        self.btn_esci = tk.Button(self.frame_bottoni, text="ESCI",background="tomato",width=25)
        self.btn_esci.pack(padx=5, pady=25)
        self.btn_esci.bind("<Button-1>", self.esci)


    ''' Ad eccezione del metodo 'visualizza' per ogni azione sono stati costruiti due metodi:
        1. info_nomemetodo -> mostra le istruzioni di compilazione e setta la variabile 'funzioni_var' con il valore corrispondente al bottone premuto
                (metodo richiamato al click del bottone)
        2. nomemetodo ->  svolge l'azione vera e propria prevista dal bottone 
                (metodo richiamato dal metodo 'funzioni')

        Il metodo 'funzioni' gestisce i metodi delle vere e proprie azioni in base al valore della variabile 'funzioni_var'
                (metodo richiamato premendo 'invio' dalla entry)
    '''

    def funzioni(self,evento):
            if self.funzioni_var.get() == "visualizza_note":
                self.visualizza_note(evento)
            if self.funzioni_var.get() == "inserisci":
                self.inserisci_stud(evento)
            if self.funzioni_var.get() == "mod_cognome":
                self.mod_cognome(evento)
            if self.funzioni_var.get() == "mod_nome":
                self.mod_nome(evento)
            if self.funzioni_var.get() == "aggiungi_esame":
                self.aggiungi_esame(evento)
            if self.funzioni_var.get() == "mod_voto":
                self.mod_voto(evento)
            if self.funzioni_var.get() == "elimina_esame":
                self.elimina_esame(evento)
            if self.funzioni_var.get() == "mod_note":
                self.mod_note(evento)
            if self.funzioni_var.get() == "cancella_stud":
                self.cancella_stud(evento)
            if self.funzioni_var.get() == "calcola_media":
                self.calcola_media(evento)
            if self.funzioni_var.get() == "carica_arch":
                self.carica_arch(evento)
            if self.funzioni_var.get() == "salva_arch":
                self.salva_arch(evento)


    def visualizza(self, evento):
        self.btn_visualizza.focus()
        self.info_var.set("")
        self.archivio_var.set(self.dizionario.__str__())


    def info_visualizza_note(self,evento):
        self.btn_visualizza_note.focus()
        self.archivio_var.set("")         #variabile della label mostra
        self.info_var.set("VISUALIZZA NOTE STUDENTE -> Inserire la matricola dello studente di cui si vogliono visualizzare le note")      #variabile della label info
        self.funzioni_var.set("visualizza_note")        #variabile per definire il metodo da eseguire dopo la compilazione

    def visualizza_note(self,evento):
        try:
            matricola= int(self.entry.get())
            if self.dizionario.get_note(matricola) != None:     #controllo che l'esecuzione della funzione get_note sia andata a buon fine (return != None)
                self.archivio_var.set(str(matricola) + ": note=" + str(self.dizionario.get_note(matricola)))        #settiamo il valore della label_mostra, che stampa a schermo i rultati dell'azione
                self.entry.delete(0, tk.END)            #delete permette di cancellare il contenuto della entry
            else:
                messagebox.showwarning("errore", "Impossibile accedere alle note dello studente")
        except Exception as e:
            messagebox.showwarning("errore", "Errore nell'inserimento dei dati:\n" + str(e))


    def info_inserisci_stud(self, evento):
        self.btn_inserisci.focus()
        self.archivio_var.set("")
        self.info_var.set("INSERISCI STUDENTE -> Inserire cognome, nome, matricola, note(facoltative)")
        self.funzioni_var.set("inserisci")

    def inserisci_stud(self, evento):
        try:
            stud = self.entry.get().split(":")      #stud è la lista creata dalla stringa di valori inseriti in ingresso prendendo ':' come separatore
            if len(stud) == 4:                  #controllo sulla lunghezza della lista per verificare se sono presenti delle note
                note = stud[3]
            else:
                note = ""
            if self.dizionario.inserisci(Studente(stud[0], stud[1], int(stud[2])), note):
                self.archivio_var.set("lo studente " + stud[0] +" "+ stud[1] + " è stato inserito correttamente. \n \n Premere 'Visualizza Archivio' per vedere l'inserimento in archivio")
                self.entry.delete(0, tk.END)
            else:
                messagebox.showwarning("errore", "Lo studente non è stato inserito correttamente, ricontrollare i dati")
        except Exception as e :
            messagebox.showwarning("errore", "Errore nell'inserimento dei dati:\n" + str(e))



    def info_mod_cognome(self,evento):
        self.btn_modifica_cognome.focus()
        self.archivio_var.set("")
        self.info_var.set("MODIFICA COGNOME -> Inserire la matricola dello studente e il cognome modificato")
        self.funzioni_var.set("mod_cognome")

    def mod_cognome(self, evento):
        try:
            mod_cogn = self.entry.get().split(":")
            matricola =int(mod_cogn[0])
            nuovo_cognome = mod_cogn[1]
            ogg_stud = self.dizionario.studente(matricola)      #con la funzione 'studente' recupero l'oggetto studente se esiste, altrimenti return None e comparirà il messaggio d'errore
            ogg_stud.set_cognome(nuovo_cognome)
            self.archivio_var.set("il cognome dello studente con matricola " + str(matricola) + " è stato modificato correttamente. \n \n Premere 'Visualizza Archivio' per vedere la modifica in archivio")
            self.entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showwarning("errore", "Errore nell'inserimento dei dati o nel trovare la matricola inserita:\n" + str(e))


    def info_mod_nome(self, evento):
        self.btn_modifica_nome.focus()
        self.archivio_var.set("")
        self.info_var.set("MODIFICA NOME -> Inserire la matricola dello studente e il nome modificato")
        self.funzioni_var.set("mod_nome")

    def mod_nome(self, evento):
        try:
            mod_nome = self.entry.get().split(":")
            matricola =int(mod_nome[0])
            nuovo_nome = mod_nome[1]
            ogg_stud = self.dizionario.studente(matricola)          #con la funzione 'studente' recupero l'oggetto studente se esiste, altrimenti return None e comparirà il messaggio d'errore
            ogg_stud.set_nome(nuovo_nome)
            self.archivio_var.set("il nome dello studente con matricola " + str(matricola) + " è stato modificato correttamente. \n \n Premere 'Visualizza Archivio' per vedere la modifica in archivio")
            self.entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showwarning("errore", "Errore nell'inserimento dei dati o nel trovare la matricola inserita:\n" + str(e))


    def info_aggiungi_esame(self,evento):
        self.btn_aggiungi_esame.focus()
        self.archivio_var.set("")
        self.info_var.set("AGGIUNGI ESAME -> Inserire la matricola dello studente, il codice e un voto compreso tra 18 e 33(escluso)")
        self.funzioni_var.set("aggiungi_esame")

    def aggiungi_esame(self, evento):
        try:
            mod_esami =self.entry.get().split(":")
            matricola= int(mod_esami[0])
            codice = (mod_esami[1])
            voto = int(mod_esami[2])
            ogg_stud = self.dizionario.studente(matricola)
            if ogg_stud.registra_esame(codice,voto):        #se la funzione 'registra_esame' non viene eseguita correttamente viene restituito False e quindi mostrato il messaggio di errore che segue 'else:'
                self.archivio_var.set("L'esame con codice " + codice + " è stato inserito correttamente. \n \n Premere 'Visualizza Archivio' per vedere la modifica in archivio")
                self.entry.delete(0, tk.END)
            else:
                messagebox.showwarning("errore", "Errore nella registrazione dell'esame")
        except Exception as e:
            messagebox.showwarning("errore", "Errore nell'inserimento dei dati o nel trovare la matricola: \n" + str(e))


    def info_mod_voto(self,evento):
        self.btn_modifica_voto.focus()
        self.archivio_var.set("")
        self.info_var.set("MODIFICA VOTO -> Inserire la matricola dello studente, il codice dell'esame, e il voto modificato (18<=voto<33)")
        self.funzioni_var.set("mod_voto")

    def mod_voto(self, evento):
        try:
            mod_esami =self.entry.get().split(":")
            matricola= int(mod_esami[0])
            codice = (mod_esami[1])
            voto = int(mod_esami[2])
            ogg_stud = self.dizionario.studente(matricola)
            if ogg_stud.modifica_voto(codice,voto):                 #modifica_voto restituisce True/False
                self.archivio_var.set("Il voto dell'esame con codice " + codice + " è stato modificato correttamente. \n \n Premere 'Visualizza Archivio' per vedere la modifica in archivio" )
                self.entry.delete(0, tk.END)
            else:
                messagebox.showwarning("errore", "Errore nella modifica del voto")
        except Exception as e:
            messagebox.showwarning("errore", "Errore nell'inserimento dei dati o nel trovare la matricola o il codice esame inseriti:\n" + str(e))



    def info_elimina_esame(self,evento):
        self.btn_elimina_esame.focus()
        self.archivio_var.set("")
        self.info_var.set("ELIMINA ESAME -> Inserire la matricola dello studente e il codice esame da eliminare")
        self.funzioni_var.set("elimina_esame")

    def elimina_esame(self, evento):
        try:
            mod_esami =self.entry.get().split(":")
            matricola= int(mod_esami[0])
            codice = mod_esami[1]
            ogg_stud = self.dizionario.studente(matricola)
            if ogg_stud.cancella_esame(codice):                 #cancella_esame restituisce True/False
                self.archivio_var.set("L'esame con codice " + codice + "è stato eliminato correttamente. \n \n Premere 'Visualizza Archivio' per vedere la modifica in archivio")
                self.entry.delete(0, tk.END)
            else:
                messagebox.showwarning("errore", "Errore nell'eliminazione dell'esame")
        except Exception as e:
            messagebox.showwarning("errore", "Errore nell'inserimento dei dati o nel trovare la matricola o il codice esame inseriti:\n" + str(e))


    def info_mod_note(self,evento):
        self.btn_modifica_note.focus()
        self.archivio_var.set("")
        self.info_var.set("MODIFICA NOTE -> Inserire la matricola dello studente e le note modificate")
        self.funzioni_var.set("mod_note")

    def mod_note(self, evento):
        try:
            mod_note =self.entry.get().split(":")
            matricola= int(mod_note[0])
            nuove_note = mod_note[1]
            if self.dizionario.modifica_note(matricola, nuove_note):         #modifica_note restituisce True/False
                self.archivio_var.set("le note dello studente con matricola " + str(matricola) + " sono state modificate correttamente. \n \n Premere 'Visualizza Note Studente' per vedere la modifica")
                self.entry.delete(0, tk.END)
            else:
                messagebox.showwarning("errore", "Errore nella modifica delle note")
        except Exception as e:
            messagebox.showwarning("errore", "Errore nell'inserimento dei dati o nel trovare la matricola inserita:\n" + str(e))


    def info_cancella_stud(self,evento):
        self.btn_cancella.focus()
        self.archivio_var.set("")
        self.info_var.set("CANCELLA STUDENTE -> Inserire la matricola dello studente da eliminare")
        self.funzioni_var.set("cancella_stud")

    def cancella_stud(self, evento):
        try:
            matricola = int(self.entry.get())
            if self.dizionario.elimina(matricola):             #elimina restituisce True/False
                self.archivio_var.set("Lo studente con matricola " + str(matricola) + " è stato eliminato correttamente")
                self.entry.delete(0, tk.END)
            else:
                messagebox.showwarning("errore", "Errore nell'eliminazione dello studente")
        except Exception as e:
            messagebox.showwarning("errore", "Errore nell'inserimento dei dati:\n" + str(e))


    def info_calcola_media(self, evento):
        self.btn_media.focus()
        self.archivio_var.set("")
        self.info_var.set("CALCOLA MEDIA -> Inserire la matricola dello studente di cui si vuole sapere la media degli esami")
        self.funzioni_var.set("calcola_media")

    def calcola_media(self, evento):
        try:
            matricola = int(self.entry.get())
            ogg_stud = self.dizionario.studente(matricola)
            if ogg_stud.media() is not None:       #media restituisce il valore f/None
                media_calcolata = ogg_stud.media()
                self.archivio_var.set(media_calcolata)
                self.entry.delete(0, tk.END)
            else:
                messagebox.showwarning("errore", "Non è possibile calcolare la media")
        except Exception as e:
            messagebox.showwarning("errore", "Errore nell'inserimento dei dati:\n" + str(e))


    def info_carica_arch(self, evento):
        self.btn_carica.focus()
        self.archivio_var.set("")
        self.info_var.set("CARICA ARCHIVIO -> Inserire nel formato nomefile.txt il nome del file da cui si vuole caricare l'archivio")
        self.funzioni_var.set("carica_arch")

    def carica_arch(self, evento):
        nomefile_car = self.entry.get()
        if self.dizionario.carica(nomefile_car):       #carica restituisce True/False
            self.archivio_var.set("L'archivio è stato caricato correttamente. \n \n Premere 'Visualizza Archivio' per vedere la modifica in archivio")
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("errore", "File non trovato oppure errore nel caricamento dei dati")


    def info_salva_arch(self, evento):
        self.btn_salva.focus()
        self.archivio_var.set("")
        self.info_var.set("SALVA ARCHIVIO -> Inserire nel formato nomefile.txt il nome del file su cui si vuole salvare l'archivio")
        self.funzioni_var.set("salva_arch")

    def salva_arch(self, evento):
        nomefile_salva = self.entry.get()
        if self.dizionario.salva(nomefile_salva):   #elimina restituisce True/False
            self.archivio_var.set("l'archivio è stato salvato correttamente.")
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("errore", "Errore nel salvataggio dei dati")


    def esci(self, evento):
        self.btn_esci.focus()
        risposta = messagebox.askquestion("ESCI", "Uscire dal programma?")
        if risposta == "yes":
            w.destroy()



w = tk.Tk()
myApp(w)
w.mainloop()
