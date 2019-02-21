# Projet vue-CLI-3, Postgre, Django Dockerizer

## 1°) Les branches git

``` 
 __  dev -> pour le developement
|
|__ test -> faires les test + préprod
|
|__ prod -> production 
|
|__ master -> init
```
/!\ mettez vous directement sur la branche dev
## 2°) Architecture du projet

```
_/ourflow
|   /api -> c'est dans ce dossier que la communication entre l'application et la base données se feront
|   /client -> c'est dans ce dossier que la page client (votre site) va être développé et compilé pour la production
|   /global -> dans ce dossier nous avons les parametres global de notre application avec les routes
|
_/Docker
|   /client -> c'est dans ce dossier ce trouve le dockerfile du build de l'image de node et que je créé mon image pour vue
|   /db/pgsql -10 -> dans ce dossier nous retrouvons le dockerfile du build de l'image de pgsql avec un shell script qui s'execute dans l'image
|   /django -> dans ce dossier nous avons un fichier.txt qui est un fichier de gestionnaire de paquet ainsi que le dockerfile pour l'image
```

/!\ toutes les commandes utilisant docker-compose doivent se vaire dans le repertoire/dossier Docker/
## 3°) Avant de build

### a) rendez-vous dans le dossier app/client/ et chercher le fichier .env.staging
une fois le fichier ouvert vous devriez avoir ça: 
```
# <--- config for dev server--->
VUE_APP_BASE_API = null -> base url de votre api django
HOST = 0.0.0.0 -> le serveur par lequel docker lance vos app
PORT = 8080
VUE_APP_DEBUG=true -> pour le debug dans le terminal
```

Une fois les modifications faites aller dans les .gitignore et decommenter la ligne suivante:
``` 
### node/vue ###
*.DS_Store
node_modules/
dist/
.env.development
# .env.staging -> à décommenter une fois le projet clone
```
/!\ si vous faites tourner docker dans une VM linux modifier la variable d'environnement API_BASE_URL par l'IP que docker vous donne par défaut

### b) Ouvrez le dossier docker-compose.yml dans le dossier Docker ainsi que settings.py dans le dossier app/global
ce qui va nous interessé dans le fichier:

- docker-compose.yml:
```
    environment:
      POSTGRES_PASSWORD: admin -> modifier à votre convenance
      POSTGRES_USER: admin -> modifier à votre convenance
      POSTGRES_DB: test -> modifier à votre convenance 
```

- settings.py:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test', -> modifier en fonction de docker-compose.yml 
        'USER': 'admin', -> modifier en fonction de docker-compose.yml
        'PASSWORD': 'admin', -> modifier en fonction de docker-compose.yml
        'HOST': 'db', -> correspond à 0.0.0.0 (voir depends_on dans le docker-compose.yml)  
        'PORT': '5432', -> port de pgsql
    }
}
```

### c) si vous avez déja lanceé un build utilisants les ports: 8080/8000/5432
lancez les commandes suivantes:
```
- dos2unix db/pgsql-10/docker-entrypoint.sh -> encode le fichier docker-entrypoint.sh
- docker rmi $(docker images -a) -> supprime toutes les images
- docker rm $(docker ps -a -q) -> supprime les container
```
flemme de faire un "alias" des ports

## 4°) Le build
Aller dans le répertoire /Docker et ouvrez le shell
lancez la commande suivante:
```
- docker-compose build
```
vous allez en avoir pour un moment.

### En cas d'erreur
lancez les commandes suivantes:
```
- dos2unix db/pgsql-10/docker-entrypoint.sh -> encode le fichier docker-entrypoint.sh
- docker rmi $(docker images -a) -> supprime toutes les images
- docker rm $(docker ps -a -q) -> supprime les container
- docker-compose build --no-cache -> relacer le build avec cette commandes pour éviter que l'erreur perciste en cas de résolution
```

si l'erreur perciste venez vers moi.

## 5°) Lancer les serveurs
une fois le build des images docker terminé sans erreur faites:
``` 
docker-compose up
``` 

en cas d'erreur n'hésiter pas à relancer la commande si l'erreur persiste venez vers moi ou aller sur internet. 

## 6°) Finish
une fois que tout est bien lancé sans erreur aller sur:
- http://0.0.0.0:8080
- http://0.0.0.0:8000 -> une erreur va apparaitre c'est normale

## 7°) Learn 
Pour apprendre le fonctionnement de :

- django : https://www.djangoproject.com/start/
- vue: https://vuejs.org/ && https://fr.vuejs.org/v2/guide/instance.html -> 2eme liens très important
- docker: https://docs.docker.com/v17.09/engine/userguide/storagedriver/imagesandcontainers/
