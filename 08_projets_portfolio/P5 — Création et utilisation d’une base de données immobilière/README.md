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

## Présentation complète du projet

<img width="1562" height="878" alt="image" src="https://github.com/user-attachments/assets/19e8170a-3720-42f1-9fcf-d4277280ab0e" />
<img width="1566" height="879" alt="image" src="https://github.com/user-attachments/assets/bb26806f-3dc5-40d6-8e01-ffc2602b5c5d" />
<img width="1566" height="880" alt="image" src="https://github.com/user-attachments/assets/78cc1c7b-3e49-4f9c-9d03-5bea2c2f2dc5" />
<img width="1565" height="876" alt="image" src="https://github.com/user-attachments/assets/57e07d2b-6ecc-45de-8492-fd117f2b8a6b" />
<img width="1568" height="880" alt="image" src="https://github.com/user-attachments/assets/31d54760-d275-44d0-93b8-e722ff627390" />
<img width="1565" height="877" alt="image" src="https://github.com/user-attachments/assets/62c2cf94-85b6-455a-9dd6-e5425b9eecfd" />
<img width="1566" height="879" alt="image" src="https://github.com/user-attachments/assets/5b0a7d15-53cc-4d1c-9a62-5ddd1b5bf34a" />
<img width="1561" height="875" alt="image" src="https://github.com/user-attachments/assets/03e5b346-7571-44bd-be43-e2620d5f6371" />
<img width="1562" height="878" alt="image" src="https://github.com/user-attachments/assets/4c794d4f-9c2b-4ec9-904b-5a5299199ea7" />
<img width="1567" height="878" alt="image" src="https://github.com/user-attachments/assets/4089259f-cbaf-4d32-8440-307d5934eb29" />
<img width="1570" height="878" alt="image" src="https://github.com/user-attachments/assets/97391813-9865-4ce2-87e7-5d08a7cb46b2" />
<img width="1563" height="877" alt="image" src="https://github.com/user-attachments/assets/6091ddff-0dce-4a60-b9a5-ba4e1de685ed" />
<img width="1563" height="879" alt="image" src="https://github.com/user-attachments/assets/964e8b8e-3306-49cb-8e7e-febadb259508" />
<img width="1565" height="876" alt="image" src="https://github.com/user-attachments/assets/fa58d9d8-cf9b-4bca-928c-4dd0a155892c" />
<img width="1563" height="873" alt="image" src="https://github.com/user-attachments/assets/41fa90f7-6b7c-4dad-b129-7193852654ff" />
<img width="1565" height="874" alt="image" src="https://github.com/user-attachments/assets/b5ad3163-bf98-402f-bc2a-c2bcac18acca" />
<img width="1562" height="879" alt="image" src="https://github.com/user-attachments/assets/e8e7c34a-cdd6-43e9-a7a2-110673101a02" />
<img width="1561" height="877" alt="image" src="https://github.com/user-attachments/assets/5041454f-a8db-498b-ba3d-0375eea2fd36" />
<img width="1563" height="877" alt="image" src="https://github.com/user-attachments/assets/6993dc16-91ce-44a9-926c-c974dd4d3c18" />
<img width="1564" height="874" alt="image" src="https://github.com/user-attachments/assets/d42cd091-3b8d-4bc7-90ce-f3b74f10c865" />
<img width="1561" height="881" alt="image" src="https://github.com/user-attachments/assets/63df00d8-6650-4cd8-86a3-82969f7fc712" />
<img width="1561" height="881" alt="image" src="https://github.com/user-attachments/assets/fa3a50e7-6d33-4a17-bb1f-25d32599710b" />
<img width="1570" height="880" alt="image" src="https://github.com/user-attachments/assets/5aacc076-4ad5-4709-98dc-1eeb044b6e95" />
<img width="1563" height="877" alt="image" src="https://github.com/user-attachments/assets/9f9ba31d-591e-4b50-aafa-ca09e4cf9f0d" />
<img width="1563" height="877" alt="image" src="https://github.com/user-attachments/assets/c59086ea-e5da-42bb-a181-6d0352618cda" />
<img width="1560" height="877" alt="image" src="https://github.com/user-attachments/assets/8db68401-2a34-4e28-bac9-3df3cbf7213a" />
