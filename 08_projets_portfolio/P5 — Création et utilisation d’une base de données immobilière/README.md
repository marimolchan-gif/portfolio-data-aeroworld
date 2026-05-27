# P5 — Création et utilisation d’une base de données immobilière

## Synthèse exécutive

Ce projet consiste à concevoir, créer et exploiter une base de données immobilière structurée à partir de plusieurs fichiers sources.

L’objectif est de transformer des données brutes et hétérogènes en une base relationnelle normalisée, documentée et exploitable pour des analyses SQL.

Ce projet démontre ma capacité à structurer un socle de données fiable, à appliquer des principes de modélisation relationnelle, à documenter les règles de gestion et à prendre en compte les enjeux de qualité, de confidentialité et de conformité RGPD.

---

## Contexte métier

Dans le secteur immobilier, les données proviennent souvent de sources multiples : transactions foncières, informations géographiques, référentiels communaux et caractéristiques des biens.

Pour être exploitables, ces données doivent être :

- structurées ;
- nettoyées ;
- normalisées ;
- documentées ;
- reliées par des clés cohérentes ;
- conformes aux exigences de confidentialité.

Le projet s’inscrit dans une logique de création d’un référentiel immobilier fiable, permettant d’interroger les données de manière claire et reproductible.

---

## Objectifs du projet

Les objectifs principaux sont les suivants :

- comprendre les données initiales ;
- identifier les données sensibles ;
- assurer la conformité avec le RGPD ;
- réduire les redondances ;
- créer un dictionnaire de données ;
- concevoir un schéma relationnel normalisé ;
- créer une base de données et des tables ;
- importer les données ;
- vérifier le bon chargement ;
- produire des requêtes SQL d’analyse.

---

## Données utilisées

Le projet s’appuie sur trois fichiers principaux :

| Source | Description | Volume |
|---|---|---:|
| Données communes | Référentiel des communes | 34 991 lignes |
| Référentiel géographique | Données géographiques et administratives | 38 916 lignes |
| Valeurs foncières | Données de transactions immobilières | 34 169 lignes |

Ces fichiers ont été analysés, nettoyés et structurés afin de créer une base relationnelle exploitable.

---

## Méthodologie

La démarche suivie comprend plusieurs étapes :

1. **Analyse des données sources**  
   Exploration des fichiers initiaux, identification des colonnes, types de données, clés potentielles et redondances.

2. **Analyse RGPD**  
   Identification des données potentiellement sensibles, suppression ou anonymisation des informations non nécessaires.

3. **Nettoyage et préparation**  
   Suppression des doublons, réduction des colonnes inutiles et contrôle de cohérence des données.

4. **Création du dictionnaire de données**  
   Documentation des champs, types, longueurs, nature des données, règles de gestion et règles de calcul.

5. **Modélisation relationnelle**  
   Construction d’un schéma relationnel normalisé afin de limiter les redondances et faciliter les jointures.

6. **Création de la base et des tables**  
   Création de la base de données, du schéma et des tables avec SQL.

7. **Chargement des données**  
   Import des données préparées dans les tables créées.

8. **Vérification du chargement**  
   Contrôle du nombre de lignes et validation de la bonne insertion des données.

9. **Requêtes SQL d’analyse**  
   Création de requêtes permettant d’exploiter la base et de vérifier sa cohérence.

---

## Outils et technologies

| Outil | Usage |
|---|---|
| Snowflake | Création et exploitation de la base de données. |
| SQL | Création des tables, chargement, contrôles et requêtes d’analyse. |
| Excel | Exploration et préparation initiale des fichiers sources. |
| Modélisation relationnelle | Structuration logique de la base. |
| Dictionnaire de données | Documentation des champs et règles de gestion. |

---

## Résultats et valeur produite

Le projet a permis de produire une base de données immobilière structurée, documentée et exploitable.

Les principaux résultats sont :

- création d’un modèle relationnel clair ;
- réduction des redondances ;
- meilleure lisibilité des données ;
- documentation des champs et règles de gestion ;
- création de tables SQL exploitables ;
- chargement contrôlé des données ;
- prise en compte des enjeux RGPD ;
- mise à disposition d’un socle fiable pour l’analyse immobilière.

---

## Recommandations

Les recommandations principales sont :

- maintenir le dictionnaire de données à jour ;
- documenter toute transformation appliquée aux données sources ;
- contrôler systématiquement les clés et les volumes après chaque chargement ;
- limiter les données personnelles au strict nécessaire ;
- prévoir des contrôles qualité réguliers ;
- conserver une structure relationnelle claire pour faciliter les futures analyses.

---

## Compétences démontrées

### Compétences techniques

- SQL
- Snowflake
- Excel
- Modélisation relationnelle
- Normalisation BDD
- Dictionnaire de données
- Data warehouse
- Contrôle qualité
- Création de tables
- Vérification du chargement des données

### Compétences métier

- Analyse immobilière
- Structuration de données foncières
- Gouvernance data
- Qualité des données
- Conformité RGPD
- Documentation des règles de gestion
- Aide à la décision

### Soft skills

- Rigueur
- Structuration
- Autonomie
- Esprit critique
- Communication claire
- Pédagogie documentaire

---

## Lien avec le besoin Aéroworld

Ce projet répond directement aux attentes Aéroworld liées à la gestion de données à grande échelle, à l’intégration de sources multiples, à l’harmonisation des données et à la documentation.

Il démontre ma capacité à :

- structurer des données hétérogènes ;
- créer un modèle relationnel fiable ;
- documenter les champs et règles de gestion ;
- contrôler la qualité du chargement ;
- prendre en compte les contraintes de confidentialité et de conformité ;
- transformer des fichiers sources en base exploitable pour l’analyse.

Même si le domaine métier est immobilier, la démarche est transférable à un contexte aéronautique : organiser des données issues de plusieurs systèmes, les fiabiliser, les documenter et les rendre exploitables pour des usages analytiques.

---

## Livrables associés

- Schéma relationnel normalisé
- Dictionnaire de données
- Scripts SQL de création de base et de tables
- Requêtes SQL de contrôle
- Présentation client
- Base de données structurée

---

## Limites et pistes d’amélioration

Le projet se concentre principalement sur la création d’une base relationnelle et la structuration des données.

Des pistes d’amélioration possibles seraient :

- automatiser davantage les contrôles qualité ;
- ajouter des tests de cohérence avancés ;
- créer un dashboard d’exploitation des données immobilières ;
- enrichir la base avec des données socio-économiques ou géographiques complémentaires ;
- mettre en place une procédure de chargement récurrent ;
- documenter un processus complet de gouvernance et de mise à jour des données.

---

## Prèsentation du projet complet

[Présentation de projet.pdf](https://github.com/user-attachments/files/28318991/Presentation.de.projet.pdf)
