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
      if nom:	      # Accueil de l'utilisateur :
        return "Bonjour, {}, comment allez-vous ?".format(nom)
      else:	    # Aucun nom n'a été fourni :
        return 'Veuillez svp fournir votre nom <a href="/">ici</a>.'
  salutations.exposed = True
 
cherrypy.quickstart(Bienvenue(), config ="tutoriel.conf")