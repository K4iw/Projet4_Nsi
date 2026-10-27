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
        affiche = ""
        #Initialisation d'une variable pour permettre le parcourt
        n = self.tete
        #Défini le numéro de la musique dans la playlist
        i = 1
        while n != None:
            #Incrémente dans affiche le numéro du morceau , le tire,l'artiste,la duree
            affiche += f"\n {i}. {n.morceau.titre} - {n.morceau.artiste} - {n.morceau.duree} sec"
            #Augmente de 1 le numéro du morceau pour la prochaine boucle
            i += 1
            #Passage au morceau suivant
            n = n.suivant
        #Renvoie le l'affichage de la playlist sous forme de chaine de caractère
        return affiche

    def ajouter_fin(self,morceau:Morceau):
        """Ajoute un morceau à la fin de la playlist"""
        assert isinstance(morceau,Morceau)
        #Création d'une liste vide qui contientra les morceaux de la playlist
        liste_morceaux = []
        n = self.tete
        while n != None :
            #On ajoute un morceau à la playlist
            liste_morceaux.append(n.morceau)
            #On passe au morceau suivant
            n = n.suivant
        #On ajoute le morceau que l'on souhaite mettre  à la fin
        # à la liste qui contient les morceaux
        liste_morceaux.append(morceau)
        #On remet la playlist à zéro
        self.tete = None
        #On parcourt la liste de morceau et on est les ajoute à la playlist
        for i in range(len(liste_morceaux)):
            #On ajoute les morceaux à la playlist en partant de la fin de la liste
            #La logique peut etre plus simple si reversed() autorisé à demander au prof
            self.ajouter_debut(liste_morceaux[len(liste_morceaux)-i-1])










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
playlist.ajouter_debut(m4)
playlist.ajouter_debut(m3)
playlist.ajouter_debut(m2)
playlist.ajouter_debut(m1)
print(playlist.afficher())
playlist.ajouter_fin(m5)
print(playlist.afficher())#Vérification




#Façon plus simple de faire
# def ajouter_fin(self, morceau):
    #assert isinstance(morceau, Morceau)

    # 1. On crée le nouveau wagon (le nœud) qui contient ton morceau.
    # Comme c'est le dernier, sa flèche "suivant" pointe vers None (rien).
    #nouveau = Noeud(morceau)

    # 2. Cas particulier : si la playlist est totalement vide,
    # le nouveau morceau devient simplement le premier (la tête).
    #if self.tete is None:
        #self.tete = nouveau
        #return

    # 3. Si la playlist n'est pas vide, on commence à la tête...
    #n = self.tete

    # 4. ...et on avance TANT QUE le wagon actuel a un wagon suivant.
    # Dès que n.suivant vaut None, la boucle s'arrête. On est sur le DERNIER wagon.
    #while n.suivant is not None:
        #n = n.suivant

    # 5. Maintenant qu'on est sur le dernier wagon, on remplace son "suivant"
    # (qui était vide) par notre nouveau wagon.
    #n.suivant = nouveau
