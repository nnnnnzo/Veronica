import sqlite3
conn = sqlite3.connect('livres.db')

c = conn.cursor()

protocol = ["SELECT titre FROM livre",
            "SELECT nom FROM usager",
            "SELECT DISTINCT nom FROM usager",
            "SELECT titre FROM livre WHERE annee < 1980",
            "SELECT titre FROM livre WHERE titre LIKE '%A%'",
            "SELECT isbn FROM emprunt WHERE retour = '2020-01-01'",
            "SELECT nom FROM auteur ORDER BY nom",
            "SELECT nom FROM usager WHERE cp = '75012' OR cp = '75013'",
            "SELECT nom, adresse FROM usager WHERE adresse NOT LIKE '%Rue%'",
            "SELECT titre FROM livre INNER JOIN emprunt ON livre.isbn = emprunt.isbn",
            "SELECT titre FROM livre INNER JOIN emprunt ON livre.isbn = emprunt.isbn AND emprunt.retour < '2020-03-31'",
            "SELECT DISTINCT nom, prenom FROM usager INNER JOIN emprunt ON usager.code_barre = emprunt.code_barre ORDER BY nom",
            "SELECT titre FROM livre WHERE annee < ( SELECT titre FROM livre WHERE titre = 'Dune')",
            "SELECT COUNT(titre) FROM livre WHERE annee < ( SELECT titre FROM livre WHERE titre = 'Dune') "]

se = ["Tous les titres de livres:",
      "Tous les noms d'usager:",
      "Tous les noms d'usager enretirant les doublons:",
      "Les titres des livres publiés avant 1980:",
      "Les titres des livres dont le titre contient la lettre 'A':",
      "Les ISBN des livres à rendre pour le 01/01/2020:",
      "Les noms d'auteurs triés par ordre alphabétique:",
      "Le noms d'usagers vivant dans le 12eme et le 13eme arrondissement de Paris (codes postaux 75012 et 75013):",
      "Les noms et adresses des usagers n'habitant pas dans une rue (la chaîne 'Rue' ne doit pas apparaître dans l'adresse):",
      "Le titre des livres empruntés:",
      "Le titre des livres empruntés à rendre avant le 31/03/2020:",
      "Le nom et le prénom des usagers ayant emprunté des livres sans doublons et par ordre alphbétique:",
      "Les titres des livres publiés strictement avant 'Dune':",
      "Le nombre des résultats trouvés à la question précédente:"]

def Veronica(protocol, se):
    print(" ____       _    __                      _            ")
    print(" \ \ \     | |  / /__  _________  ____  (_)________ _ ")
    print("  \ \ \    | | / / _ \/ ___/ __ \/ __ \/ / ___/ __ `/ ")
    print("  / / /    | |/ /  __/ /  / /_/ / / / / / /__/ /_/ /  ")
    print(" /_/_/     |___/\___/_/   \____/_/ /_/_/\___/\__,_/   ")
    print()
    i = 0
    for e in protocol :
        print(se[i])
        i += 1
        J = c.execute(e)
        print("|REQUETE| ", e)
        print("|RESULTAT| ",c.fetchall())
        print()
        print()
Veronica(protocol, se)