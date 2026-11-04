#Créer par Kyrian Payen


class Morceau:
    def __init__(self,t:str, a:str, d:int):
        self.titre = t
        self.artiste = a
        self.duree = d

class Noeud:
    def __init__(self,morceau:Morceau , suivant=None):
        self.morceau = morceau
        self.suivant = suivant

class Playlist:
    def __init__(self) :
        self.tete = None

    def ajouter_debut(self,morceau:Morceau) :
        """Ajoute un morceau au début de la playlist"""
        assert isinstance(morceau,Morceau)

        #Creer un nouveau maillon le met en première position et place les autres au niveau de la queue
        self.tete = Noeud(morceau,self.tete)

    def afficher(self):
        """Affiche les morceaux qui sont dans la playlist"""
        #Initialisation des variables
        affichage = ""#Création d'une varible permettan l'affichage
        m = self.tete#Permet le parcourt de la playlist
        i = 1#Défini le numéro de la musique dans la playlist

        while m != None:
            #Incrémente dans affiche le numéro du morceau , le tire,l'artiste,la duree
            affichage += f"\n {i}. {m.morceau.titre} - {m.morceau.artiste} - {m.morceau.duree} sec"
            i += 1#Augmente de 1 le numéro du morceau pour la prochaine boucle

            m = m.suivant#Passage au morceau suivant

        #Renvoie l'affichage de la playlist sous forme de chaine de caractère
        print(affichage)

    def ajouter_fin(self,morceau:Morceau) :
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

    def rechercher(self,titre:str) :
        """Cherche un morceau à partir de son titre"""
        assert isinstance(titre,str)

        #n est initialisé pour permettre le parcourt de la playlist
        n = self.tete

        while n  is not  None :
            if n.morceau.titre == titre :
                return n
            #Passage au noeud suivant
            n = n.suivant

        return None

    def supprimer(self,titre:str):
        """Supprime le premier morceau correspondant au titre dans la playlist"""
        assert isinstance(titre,str)

        # Recherche le Noeud ou le morceau se trouve
        n = self.rechercher(titre)


        #Prévois le cas ou le morceau est absent
        if n is None:
            print("Le morceau choisi n'existe pas dans la playlist ")

        # Vérifie si le premier morceau de la playlist est  celui que l'on cherche à supprimer
        elif self.tete == n:
            self.tete = self.tete.suivant


        else:
            supprime = self.tete
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

        # Prise en compte de la position 0
        if position == 0:
            self.tete = Noeud(morceau ,self.tete)
        #Prise en compte de la playlist vide
        elif self.tete is None:
            print("Position choisi out of range car playlist vide,unique position valide 0")

        else:
            #Initialisation des variables
            actuelle = 0
            parcourt = self.tete
            #Permet d'arreter la boucle
            insertion_possible = True

            #Parcourt de la playlist
            while actuelle < position - 1 and insertion_possible:
                #Incrémentation de la position actuelle
                actuelle += 1
                #Vérification de si la position choisi n'est pas out of range
                if actuelle < position -1 and parcourt.suivant is None:
                    print("position choisi out of range")
                    insertion_possible = False
                else:
                    #Passage au morceau suivant
                    parcourt = parcourt.suivant
            #Permet de vérifier si l'insertion est possible
            if insertion_possible:
                #On change le maillon  suivant par le morceau que l'on veut inserer
                parcourt.suivant = Noeud(morceau,parcourt.suivant)


    def compter(self) -> int:
        """Compte le nombre de morceaux présent dans la playlist"""
        # Initialisation des variables
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
        # Initialisaion des variables
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
playlist.afficher()

playlist.ajouter_fin(m5)
#Vérification du fonctionnement de la méthode ajouter_fin
playlist.afficher()
#Vérification du bon fonctionnement de la méthode rechercher
n = playlist.rechercher("Imagine")
if n is not None:
    print(n.morceau.artiste)
#Test des méthodes
playlist.supprimer("Smells Like Teen Spirit")
playlist.afficher()
playlist.inserer(m6,0)
playlist.afficher()
print(playlist.compter())
print(playlist.duree_total())
playlist.afficher_duree_total()
