# koesio-job-interview

Sujet du Test : Création d'une API REST et FRONTEND

 

Il conviendra de poser les bases : 

- Définition des endpoints

- Modélisation de la base de données

- Structure du projet avec la gestion complète d'au moins deux ressources (relations)

- Des indications pour la suite (intégration des autres ressources, projet d'implémentation d'une API externe)

- Gestion du code source sur votre compte Github (c'est vraiment important : je retiendrais vers vous avec les informations)


Contexte : Vous travaillez pour une entreprise de gestion de bibliothèques. Votre tâche consiste à développer une API REST pour gérer les ressources de la bibliothèque, notamment les livres, les auteurs et les emprunts. De plus, l'entreprise souhaite intégrer un service externe qui fournit des informations sur les livres à l'aide d'une API tierce. L'API doit être exploitable via un Frontend utilisateur simple. 


Fonctionnalités à Implémenter :


1. Gestion des Livres :

- Création, lecture, mise à jour et suppression de livres.

- Récupération de la liste des livres disponibles.

- Recherche de livres par titre, auteur ou genre.


2. Gestion des Auteurs :

- Création, lecture, mise à jour et suppression d'auteurs.

- Récupération de la liste des auteurs.

- Récupération des livres écrits par un auteur donné.


3. Gestion des Emprunts :

- Création et retour d'emprunts.

- Récupération de la liste des emprunts en cours.

- Recherche des emprunts par utilisateur ou par livre.


4. Intégration avec une API Externe :

- Intégration avec une API tierce (par exemple, Google Books API) pour obtenir des informations supplémentaires sur un livre lors de sa création ou de sa mise à jour : les données ainsi récupérées seront stockées dans la DB.

- Une indisponibilité de l'API, ou la non-présence de l'ouvrage/auteur ne doivent pas être bloquantes pour l'enregistrement des données saisies par l'utilisateur.
Prévoir en revanche une tâche de maintenance automatique qui vient récupérer les informations manquantes en cas d'erreur.


Exigences Techniques :

- Utilisation d'un framework de votre choix (par exemple, Django, FastAPI, Flask ou autre).

- Stockage des données dans une base de données (SQL ou NoSQL, selon votre préférence).

- Utilisation de tests unitaires pour garantir la fiabilité des endpoints.

- Frontent simple au choix (généré par le framework Python ou utiliser un framework js)

- Présentation du projet fonctionnel en local ou hébergé 



Critères d'Évaluation : Le candidat sera évalué en fonction de sa capacité à :

- Concevoir une API REST avec des endpoints clairement définis : documentation des endpoints (Doc en ligne ou fichier)

- Mettre en œuvre des opérations CRUD (Create, Read, Update, Delete) pour les entités.

- Gérer les relations entre les entités (livres, auteurs, emprunts).

- Intégrer une API externe.

- Assurer une gestion efficace des erreurs et une validation des données.

- Consommer l'API via un Frontend basique 
