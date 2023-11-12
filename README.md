# ue19_labo09-10


## Descripion du projet : 

--> Fichier python (app.py) qui fait appel à une API pour connaître l'adresse IP public                                  
--> fichier Docker (Dockerfile) pour conteneuriser le fichier python

## Comment installer et exécuter le projet

Posséder Docker sur son appareil sinon l'installer, voici le site officiel pour trouver l'instal par rapport à votre système d'exploitation : https://www.docker.com/                                                  
Il suffit d'exécuter le fichier et de redémarrer sa machine.

## Installer le projet :

1. Télécharger le fichier app.py et Dockerfile
2. Créer un dossier et y insérer les fichiers
3. Lancer le cmd ou temrinal (dépend de votre système d'exploitation)
4. Accéder au répertoire se trouvant le fichier app.py et DockerFile
5. Taper la commande suivante pour créer un conteners :                                     
   docker build -t "Le nom que vous souhaiter mettre" .
6. Patienter et c'est bon !

## Utiliser le projet :

Ouvrir un terminal ou CMD et exécuter la commande suivante :                  
  docker run "Le nom que vous lui avez donnée"                                                          
