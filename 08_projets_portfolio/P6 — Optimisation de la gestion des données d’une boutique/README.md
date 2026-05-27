# P6 — Optimisation de la gestion des données d’une boutique

## Synthèse exécutive

Ce projet consiste à optimiser la gestion des données d’une boutique de vins en ligne à partir de plusieurs fichiers issus de systèmes différents.

L’objectif est de consolider les données web, ERP et de liaison afin d’analyser les ventes, les stocks, les prix, les marges et les anomalies.

Ce projet démontre ma capacité à nettoyer, fiabiliser et exploiter des données commerciales hétérogènes pour produire des analyses orientées performance, qualité des données et aide à la décision.

---

## Contexte métier

Une boutique de vins en ligne dispose de plusieurs sources de données :

- un fichier web contenant les informations produits publiées en ligne ;
- un fichier ERP contenant les données de stock, prix et ventes ;
- un fichier de liaison permettant de rapprocher les références entre les deux systèmes.

L’entreprise souhaite fiabiliser ses données afin de mieux piloter son catalogue, identifier les anomalies, analyser les ventes et améliorer la gestion commerciale.

Le projet s’inscrit dans une logique de **data cleaning**, **analyse commerciale** et **contrôle qualité des données**.

---

## Objectifs du projet

Les objectifs principaux sont les suivants :

- explorer les fichiers sources ;
- nettoyer les données web, ERP et de liaison ;
- contrôler les clés de jointure ;
- fusionner les sources de données ;
- vérifier les incohérences entre stock, prix et ventes ;
- détecter les valeurs aberrantes ;
- analyser le chiffre d’affaires ;
- identifier les meilleurs produits ;
- analyser les marges ;
- formuler des recommandations opérationnelles.

---

## Données utilisées

Le projet s’appuie sur trois fichiers principaux :

| Source | Description | Volume |
|---|---|---:|
| `web.xlsx` | Données produits issues du site web | 1 513 lignes, 29 colonnes |
| `erp.xlsx` | Données ERP : prix, stock, ventes | 825 lignes, 6 colonnes |
| `liaison.xlsx` | Table de correspondance entre références web et ERP | 825 lignes, 2 colonnes |

Ces fichiers ont été contrôlés, nettoyés et consolidés pour construire une base d’analyse commerciale fiable.

---

## Méthodologie

La démarche suivie comprend plusieurs étapes :

1. **Exploration des fichiers sources**  
   Analyse des structures, colonnes, types de données, valeurs manquantes et doublons.

2. **Nettoyage des données**  
   Suppression des colonnes vides, traitement des valeurs manquantes, contrôle des doublons et des clés.

3. **Contrôle qualité**  
   Vérification de la cohérence entre les données web, ERP et liaison.

4. **Fusion des données**  
   Jointure des fichiers afin de créer une base consolidée exploitable pour l’analyse.

5. **Analyse univariée des prix**  
   Étude de la distribution des prix, calcul des quartiles, IQR et seuils d’outliers.

6. **Détection des anomalies**  
   Identification des valeurs aberrantes à partir des méthodes IQR et Z-score.

7. **Analyse du chiffre d’affaires**  
   Calcul du chiffre d’affaires total et identification des produits les plus performants.

8. **Analyse des ventes et quantités vendues**  
   Identification du top 20 des produits par chiffre d’affaires et par volume vendu.

9. **Analyse des marges**  
   Calcul et interprétation des marges, détection des produits à marge négative.

10. **Analyse de corrélation**  
    Étude des liens entre stock, ventes et prix.

11. **Recommandations**  
    Formulation de recommandations pour améliorer la qualité des données et le pilotage commercial.

---

## Outils et technologies

| Outil | Usage |
|---|---|
| Python | Traitement, analyse et automatisation des calculs. |
| Pandas | Nettoyage, fusion et manipulation des données. |
| NumPy | Calculs numériques. |
| Matplotlib | Visualisation des résultats. |
| Seaborn | Graphiques statistiques et corrélations. |
| Excel | Source des fichiers initiaux. |
| Jupyter Notebook | Développement et restitution de l’analyse. |

---

## Résultats et valeur produite

Le projet a permis de produire une analyse complète de la qualité des données et de la performance commerciale de la boutique.

Les principaux résultats sont :

- consolidation des fichiers web, ERP et liaison ;
- suppression des colonnes vides, valeurs manquantes et doublons ;
- vérification des incohérences entre stock, statut de stock et ventes ;
- détection de **36 prix considérés comme outliers**, soit **4,36 % du catalogue** ;
- calcul du chiffre d’affaires total d’octobre : **143 680,10 €** ;
- identification des produits les plus performants par chiffre d’affaires ;
- identification des produits les plus vendus en quantité ;
- détection de **7 produits avec des marges négatives** ;
- analyse des corrélations entre stock, ventes et prix.

---

## Principaux constats

L’analyse met en évidence plusieurs points importants :

