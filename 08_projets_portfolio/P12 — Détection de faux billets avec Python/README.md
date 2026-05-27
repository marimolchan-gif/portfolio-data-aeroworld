# P12 — Détection de faux billets avec Python

## Synthèse exécutive

Ce projet consiste à développer un modèle de machine learning permettant de détecter automatiquement les faux billets à partir de leurs caractéristiques physiques.

L’objectif est de comparer plusieurs approches de classification, d’évaluer leurs performances et de sélectionner le modèle le plus adapté à un usage opérationnel, avec une attention particulière portée à la réduction des erreurs critiques.

Ce projet démontre ma capacité à construire une solution prédictive, à évaluer des modèles de machine learning et à relier les performances techniques à un enjeu métier de gestion du risque.

---

## Contexte métier

La détection de faux billets représente un enjeu opérationnel important pour limiter les risques financiers et fiabiliser les processus de contrôle.

Dans ce type de projet, l’objectif n’est pas seulement d’obtenir un bon score global. Il est surtout essentiel de limiter les erreurs les plus critiques : les faux billets non détectés.

Le projet s’inscrit dans une logique de :

- détection de fraude ;
- classification automatique ;
- réduction du risque ;
- fiabilisation de la décision ;
- automatisation d’un processus de contrôle.

---

## Objectifs du projet

Les objectifs principaux sont les suivants :

- analyser les caractéristiques physiques des billets ;
- identifier les variables les plus discriminantes ;
- explorer les distributions des variables ;
- analyser les corrélations avec la variable cible ;
- tester plusieurs modèles de machine learning ;
- comparer les performances des modèles ;
- analyser les faux positifs et faux négatifs ;
- sélectionner le modèle le plus pertinent ;
- créer un processus de prédiction à partir d’un fichier CSV.

---

## Données utilisées

Le jeu de données contient des mesures physiques de billets, associées à une variable cible indiquant si le billet est authentique ou faux.

| Variable | Description |
|---|---|
| `is_genuine` | Variable cible indiquant si le billet est authentique ou faux. |
| `diagonal` | Mesure de la diagonale du billet. |
| `height_left` | Hauteur mesurée à gauche. |
| `height_right` | Hauteur mesurée à droite. |
| `margin_low` | Marge inférieure. |
| `margin_up` | Marge supérieure. |
| `length` | Longueur du billet. |

---

## Méthodologie

La démarche suivie comprend plusieurs étapes :

1. **Exploration des données**  
   Analyse initiale du dataset, des variables disponibles et de la variable cible.

2. **Analyse des distributions**  
   Comparaison des distributions des caractéristiques physiques selon que les billets sont vrais ou faux.

3. **Analyse de corrélation**  
   Identification des variables les plus liées à l’authenticité des billets.

4. **Prétraitement des données**  
   Préparation des variables, séparation des données d’entraînement et de test, standardisation lorsque nécessaire.

5. **Modélisation**  
   Test de plusieurs modèles : K-means, régression logistique, KNN et Random Forest.

6. **Évaluation des modèles**  
   Comparaison des performances selon plusieurs métriques : accuracy, précision, rappel, F1-score, AUC et erreurs critiques.

7. **Analyse des erreurs**  
   Étude des faux positifs et faux négatifs, avec une attention particulière portée aux faux billets non détectés.

8. **Choix du modèle final**  
   Sélection du modèle offrant le meilleur équilibre entre performance, fiabilité et interprétabilité.

9. **Application de prédiction**  
   Mise en place d’un processus permettant de prédire l’authenticité de nouveaux billets à partir d’un fichier CSV.

---

## Outils et technologies

| Outil | Usage |
|---|---|
| Python | Analyse, modélisation et prédiction. |
| Pandas | Préparation et manipulation des données. |
| NumPy | Calculs numériques. |
| Matplotlib | Visualisation des résultats. |
| Seaborn | Analyse graphique des distributions et corrélations. |
| Scikit-learn | Entraînement, comparaison et évaluation des modèles. |
| CSV | Format d’entrée pour l’application de prédiction. |

---

## Résultats et valeur produite

Le projet a permis de comparer plusieurs modèles de classification et de sélectionner la régression logistique comme modèle final.

Les principaux résultats sont :

- identification des variables les plus discriminantes ;
- forte corrélation positive entre `length` et l’authenticité du billet ;
- forte corrélation négative entre `margin_low` et l’authenticité ;
- comparaison de plusieurs modèles de classification ;
- sélection de la régression logistique comme modèle final ;
- accuracy du modèle final : **0,990** ;
- précision sur les faux billets : **0,98** ;
- rappel sur les faux billets : **0,99** ;
- F1-score sur les faux billets : **0,985** ;
- AUC : **0,99** ;
- seulement **1 faux billet non détecté**.

---

## Comparaison des modèles

| Modèle | Rôle dans l’analyse | Résultat principal |
|---|---|---|
| K-means | Approche exploratoire de regroupement | Permet d’observer une séparation naturelle partielle des billets. |
| Régression logistique | Modèle de classification interprétable | Modèle final retenu. |
| KNN | Modèle basé sur la proximité entre observations | Bonnes performances, mais moins retenu que la régression logistique. |
| Random Forest | Modèle robuste basé sur des arbres de décision | Très bonnes performances, mais moins interprétable. |

---

## Principaux constats

L’analyse met en évidence plusieurs points importants :

