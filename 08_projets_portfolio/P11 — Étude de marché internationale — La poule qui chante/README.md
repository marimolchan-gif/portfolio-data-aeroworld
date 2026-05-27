# P11 — Étude de marché internationale — La poule qui chante

## Synthèse exécutive

Ce projet consiste à réaliser une étude de marché internationale pour **La poule qui chante**, une entreprise française spécialisée dans le poulet issu de l’agriculture biologique.

L’objectif est d’identifier des pays à fort potentiel pour un développement international, sans liste de pays cible prédéfinie au départ.

Ce projet démontre ma capacité à structurer une analyse stratégique à partir de données open data, à sélectionner des indicateurs pertinents, à segmenter des pays et à formuler des recommandations orientées décision.

---

## Contexte métier

L’entreprise souhaite explorer de nouveaux marchés internationaux pour développer son activité.

Le choix des pays cibles doit tenir compte de plusieurs dimensions :

- niveau de développement économique ;
- capacité d’importation ;
- structure démographique ;
- urbanisation ;
- infrastructures ;
- consommation potentielle ;
- production locale ;
- risques liés à la sécurité alimentaire.

Le projet s’inscrit dans une logique de **market intelligence**, d’**analyse internationale** et d’**aide à la décision stratégique**.

---

## Objectifs du projet

Les objectifs principaux sont les suivants :

- sélectionner des données open data pertinentes ;
- construire un jeu de données consolidé par pays ;
- structurer l’analyse selon une logique PESTEL ;
- analyser les corrélations entre indicateurs ;
- réduire la dimension des données avec une ACP ;
- segmenter les pays à l’aide de méthodes de clustering ;
- identifier des groupes de pays comparables ;
- prioriser les marchés les plus pertinents ;
- formuler des recommandations pour orienter les futures études de marché.

---

## Données utilisées

Le projet s’appuie sur des données open data issues principalement de la **FAO** et de la **Banque mondiale**.

Le jeu de données final contient **128 pays** et **15 colonnes**, avec des indicateurs économiques, démographiques, commerciaux, agricoles et sociaux.

| Indicateur | Utilisation dans l’analyse |
|---|---|
| Accès à l’électricité | Niveau d’infrastructure |
| PIB par habitant | Pouvoir d’achat et développement économique |
| Importations de biens | Capacité d’importation |
| Croissance du PIB | Dynamique économique |
| Terres agricoles | Potentiel agricole local |
| Consommation d’électricité | Niveau de développement |
| Commerce de marchandises en % du PIB | Ouverture commerciale |
| Population 15–64 ans | Population active potentielle |
| Population 65 ans et plus | Structure démographique |
| Densité de population | Concentration du marché |
| Population urbaine | Urbanisation |
| Sous-alimentation | Fragilité alimentaire |
| Importation de volaille | Dépendance aux importations |
| Production de volaille | Capacité de production locale |

---

## Méthodologie

La démarche suivie comprend plusieurs étapes :

1. **Sélection des indicateurs**  
   Choix d’indicateurs pertinents pour évaluer l’attractivité des pays selon une logique PESTEL.

2. **Collecte et consolidation des données**  
   Rassemblement des données FAO et Banque mondiale dans un jeu de données unique.

3. **Nettoyage et préparation**  
   Harmonisation des formats, gestion des valeurs manquantes et contrôle de cohérence.

4. **Analyse exploratoire**  
   Étude des distributions, comparaison des pays et premières observations sur les indicateurs.

5. **Analyse de corrélation**  
   Production d’une matrice de corrélation de Spearman pour identifier les relations entre variables.

6. **Analyse en Composantes Principales — ACP**  
   Réduction de la dimension des données afin de mieux visualiser les structures et profils de pays.

7. **Interprétation des axes**  
   Analyse des composantes principales pour comprendre les facteurs qui différencient les pays.

8. **Clustering**  
   Segmentation des pays à l’aide de la CAH et de K-means.

9. **Analyse des clusters**  
   Interprétation des groupes de pays selon leurs caractéristiques économiques, commerciales et démographiques.

10. **Recommandations stratégiques**  
    Identification des marchés à approfondir en priorité.

---

## Outils et technologies

| Outil | Usage |
|---|---|
| Python | Analyse, traitement et modélisation des données. |
| Pandas | Nettoyage, consolidation et manipulation des données. |
| NumPy | Calculs numériques. |
| Matplotlib | Visualisation des résultats. |
| Seaborn | Analyse graphique et corrélations. |
| Scikit-learn | ACP, clustering et préparation des modèles. |
| ACP / PCA | Réduction dimensionnelle. |
| CAH | Classification ascendante hiérarchique. |
| K-means | Segmentation des pays. |
| Données FAO / Banque mondiale | Sources open data utilisées pour l’analyse. |

---

## Résultats et valeur produite

Le projet a permis de transformer un besoin stratégique large en analyse structurée et exploitable.

Les principaux résultats sont :

- création d’un dataset international consolidé ;
- sélection de 14 indicateurs structurants ;
- structuration de l’analyse selon une approche PESTEL ;
- identification des corrélations entre développement économique, commerce, urbanisation et sécurité alimentaire ;
- réduction de la complexité des données grâce à l’ACP ;
- interprétation des axes principaux ;
- segmentation des pays en groupes cohérents ;
- identification de profils de marchés à potentiel ;
- production d’une base de priorisation pour les futures études commerciales.