- certains prix présentent des valeurs atypiques nécessitant une vérification métier ;
- des incohérences existent entre les données web, ERP et liaison ;
- les ventes sont concentrées sur un nombre limité de produits performants ;
- certains produits génèrent des marges négatives et doivent être analysés en priorité ;
- la relation entre prix et ventes est négative, ce qui suggère que les produits plus chers se vendent généralement moins ;
- le stock et les ventes présentent une corrélation positive modérée.

---

## Recommandations

Les recommandations principales sont :

- nettoyer et normaliser régulièrement les données produits ;
- mettre en place des contrôles automatiques sur les prix, stocks et marges ;
- vérifier les produits identifiés comme outliers ;
- analyser en priorité les produits à marge négative ;
- améliorer la synchronisation entre les données web et ERP ;
- suivre régulièrement les indicateurs de chiffre d’affaires, stock et marge ;
- documenter les règles de gestion pour éviter les incohérences futures.

---

## Compétences démontrées

### Compétences techniques

- Python
- Pandas
- NumPy
- Excel
- Nettoyage de données
- Jointures de données
- Contrôle qualité
- Analyse exploratoire
- Analyse univariée
- Analyse de corrélation
- Détection d’outliers
- IQR
- Z-score
- Visualisation de données

### Compétences métier

- Analyse commerciale
- Analyse des ventes
- Analyse produit
- Analyse des stocks
- Analyse des marges
- Analyse e-commerce
- Aide à la décision
- Recommandations opérationnelles

### Soft skills

- Rigueur
- Esprit critique
- Sens business
- Orientation solution
- Priorisation
- Communication claire
- Structuration d’une analyse

---

## Lien avec le besoin Aéroworld

Ce projet répond aux attentes Aéroworld liées à la qualité des données, à la consolidation de sources, à l’analyse fiable et à la transformation des données en informations exploitables.

Il démontre ma capacité à :

- intégrer des données issues de systèmes différents ;
- fiabiliser des données opérationnelles ;
- détecter des anomalies ;
- produire des indicateurs utiles à la décision ;
- identifier des incohérences métier ;
- formuler des recommandations concrètes.

Même si le domaine métier est celui du e-commerce, la démarche est transférable à un contexte aéronautique : consolider des sources hétérogènes, contrôler la qualité des données, détecter des anomalies et produire une lecture opérationnelle fiable.

---

## Livrables associés

- Notebook Python d’analyse
- Fichiers nettoyés et consolidés
- Analyse des prix et outliers
- Analyse du chiffre d’affaires
- Analyse des stocks et marges
- Matrice de corrélation
- Présentation client
- Recommandations opérationnelles

---

## Limites et pistes d’amélioration

Le projet repose sur des fichiers ponctuels et ne met pas encore en place de pipeline automatisé de mise à jour.

Des pistes d’amélioration possibles seraient :

- automatiser les contrôles qualité ;
- créer un dashboard de suivi commercial ;
- mettre en place des alertes sur les prix anormaux ;
- suivre automatiquement les marges négatives ;
- améliorer la synchronisation entre les systèmes web et ERP ;
- enrichir l’analyse avec des données temporelles plus détaillées ;
- documenter un processus de contrôle qualité récurrent.

---

## Présentation complète du projet

<img width="1560" height="876" alt="image" src="https://github.com/user-attachments/assets/fe8d59e2-e949-4cf1-987c-7af0bcc0bf74" />
<img width="1565" height="874" alt="image" src="https://github.com/user-attachments/assets/77cec230-ce08-470a-b8d6-426dba4b21e1" />
<img width="1562" height="879" alt="image" src="https://github.com/user-attachments/assets/7f21a2e4-043e-4741-a4a5-513bb8e776c6" />
<img width="1562" height="877" alt="image" src="https://github.com/user-attachments/assets/16ed59ab-a0f7-400a-a51e-25c247d27873" />
<img width="1558" height="880" alt="image" src="https://github.com/user-attachments/assets/ae73efec-c984-4d66-976f-81e8506920ef" />
<img width="1563" height="875" alt="image" src="https://github.com/user-attachments/assets/ea43c9c3-0b38-473c-9b9d-6452c2505131" />
<img width="1564" height="882" alt="image" src="https://github.com/user-attachments/assets/f7282b93-0dd9-46b5-afe9-897c037b4c27" />
<img width="1560" height="881" alt="image" src="https://github.com/user-attachments/assets/c10a34ac-b160-497e-9581-04fde592fc53" />
<img width="1561" height="872" alt="image" src="https://github.com/user-attachments/assets/179771e5-b46b-4bdd-b2f1-b68d5ed56646" />
<img width="1561" height="876" alt="image" src="https://github.com/user-attachments/assets/000da92b-c424-4b88-b9bc-28f16c8fef52" />
<img width="1565" height="878" alt="image" src="https://github.com/user-attachments/assets/13d284fb-d2e5-47bd-be95-cf8e5ebc6149" />
<img width="1563" height="879" alt="image" src="https://github.com/user-attachments/assets/a799270a-9f3c-490c-a40e-4f4eff4af185" />
<img width="1566" height="877" alt="image" src="https://github.com/user-attachments/assets/23af4f1f-5e99-4063-bf5b-942e41a951ec" />
