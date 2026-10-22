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
    def __init__(self) -> None:
        self.tete =None


#teste des morceaux
m1 = Morceau("Imagine", "John Lennon", 183)
m2 = Morceau("Billie Jean", "Michael Jackson", 294)
m3 = Morceau("Hey Jude", "The Beatles", 431)
m4 = Morceau("One", "U2", 276)
m5 = Morceau("Smells Like Teen Spirit", "Nirvana", 301)
#création d'une liste chainé à partir de la class:Noeud
n1=Noeud(m1,Noeud(m2,Noeud(m3)))
#création d'une playlist
playlist = Playlist()