---

## Principaux constats

L’analyse met en évidence plusieurs dimensions clés :

- les pays les plus développés se distinguent par un PIB par habitant élevé, une forte urbanisation et de meilleures infrastructures ;
- certains pays présentent une forte ouverture commerciale et une capacité d’importation intéressante ;
- les indicateurs de sous-alimentation permettent d’identifier des marchés plus fragiles ou moins prioritaires ;
- l’ACP permet de structurer les pays selon des axes de développement économique, d’importation et de profil démographique ;
- le clustering permet d’identifier des groupes de pays comparables et de prioriser les zones à approfondir.

---

## Recommandations

Les recommandations principales sont :

- concentrer les futures études de marché sur les clusters de pays économiquement développés et ouverts au commerce ;
- analyser plus finement les pays présentant une forte capacité d’importation ;
- intégrer des données spécifiques au marché du poulet biologique ;
- compléter l’analyse quantitative par une étude réglementaire et concurrentielle ;
- approfondir les pays présentant un bon équilibre entre pouvoir d’achat, urbanisation et dépendance aux importations ;
- éviter de sélectionner les pays uniquement sur la base d’un indicateur isolé.

---

## Compétences démontrées

### Compétences techniques

- Python
- Pandas
- NumPy
- Nettoyage de données
- Fusion de données
- Analyse exploratoire
- Analyse multivariée
- Analyse de corrélation
- Visualisation de données
- ACP
- Clustering
- CAH
- K-means
- Scikit-learn

### Compétences métier

- Analyse de marché
- Analyse internationale
- Analyse PESTEL
- Market intelligence
- Segmentation marché
- Priorisation de pays
- Analyse socio-économique
- Aide à la décision stratégique
- Recommandations business

### Soft skills

- Autonomie
- Structuration
- Esprit critique
- Esprit de synthèse
- Orientation solution
- Communication claire
- Capacité à justifier les choix méthodologiques
- Vision stratégique

---

## Lien avec le besoin Aéroworld

Ce projet répond aux attentes Aéroworld liées à la valorisation stratégique des données, à l’analyse fiable, aux techniques avancées d’analyse et à l’aide à la décision.

Il démontre ma capacité à :

- structurer un besoin métier large et peu défini ;
- sélectionner des indicateurs pertinents ;
- consolider des données open data ;
- appliquer une méthodologie d’analyse stratégique ;
- utiliser des méthodes avancées comme l’ACP et le clustering ;
- transformer des données complexes en recommandations actionnables.

Même si le domaine métier est agroalimentaire, la démarche est transférable à un contexte aéronautique international : analyser des données multi-sources, segmenter des environnements complexes, identifier des priorités et orienter la décision stratégique.

---

## Livrables associés

- Notebook Python d’analyse
- Dataset international consolidé
- Analyse PESTEL
- Matrice de corrélation
- ACP avec interprétation des axes
- Clustering CAH et K-means
- Segmentation des pays
- Présentation client
- Recommandations stratégiques

---

## Limites et pistes d’amélioration

Le projet repose sur des données macro-économiques et open data. Il constitue donc une première analyse de priorisation, mais ne remplace pas une étude de marché complète.

Des pistes d’amélioration possibles seraient :

- intégrer des données plus récentes ;
- ajouter des indicateurs spécifiques au poulet biologique ;
- analyser la concurrence par pays ;
- étudier les contraintes réglementaires d’importation ;
- intégrer des données de prix et de consommation ;
- approfondir les habitudes alimentaires locales ;
- créer un dashboard interactif de comparaison des pays ;
- compléter l’analyse quantitative par une étude qualitative.

---

## Présentation complète du projet

<img width="1560" height="884" alt="image" src="https://github.com/user-attachments/assets/9738a491-3589-4004-bc7f-5fc56bf8e9a4" />
<img width="1559" height="874" alt="image" src="https://github.com/user-attachments/assets/537a3aec-7aba-40cf-9147-b6a5932645c7" />
<img width="1562" height="878" alt="image" src="https://github.com/user-attachments/assets/936ef576-a134-43cb-ba95-47c4dd1ef2d2" />
<img width="1561" height="877" alt="image" src="https://github.com/user-attachments/assets/6ebdc744-8489-4eab-84bf-08ebfb36aaf9" />
<img width="1562" height="881" alt="image" src="https://github.com/user-attachments/assets/17bc2417-00c4-47d8-a872-7cb69cebdfde" />
<img width="1564" height="880" alt="image" src="https://github.com/user-attachments/assets/13dd2362-451e-4b24-9e94-59af8b96f301" />
<img width="1559" height="880" alt="image" src="https://github.com/user-attachments/assets/551ef76b-aac1-4557-ab7a-6241949bde8b" />
<img width="1568" height="880" alt="image" src="https://github.com/user-attachments/assets/69f2afb5-2bd0-47db-83da-8ee815a34aa6" />
<img width="1561" height="878" alt="image" src="https://github.com/user-attachments/assets/c108d5c6-b571-45e5-b271-52589fc48dd5" />
<img width="1563" height="876" alt="image" src="https://github.com/user-attachments/assets/ea33618c-3750-4a00-bdea-4c9067ae11fd" />

