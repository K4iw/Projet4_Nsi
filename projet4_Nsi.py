#Créer par Kyrian Payen


class Morceau:
    #Constructeur
    def __init__(self,t:str, a:str, d:int):
        self.titre = t
        self.artiste = a
        self.duree = d

class Noeud:
    #Constructeur
    def __init__(self,morceau:Morceau , suivant=None):
        self.morceau = morceau
        self.suivant = suivant

class Playlist:
    #Constructeur
    def __init__(self) :
        self.tete = None

    def ajouter_debut(self,morceau:Morceau)-> None:
        """Ajoute un morceau au début de la playlist"""
        assert isinstance(morceau,Morceau)

        #Creer un nouveau maillon le met en première position et place les autres au niveau de la queue
        self.tete = Noeud(morceau,self.tete)

    def afficher(self)->str:
        """Affiche les morceaux qui sont dans la playlist"""
        affichage = ""#Création d'une varible permettan l'affichage
        m = self.tete#Permet le parcourt de la playlist
        i = 1#Défini le numéro de la musique dans la playlist

        while m != None:
            #Incrémente dans affiche le numéro du morceau , le tire,l'artiste,la duree
            affichage += f"\n {i}. {m.morceau.titre} - {m.morceau.artiste} - {m.morceau.duree} sec"
            i += 1#Augmente de 1 le numéro du morceau pour la prochaine boucle

            m = m.suivant#Passage au morceau suivant

        #Renvoie l'affichage de la playlist sous forme de chaine de caractère
        return affichage

    def ajouter_fin(self,morceau:Morceau)-> None:
        """Ajoute un morceau à la fin de la playlist"""
        assert isinstance(morceau, Morceau)

        #Création du noeud du morceau qui sera à la fin
        nouveau = Noeud(morceau)

        #Vérifie si la playlist n'est pas vide.
        if self.tete is None:
            self.tete = nouveau
        else:
            m = self.tete
            #On avance dans la playlist jusqu'a temps qu'il n'y est plus de morceau après
            while m.suivant is not None:
                #Passage au noeud suivant
                m = m.suivant

            #On arrive au dernier noeud et on remplace le suivant qui est None  par le morceau que l'on souhaite ajouter
            m.suivant = nouveau

    def rechercher(self,titre:str) -> Noeud | None :
        """Cherche un morceau à partir de son titre"""
        assert isinstance(titre,str)

        #n est initialisé pour permettre le parcourt de la playlist
        n = self.tete
        #noeud est le Noeud qui sera renvoyé à la fin du script
        noeud = None

        while n  is not  None :
            if n.morceau.titre == titre :
                #Assigne à la variable(noeud) le noeud ou le morceau se trouve
                noeud = n
                #Retourne le noeud
                return noeud
            #Passage au noeud suivant
            n = n.suivant

        #Retourne le noeud , vide si le morceau avec le titre n'a pas été trouvé
        return noeud

    def supprimer(self,titre:str)-> None:
        """Supprime le premier morceau correspondant au titre dans la playlist"""
        assert isinstance(titre,str)

        # Recherche le Noeud ou le morceau se trouve
        n = self.rechercher(titre)
        # Permet le parcourt de la playlist
        supprime = self.tete

        #Prévois le cas ou le morceau est absent
        if n is None:
            print("Le morceau choisi n'existe pas dans la playlist ")

        else:
            # Vérifie si le premier morceau de la playlist est  celui que l'on cherche à supprimer
            if supprime == n:
                self.tete = self.tete.suivant

            else:
                # Termine la boucle quand le noeud suivant et le noeud à supprimer
                while supprime.suivant != n:
                    #Passage au noeud suivant
                    supprime = supprime.suivant
                #Change le noeud suivant , en prenant celui qui vient  après le noeud suivant (on passe le noeud que l'on veut supprimer)
                supprime.suivant =supprime.suivant.suivant



    def inserer(self,morceau :Morceau,position:int):
        """Insére un morceau à une position donné , on compte à partir de 0"""
        assert isinstance(morceau,Morceau)
        assert isinstance(position,int)

        # Initialisation de variables
        actuelle = 0
        parcourt = self.tete
        # Prise en compte de la position 0
        if position == 0:
            self.tete = Noeud(morceau ,self.tete)

        else :
            #Prends en compte si la liste est vide
            if self.tete == None:
                print("Position choisi out of range et la playlist vide")

            else :
                # Vérifie si la position suivante sera la position souhaité
                while actuelle != position -1 :
                    # Ajout de 1 à la position actuelle
                    actuelle += 1
                    # Vérifie si le parcourt n'arrive pas en dehors la playlist
                    if parcourt.suivant==None and actuelle != position -1:
                        # Indication à l'utilisateur que sa demande n'est pas possible
                        print("Position choisi out of range ")
                        # Arrete la méthode
                        return
                    # Passage au Noeud suivant
                    parcourt = parcourt.suivant
                # Insérer le morceau désiré à la position souhaité en créant un nouveau noeud
                parcourt.suivant = Noeud(morceau,parcourt.suivant)


    def compter(self) -> int:
        """Compte le nombre de morceaux présent dans la playlist"""
        # Initialisation de variable
        compte =0
        parcourt =self.tete
        # Parcourt la playlist
        while parcourt != None:
            # Incrémentation de compte
            compte += 1
            # Passage au morceau suivant
            parcourt = parcourt.suivant
        # Retourne le nombre de morceau présent dans la playlist
        return compte

    def duree_total(self) ->int:
        """ retourne la durée totale de la playlist en secondes"""
        # Initialisaion de variable
        duree_total = 0
        parcourt = self.tete

        while parcourt !=None:
            # Ajout de la duree d'un morceau
            duree_total += parcourt.morceau.duree
            # Passage au morceau suivant
            parcourt = parcourt.suivant
        # Retourne la duree_total de la playlist en seconde
        return duree_total

    def afficher_duree_total(self):
        """Affiche la duree totale dans la console"""

        duree_total =self.duree_total()
        affiche ="Durée totale : "

        # Conversion en heures,miutes,secondes
        heures = duree_total//3600
        minutes = duree_total//60 - heures * 60
        secondes = duree_total - minutes*60 - heures*3600
        # Ajout  des heures , des minutes et des secondes à affiche
        if heures>0:
            affiche += str(heures) +" heures "
        if minutes>0:
            affiche += str(minutes) + " minutes "
        if secondes>=0:
            affiche += str(secondes) + " secondes"
        print(affiche)














