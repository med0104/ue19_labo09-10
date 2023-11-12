# ue19_labo09-10


## Descripion du projet : 

--> Fichier python (app.py) qui fait appelle à une API pour connaitre l'adresse IP public                                  
--> fichier Docker (Dockerfile) pour conteneuriser le fichier python

## Comment installer et exécuter le projet

Posséder Docker sur son appareil sinon l'installer, voici le site officiel pour trouver l'install par rapport à votre système d'exploitation : https://www.docker.com/
Il suffit d'executer le fichier et de redémarrer sa machine.

## Installer le projet :

1. Télecharger le fichier app.py et Dockerfile
2. Créer un dossier et y insérez les fichiers
3. Lancer le cmd ou temrinal (dépend de votre système d'exploitation)
4. Accéder au répertoire se trouvant le fichier app.py et DockerFile
5. Taper la commande suivante pour créer un conteners :                                     
   docker build -t "Le nom que vous souhaiter mettre" .

   Exemple :
   ![image](https://github.com/med0104/ue19_labo09-10/assets/150246758/4fe7c39b-498d-49ff-8615-72ee75e2499d)

7. Patienter et c'est bon !

## Utiliser le projet :

Ouvrir un temrinal ou CMd et exécuter la commande suivante :                  
  docker run "Le nom que vous lui avez donner"                                                          
  Exemple :
  ![image](https://github.com/med0104/ue19_labo09-10/assets/150246758/cd1ade86-73eb-460b-b6f5-25d3042ece69)
