#Créer par Kyrian Payen
class Morceau:
    #Constructeur
    def __init__(self,t:str, a:str, d:int)-> None:
        self.titre = t
        self.artiste = a
        self.duree = d

class Noeud:
    #Constructeur
    def __init__(self,morceau:object , suivant=None) -> None:
        self.morceau = morceau
        self.suivant = suivant

class Playlist:
    #Constructeur
    def __init__(self) -> None:
        self.tete = None

    def ajouter_debut(self,morceau:Morceau)->None:
        """Ajoute un morceau au début de la playlist"""
        assert isinstance(morceau,Morceau)

        #Creer un nouveau maillon le met en première position et place les autres au niveau de la queue
        self.tete = Noeud(morceau,self.tete)

    def afficher(self):
        """Affiche les morceaux qui sont dans la playlist"""
        affiche = ""#Création d'une varible permettan l'affichage
        m = self.tete#Permet le parcourt de la playlist
        i = 1#Défini le numéro de la musique dans la playlist

        while m != None:
            #Incrémente dans affiche le numéro du morceau , le tire,l'artiste,la duree
            affiche += f"\n {i}. {m.morceau.titre} - {m.morceau.artiste} - {m.morceau.duree} sec"
            i += 1#Augmente de 1 le numéro du morceau pour la prochaine boucle

            m = m.suivant#Passage au morceau suivant

        #Renvoie l'affichage de la playlist sous forme de chaine de caractère
        return affiche

    def ajouter_fin(self,morceau:Morceau):
        """Ajoute un morceau à la fin de la playlist"""
        assert isinstance(morceau, Morceau)

        #Création du noeud du morceau qui sera à la fin
        nouveau = Noeud(morceau)

        #Vérifie si la playlist n'est pas vide.
        if self.tete is None:
            self.tete = nouveau

        #La playlist n'est pas vide alors on commence à la tete
        m = self.tete

        #On avance dans la playlist jusqu'a temps qu'il n'y est plus de morceau après
        while m.suivant is not None:
            #Passage au noeud suivant
            m = m.suivant

        #On arrive au dernier noeud et on remplace le suivant qui None  par le morceau que l'on souhaite ajouter
        m.suivant = nouveau





#Création de morceau
m1 = Morceau("Imagine", "John Lennon", 183)
m2 = Morceau("Billie Jean", "Michael Jackson", 294)
m3 = Morceau("Hey Jude", "The Beatles", 431)
m4 = Morceau("One", "U2", 276)
m5 = Morceau("Smells Like Teen Spirit", "Nirvana", 301)

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