#Création de morceau
m1 = Morceau("Imagine", "John Lennon", 183)
m2 = Morceau("Billie Jean", "Michael Jackson", 294)
m3 = Morceau("Hey Jude", "The Beatles", 431)
m4 = Morceau("One", "U2", 276)
m5 = Morceau("Smells Like Teen Spirit", "Nirvana", 301)
m6 = Morceau("Test","Kyrian",60)

#Création d'une liste chainé à partir de la class:Noeud
n1=Noeud(m1,Noeud(m2,Noeud(m3)))

#Création d'une playlist
playlist = Playlist()
#Ajout des morceaux à la playlist
playlist.ajouter_debut(m4)
playlist.ajouter_debut(m3)
playlist.ajouter_debut(m2)
playlist.ajouter_debut(m1)
#Affichage des morceaux present dans la playlist
print(playlist.afficher())

playlist.ajouter_fin(m5)
#Vérification du fonctionnement de la méthode ajouter_fin
print(playlist.afficher())
#Vérification du bon fonctionnement de la méthode rechercher
n = playlist.rechercher("Imagine")
if n is not None:
    print(n.morceau.artiste)
#Test des méthodes
playlist.supprimer("Smells Like Teen Spirit")
print(playlist.afficher())
playlist.inserer(m6,0)
print(playlist.afficher())
print(playlist.compter())
print(playlist.duree_total())
playlist.afficher_duree_total()
