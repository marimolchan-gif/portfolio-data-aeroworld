# P9 — Analyse des ventes d’une librairie avec Python

## Synthèse exécutive

Ce projet consiste à analyser les ventes d’une librairie à partir de données clients, produits et transactions.

L’objectif est de comprendre l’évolution du chiffre d’affaires, d’identifier les comportements d’achat, d’analyser les profils clients et d’étudier les relations entre certaines variables comme l’âge, le sexe, la fréquence d’achat, le panier moyen et les catégories de livres achetées.

Ce projet démontre ma capacité à exploiter des données transactionnelles pour produire des indicateurs commerciaux, analyser le comportement client et formuler des constats utiles à la prise de décision marketing et commerciale.

---

## Contexte métier

Une librairie souhaite mieux comprendre son activité commerciale et le comportement de ses clients.

Les données disponibles permettent d’analyser :

- les ventes par période ;
- l’évolution du chiffre d’affaires ;
- les profils clients ;
- les catégories de produits vendues ;
- les comportements d’achat ;
- les liens entre caractéristiques clients et habitudes de consommation.

Le projet s’inscrit dans une logique d’**analyse commerciale**, d’**analyse client** et d’**aide à la décision**.

---

## Objectifs du projet

Les objectifs principaux sont les suivants :

- préparer et consolider les données clients, produits et transactions ;
- calculer les principaux indicateurs commerciaux ;
- analyser l’évolution du chiffre d’affaires par année et par trimestre ;
- étudier la répartition des clients par âge et par sexe ;
- analyser les comportements d’achat ;
- étudier les liens statistiques entre variables ;
- identifier les tendances commerciales ;
- formuler des constats exploitables pour le pilotage de l’activité.

---

## Données utilisées

Le projet s’appuie sur plusieurs jeux de données :

| Source | Description |
|---|---|
| Clients | Informations sur les clients : identifiant, sexe, âge ou date de naissance. |
| Produits | Informations sur les livres : identifiant produit, catégorie, prix. |
| Transactions | Données de ventes : identifiant transaction, date, client, produit et montant. |

Ces données ont été préparées et jointes afin de construire une base d’analyse unique permettant d’étudier les ventes et les comportements clients.

---

## Méthodologie

La démarche suivie comprend plusieurs étapes :

1. **Chargement des données**  
   Import des fichiers clients, produits et transactions.

2. **Préparation des données**  
   Vérification des formats, traitement des valeurs manquantes et contrôle des types de variables.

3. **Jointure des tables**  
   Fusion des données clients, produits et transactions afin d’obtenir une base complète.

4. **Création de variables d’analyse**  
   Création de variables temporelles, catégories d’âge, indicateurs d’achat et variables commerciales.

5. **Calcul des KPI commerciaux**  
   Calcul du chiffre d’affaires, du panier moyen, de la fréquence d’achat et des indicateurs par segment client.

6. **Analyse temporelle**  
   Analyse du chiffre d’affaires par année et par trimestre.

7. **Analyse client**  
   Étude des profils clients selon l’âge, le sexe et les comportements d’achat.

8. **Analyse statistique**  
   Étude des relations entre variables : genre, âge, montant dépensé, fréquence d’achat, panier moyen et catégories achetées.

9. **Visualisation des résultats**  
   Production de graphiques pour faciliter l’interprétation des tendances.

10. **Interprétation métier**  
   Formulation de constats utiles pour le pilotage commercial et marketing.

---

## Outils et technologies

| Outil | Usage |
|---|---|
| Python | Analyse et traitement des données. |
| Pandas | Préparation, jointures, agrégations et calculs d’indicateurs. |
| NumPy | Calculs numériques. |
| Matplotlib | Visualisation des résultats. |
| Seaborn | Visualisations statistiques. |
| Tests statistiques | Analyse des relations entre variables. |
| Jupyter Notebook | Développement et restitution de l’analyse. |

---

## Résultats et valeur produite

Le projet a permis de produire une lecture structurée de l’activité commerciale de la librairie.

Les principaux résultats sont :

- chiffre d’affaires 2021 : **4 584 976 €** ;
- chiffre d’affaires 2022 : **5 655 420 €** ;
- chiffre d’affaires 2023 : **902 969 €**, à interpréter avec prudence car la période semble incomplète ;
- analyse d’un portefeuille de **640 734 clients** ;
- identification d’une forte croissance du chiffre d’affaires en 2022 ;
- analyse des tendances annuelles et trimestrielles ;
- étude des comportements clients selon l’âge et le sexe ;
- analyse des liens entre âge, montant dépensé, fréquence d’achat, panier moyen et catégories achetées.

---

## Principaux constats

L’analyse met en évidence plusieurs éléments :

- le chiffre d’affaires progresse fortement entre 2021 et 2022 ;
- la baisse observée en 2023 doit être vérifiée, car elle peut être liée à une période d’observation incomplète ;
- le genre ne semble pas avoir d’influence notable sur les catégories de livres achetées ;
- l’âge influence faiblement le montant total dépensé ;
- les clients plus jeunes ont tendance à dépenser légèrement plus ;
- l’âge a une influence limitée sur la fréquence d’achat ;
- le panier moyen tend à diminuer avec l’âge ;
- l’âge est statistiquement lié aux catégories de livres achetées.

---

## Recommandations

Les recommandations principales sont :

