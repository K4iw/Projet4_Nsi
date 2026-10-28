#Créer par Kyrian Payen


class Morceau:
    #Constructeur
    def __init__(self,t:str, a:str, d:int):
        self.titre = t
        self.artiste = a
        self.duree = d

class Noeud:
    #Constructeur
    def __init__(self,morceau:object , suivant=None):
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
            return

        #La playlist n'est pas vide alors on commence à la tete
        m = self.tete

        #On avance dans la playlist jusqu'a temps qu'il n'y est plus de morceau après
        while m.suivant is not None:
            #Passage au noeud suivant
            m = m.suivant

        #On arrive au dernier noeud et on remplace le suivant qui None  par le morceau que l'on souhaite ajouter
        m.suivant = nouveau

    def rechercher(self,titre:str) -> Noeud | None :
        """Cherche un morceau à partir de son titre"""
        assert isinstance(titre,str)
        #n est initialisé pour permettre le parcourt de la playlist
        n = self.tete
        #noeud est le Noeud qui sera renvoyé à la fin du script
        noeud = None
        #trouve permet d'arreté la boucle si le morceau à été trouvé
        trouve = False

        while n  is not  None and  trouve is not(True) :
            if n.morceau.titre == titre :
                #Permet d'arreter la boucle
                trouve = True
                #Assigne à la variable(noeud) le noeud ou le morceau se trouve
                noeud = n
            #Passage au noeud suivant
            n = n.suivant
        #Retourne le noeud , vide si le morceau avec le titre n'a pas été trouvé
        return noeud







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
#Vérification du bon fonctionnement de la méthode rechercher
n = playlist.rechercher("Imagine")
if n is not None:
    print(n.morceau.artiste)
m = playlist.rechercher("Je sais pas")
if m is not None:
    print(m.morceau.artiste)
