# Comment installer et paramétrer l'application ?

1. Cloner ce repo
2. Initialiser les variables d'environnement. Les variables d'environnement sont stockées dans config/. Les variables pour la base de données dans database.env doivent correspondre à celles de docker-compose.env.
   2.1 La base de donnée utilisée est MariaDB, qui sera souvent notée "MySQL" en raison des librairies partagées. (MariaDB est originellement MySQL avant l'acquisition de ce dernier par Oracle, ça n'est que la branche communautaire qui est maintenue)
3. Initialiser les containeurs : docker-compose up -d

# Dépendances librairies

2. Django v4.23+
3. Django-environ
4. Django-tailwindCSS
5. mysqlclient 1.4.3+ (DB Api Drivers for MariaDB/MySQL)
6. Connector/Python 8.0.33+ (ORM : Mapping for MariaDB/MySQL (Relational Database) -> Django Models (Objects))
   Note : Connector/Python === oracle = bad :(

# Dépendances globales

1. Python v3.8+
2. Docker, docker-compose

Il est recommandé d'utiliser un environnement virtuel (venv)