- la variable `length` est l’une des plus discriminantes ;
- les variables liées aux marges sont également très utiles pour distinguer les vrais et faux billets ;
- la performance globale des modèles est élevée ;
- l’analyse des erreurs est plus importante que l’accuracy seule ;
- le rappel sur les faux billets est un critère prioritaire ;
- la régression logistique offre un bon équilibre entre performance et interprétabilité.

---

## Recommandations

Les recommandations principales sont :

- privilégier un modèle interprétable pour faciliter son usage opérationnel ;
- suivre en priorité les faux négatifs, car ils représentent l’erreur métier la plus critique ;
- conserver une analyse détaillée de la matrice de confusion ;
- ajuster éventuellement le seuil de décision selon le niveau de risque accepté ;
- tester le modèle sur de nouvelles données avant un déploiement réel ;
- mettre en place un suivi régulier des performances du modèle ;
- documenter les conditions d’utilisation du modèle prédictif.

---

## Compétences démontrées

### Compétences techniques

- Python
- Pandas
- NumPy
- Scikit-learn
- Machine learning
- Classification
- Régression logistique
- KNN
- Random Forest
- K-means
- Standardisation
- Évaluation de modèle
- Matrice de confusion
- Faux positifs
- Faux négatifs
- Visualisation de données
- Analyse de corrélation

### Compétences métier

- Détection de fraude
- Gestion du risque
- Automatisation analytique
- Aide à la décision
- Réduction des erreurs critiques
- Fiabilisation d’un processus de contrôle
- Interprétation métier des performances modèle

### Soft skills

- Rigueur
- Esprit critique
- Sens du risque
- Orientation solution
- Capacité à arbitrer entre performance et interprétabilité
- Vulgarisation d’un modèle prédictif
- Structuration d’un processus analytique

---

## Lien avec le besoin Aéroworld

Ce projet répond aux attentes Aéroworld liées à l’apprentissage automatique, à l’intelligence artificielle, à la détection d’anomalies, à la gestion du risque et à la fiabilisation de la décision.

Il démontre ma capacité à :

- construire un modèle prédictif ;
- comparer plusieurs méthodes de machine learning ;
- évaluer les performances avec des métriques adaptées ;
- analyser les erreurs critiques ;
- sélectionner un modèle selon des critères métier ;
- automatiser un processus de décision ;
- expliquer les résultats de manière claire et opérationnelle.

Même si le domaine métier est la détection de faux billets, la démarche est transférable à un contexte aéronautique : maintenance prédictive, détection d’anomalies, contrôle qualité, analyse de risques ou surveillance de données opérationnelles.

---

## Livrables associés

- Notebook Python d’analyse
- Analyse exploratoire des variables
- Visualisations des distributions
- Analyse de corrélation
- Comparaison de modèles de machine learning
- Matrice de confusion
- Évaluation des faux positifs et faux négatifs
- Application de prédiction à partir d’un fichier CSV
- Présentation client

---

## Limites et pistes d’amélioration

Le projet repose sur un jeu de données structuré et limité à des caractéristiques physiques précises.

Des pistes d’amélioration possibles seraient :

- tester le modèle sur un volume de données plus important ;
- intégrer de nouvelles variables physiques ou contextuelles ;
- ajuster le seuil de classification selon le coût métier des erreurs ;
- mettre en place un suivi des performances dans le temps ;
- prévoir une procédure de réentraînement du modèle ;
- créer une interface utilisateur pour faciliter l’usage du modèle ;
- documenter un processus complet de déploiement et de monitoring.

---

## Présentation complète du projet

<img width="1562" height="880" alt="image" src="https://github.com/user-attachments/assets/fa828052-0c3f-4d3e-97fc-b9b92c515822" />
<img width="1559" height="879" alt="image" src="https://github.com/user-attachments/assets/67dd84e9-05ff-4e8a-95f2-22b1baa9b770" />
<img width="1562" height="875" alt="image" src="https://github.com/user-attachments/assets/e086fe54-4e07-4352-94dd-99a268400bce" />
<img width="1560" height="876" alt="image" src="https://github.com/user-attachments/assets/cde5d0d0-1ea7-4dcd-a0ed-a12a258bcca4" />
<img width="1563" height="879" alt="image" src="https://github.com/user-attachments/assets/e99e1070-1e82-4c3f-b383-69777c368f4b" />
<img width="1566" height="879" alt="image" src="https://github.com/user-attachments/assets/656eaaa3-a89c-4b3c-9091-dd6a71274d27" />
<img width="1560" height="878" alt="image" src="https://github.com/user-attachments/assets/201cdc82-b6ce-4e31-bed0-78016f714ddd" />
<img width="1560" height="877" alt="image" src="https://github.com/user-attachments/assets/3d462757-c8f3-47eb-8b5a-3fd36951baf3" />
<img width="1559" height="877" alt="image" src="https://github.com/user-attachments/assets/ab65b3ad-ac32-4621-9640-ef8c3fc98532" />
<img width="1567" height="881" alt="image" src="https://github.com/user-attachments/assets/b7708c81-ab21-4f6c-8ae3-30b009d57541" />
<img width="1559" height="880" alt="image" src="https://github.com/user-attachments/assets/13a83793-f28c-4782-b0c8-fcd21340cafb" />
<img width="1563" height="878" alt="image" src="https://github.com/user-attachments/assets/08b3b399-feaf-4d9f-a2e9-cacbfdac3789" />
<img width="1565" height="877" alt="image" src="https://github.com/user-attachments/assets/a1a15798-7999-49b4-ade1-5d33fe03aa27" />
<img width="1563" height="875" alt="image" src="https://github.com/user-attachments/assets/bb8c68a5-577f-4564-bb2c-0524d77d14a8" />

