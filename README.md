## Installation du projet

Toutes les commandes ci-dessous sont à éxecuter à la racine du projet

1. Récupérer les dépendences avec yarn ou npm
```
npm install
```
OU
```
yarn
```

2. Compiler les assets avec webpack
```
npm run watch
```
OU
```
yarn watch
```

3. Lancer l'environnement docker du projet
```
docker-compose up -d --build
```

Les éléments suivants sont alors gérés :
- application django -> [http://localhost:8000](http://localhost:8000)
- adminer pour visualiser les informations de la BDD -> [http://localhost:8080](http://localhost:8080)
- base de donnée postgres -> port **5432** (interne au réseau docker, **non bindé vers l'extérieur**)

Pour se connecter à Adminer, utiliser les identifiants suivants :
- Système : **PostgreSQL**
- Serveur : **postgres_django**
- Utilisateur : **app_hs**
- Mot de passe : **root**
- Base de données : **app_hs**

4. Couper l'environnement docker
```
docker-compose down
```

