import cherrypy
 
class Bienvenue(object):
    def index(self):
    # Formulaire demandant son nom à l'utilisateur :
        return '''
        <form action="salutations" method="GET">
        Bonjour. Quel est votre nom ?
        <input type="text" name="nom" />
        <input type="submit" value="OK" />
        </form>
        '''
    index.exposed = True
 
    def salutations(self, nom =None):
            # Exemple simplissime : incrémentation d'un compteur d'accès.
    # On commence par récupérer le total actuel du comptage :
        count = cherrypy.session.get('count', 0)
    # ... on l'incrémente :
        count += 1
    # ... on mémorise sa nouvelle valeur dans le dictionnaire de session :
        cherrypy.session['count'] = count
    # ... et on affiche le compte actuel :

        if nom:	      # Accueil de l'utilisateur :
            #return "Bonjour, {}, comment allez-vous ?".format(nom)
            return "Durant la présente session, vous avez déjà visité cette page {} fois ! Votre vie est bien excitante !".format(count)
        else:	    # Aucun nom n'a été fourni :
            return 'Veuillez svp fournir votre nom <a href="/">ici</a>.'
    salutations.exposed = True
 
cherrypy.quickstart(Bienvenue(), config ="tutoriel.conf")