- vérifier le périmètre temporel des données 2023 avant toute conclusion définitive ;
- suivre régulièrement l’évolution du chiffre d’affaires par trimestre ;
- approfondir l’analyse des segments clients les plus contributeurs ;
- analyser les catégories de livres les plus associées à chaque tranche d’âge ;
- mettre en place des indicateurs de suivi du panier moyen et de la fréquence d’achat ;
- utiliser les résultats pour orienter les actions marketing et commerciales ;
- envisager une segmentation client plus avancée, par exemple RFM.

---

## Compétences démontrées

### Compétences techniques

- Python
- Pandas
- NumPy
- Nettoyage de données
- Jointures de données
- Analyse exploratoire
- Statistiques descriptives
- Analyse univariée
- Analyse bivariée
- Analyse multivariée
- Analyse temporelle
- KPI commerciaux
- Visualisation de données
- Tests statistiques

### Compétences métier

- Analyse commerciale
- Analyse des ventes
- Analyse client
- Analyse produit
- Analyse du panier moyen
- Analyse de la fréquence d’achat
- Segmentation client
- Aide à la décision commerciale
- Analyse du comportement d’achat

### Soft skills

- Esprit analytique
- Rigueur
- Esprit critique
- Sens business
- Esprit de synthèse
- Communication claire
- Capacité à formuler des hypothèses métier

---

## Lien avec le besoin Aéroworld

Ce projet répond aux attentes Aéroworld liées à l’exploitation des données clients, à la transformation des données en informations exploitables et à l’aide à la décision.

Il démontre ma capacité à :

- consolider des données transactionnelles ;
- produire des indicateurs commerciaux ;
- analyser des comportements utilisateurs ;
- identifier des tendances ;
- interpréter des résultats statistiques ;
- formuler des constats métier utiles à la décision.

Même si le domaine métier est celui de la librairie, la démarche est transférable à un contexte industriel ou aéronautique : exploiter des données clients ou opérationnelles, identifier des comportements, détecter des tendances et produire une analyse utile au pilotage stratégique.

---

## Livrables associés

- Notebook Python d’analyse
- Base consolidée clients / produits / transactions
- Analyse du chiffre d’affaires
- Analyse temporelle annuelle et trimestrielle
- Analyse des profils clients
- Tests statistiques
- Visualisations des résultats
- Présentation client

---

## Limites et pistes d’amélioration

Le projet repose sur un périmètre de données qui semble incomplet pour l’année 2023, ce qui limite l’interprétation de la baisse du chiffre d’affaires sur cette période.

Des pistes d’amélioration possibles seraient :

- vérifier et compléter les données 2023 ;
- créer une segmentation RFM ;
- analyser la fidélisation client ;
- étudier les produits les plus performants par segment ;
- intégrer des indicateurs marketing complémentaires ;
- créer un dashboard interactif de suivi des ventes ;
- automatiser la mise à jour des indicateurs commerciaux.

---

## Présentation complète du projet

<img width="1085" height="613" alt="image" src="https://github.com/user-attachments/assets/da181551-434c-4167-870d-2cf8ce20dbdf" />

<img width="1082" height="608" alt="image" src="https://github.com/user-attachments/assets/a270109e-dc7c-4445-8af9-f5112411da23" />

<img width="1084" height="607" alt="image" src="https://github.com/user-attachments/assets/cb4d3310-d087-4422-9bf3-15fa6c22c9e5" />

<img width="1079" height="604" alt="image" src="https://github.com/user-attachments/assets/029002ba-5aee-43f1-a30b-fd074e1c159c" />

<img width="1082" height="608" alt="image" src="https://github.com/user-attachments/assets/202e0027-d4ec-49fb-80a0-68c304783881" />

<img width="1083" height="607" alt="image" src="https://github.com/user-attachments/assets/01e70198-2379-46a5-afa0-e242a2d7583d" />

<img width="1080" height="608" alt="image" src="https://github.com/user-attachments/assets/6fca0d78-80a9-4366-9177-6afd80c1de8a" />

<img width="1082" height="612" alt="image" src="https://github.com/user-attachments/assets/7e4a706b-3244-4166-8b21-ba76d5abaf70" />

<img width="1080" height="608" alt="image" src="https://github.com/user-attachments/assets/f98eef87-89a4-4176-bed7-fc06613730bb" />

<img width="1082" height="607" alt="image" src="https://github.com/user-attachments/assets/08a2951a-b981-4896-a498-5f7cac031d59" />

<img width="1085" height="610" alt="image" src="https://github.com/user-attachments/assets/0dcde208-d8be-483f-902f-977afff61d3c" />

<img width="1087" height="609" alt="image" src="https://github.com/user-attachments/assets/fea4e600-0785-439d-bce5-a33a4e85e09d" />

<img width="1080" height="611" alt="image" src="https://github.com/user-attachments/assets/a4ecbfb8-351b-4970-8571-84c854a961c0" />

<img width="1081" height="607" alt="image" src="https://github.com/user-attachments/assets/0ff44bcd-1c60-4d8c-a9fe-6b9939da823f" />

<img width="1078" height="612" alt="image" src="https://github.com/user-attachments/assets/b8af10ed-e61a-4659-bf6f-56c5b4643fea" />

<img width="1081" height="607" alt="image" src="https://github.com/user-attachments/assets/aaefe49a-9023-41fa-8b43-0e6196adeefb" />

<img width="1080" height="610" alt="image" src="https://github.com/user-attachments/assets/ed746241-e08d-45ca-8895-d25538f9f27d" />

<img width="1081" height="601" alt="image" src="https://github.com/user-attachments/assets/34ef6676-7be3-4f89-b118-8e9b8a0a999d" />
