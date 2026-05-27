# P7 — Création d’un tableau de bord dynamique avec Power BI

## Synthèse exécutive

Ce projet consiste à concevoir un tableau de bord Power BI destiné au suivi des indicateurs clés de projets pour l’entreprise Sanitoral.

L’objectif est de permettre à différents niveaux de management — directeurs pays, directeurs régionaux et direction générale — de suivre la performance des projets IT et Marketing à travers des indicateurs de coûts, délais et livrables.

Ce projet démontre ma capacité à concevoir un dashboard décisionnel complet, structuré par niveaux d’analyse, avec une navigation claire, des KPI pertinents, une logique de pilotage projet et une documentation de prise en main.

---

## Contexte métier

Sanitoral souhaite suivre la performance de ses projets internes à plusieurs niveaux de décision.

Les utilisateurs cibles sont :

- les directeurs pays ;
- les directeurs régionaux ;
- la direction générale.

Chaque niveau a besoin d’une lecture adaptée :

- vision détaillée par pays ;
- vision consolidée par région ;
- vision globale pour la direction ;
- suivi des écarts entre prévisions et résultats réels ;
- identification rapide des projets en difficulté.

Le projet s’inscrit dans une logique de **Business Intelligence**, de **pilotage de projet** et d’**aide à la décision**.

---

## Objectifs du projet

Les objectifs principaux sont les suivants :

- construire un tableau de bord dynamique dans Power BI ;
- suivre les indicateurs clés de performance projet ;
- comparer les valeurs prévues et réelles ;
- identifier les écarts critiques ;
- permettre une analyse par pays, région et niveau global ;
- créer une navigation claire entre les pages du rapport ;
- documenter la procédure de mise à jour des données ;
- adapter les visuels aux besoins des différents utilisateurs.

---

## Données utilisées

Le projet s’appuie sur un fichier source contenant les informations liées aux projets Sanitoral.

Les données comprennent notamment :

| Donnée | Description |
|---|---|
| Project ID | Identifiant unique du projet. |
| Project type | Type de projet : IT ou Marketing. |
| Region | Région géographique du projet. |
| Country | Pays concerné par le projet. |
| Phase | Phase du projet. |
| Planned cost | Coût prévu. |
| Actual cost | Coût réel. |
| Planned duration | Durée prévue. |
| Actual duration | Durée réelle. |
| Planned deliverables | Nombre de livrables prévus. |
| Actual deliverables | Nombre de livrables réalisés. |
| Dates | Dates de début, de fin et informations temporelles associées. |

Ces données ont été transformées et enrichies afin de construire des indicateurs de suivi fiables.

---

## Méthodologie

La démarche suivie comprend plusieurs étapes :

1. **Analyse du besoin utilisateur**  
   Identification des publics cibles et des indicateurs attendus pour chaque niveau de management.

2. **Structuration du rapport**  
   Organisation du dashboard en plusieurs pages : page d’accueil, documentation de mise à jour, Product Strategy Canvas, Gantt, analyse pays, analyse régionale et analyse générale.

3. **Préparation des données dans Power Query**  
   Nettoyage, transformation, typage des colonnes et création de variables utiles pour l’analyse.

4. **Création des indicateurs DAX**  
   Calcul des écarts entre valeurs prévues et réelles : coûts, durées et livrables.

5. **Définition des seuils critiques**  
   Mise en évidence des écarts importants, notamment lorsque la variance atteint ou dépasse 15 %.

6. **Conception des visualisations**  
   Création de cartes KPI, tableaux, graphiques de variance, cartes géographiques, jauges et Gantt.

7. **Création de la navigation**  
   Mise en place d’une page d’accueil et de boutons de navigation pour faciliter l’utilisation du rapport.

8. **Documentation de la mise à jour**  
   Rédaction d’une procédure expliquant comment remplacer ou actualiser le fichier source.

9. **Contrôle final du dashboard**  
   Vérification de la lisibilité, cohérence des filtres, clarté des indicateurs et bon fonctionnement de la navigation.

---

## Outils et technologies

| Outil | Usage |
|---|---|
| Power BI | Création du dashboard et des pages d’analyse. |
| Power Query | Transformation et préparation des données. |
| DAX | Création des mesures et indicateurs de performance. |
| Excel | Source de données initiale. |
| Gantt visual | Visualisation des durées prévues et réelles par phase projet. |
| Cartes Power BI | Analyse géographique par pays et région. |
| Product Strategy Canvas | Formalisation du besoin utilisateur et des objectifs du dashboard. |

---

## Résultats et valeur produite

Le projet a permis de créer un tableau de bord complet pour le pilotage des projets Sanitoral.

Les principaux résultats sont :

- création d’un rapport Power BI multi-pages ;
- mise en place d’une navigation claire ;
- suivi des projets par pays, région et niveau global ;
- calcul des écarts de coûts, durées et livrables ;
- identification des projets présentant au moins une variance critique ;
- visualisation des durées planifiées et réelles via un Gantt ;
- création de cartes géographiques pour analyser les projets par zone ;
- documentation de la procédure de mise à jour des données ;
- adaptation des pages aux besoins de différents niveaux de management.

---

## Principaux indicateurs suivis

| Indicateur | Description |
|---|---|
| Cost variance | Écart entre coût prévu et coût réel. |
| Duration variance | Écart entre durée prévue et durée réelle. |
| Deliverable variance | Écart entre livrables prévus et livrables réalisés. |
| Planned cost | Coût total prévu. |
| Actual cost | Coût total réel. |
| Planned duration | Durée totale prévue. |
| Actual duration | Durée totale réelle. |
| Planned deliverables | Nombre de livrables prévus. |
| Actual deliverables | Nombre de livrables réalisés. |
| Critical variance | Indicateur signalant une variance supérieure ou égale à 15 %. |

---

## Recommandations

Les recommandations principales sont :

- suivre régulièrement les projets présentant des écarts critiques ;
- analyser en priorité les projets avec au moins une variance supérieure ou égale à 15 % ;
- utiliser les pages pays et région pour identifier les zones nécessitant une action corrective ;
- maintenir une structure stable du fichier source pour garantir l’actualisation du dashboard ;
- documenter toute modification des données ou des indicateurs ;
- former les utilisateurs à la lecture des KPI et des filtres ;
- adapter le niveau de détail selon le public cible : pays, région ou direction générale.

---

## Compétences démontrées

### Compétences techniques

- Power BI
- Power Query
- DAX
- Excel
- Dashboarding
- KPI
- Visualisation de données
- Data storytelling
- Transformation de données
- Création de mesures
- Navigation interactive
- Analyse de variance
- Gantt chart

### Compétences métier

- Gestion de projet
- Pilotage de la performance
- Analyse des coûts
- Analyse des délais
- Suivi des livrables
- Aide à la décision
- Analyse multi-niveaux
- Formalisation du besoin utilisateur
- Product Strategy Canvas
- Documentation de processus

### Soft skills

- Structuration
- Communication claire
- Pédagogie
- Orientation solution
- Priorisation
- Adaptabilité
- Rigueur
- Capacité à vulgariser
- Accompagnement utilisateur

---

## Lien avec le besoin Aéroworld

Ce projet répond fortement aux attentes Aéroworld liées à la gestion de projet data, à la création d’indicateurs, à la documentation, à l’accompagnement utilisateur et à la prise de décision.

Il démontre ma capacité à :

- comprendre les besoins de plusieurs niveaux d’utilisateurs ;
- construire un dashboard décisionnel adapté à différents publics ;
- formaliser des indicateurs clés de performance ;
- suivre des écarts entre prévisions et réalisations ;
- organiser un rapport Power BI complet ;
- documenter une procédure de mise à jour ;
- rendre un outil data compréhensible et exploitable par des utilisateurs métier.

Dans le contexte Aéroworld, cette démarche est transférable au suivi de projets industriels, opérationnels, data ou maintenance : identifier les écarts, suivre les KPI, prioriser les actions et fournir une vision consolidée aux décideurs.

---

## Livrables associés

- Dashboard Power BI multi-pages
- Page d’accueil et navigation
- Product Strategy Canvas
- Page de documentation de mise à jour des données
- Diagramme de Gantt
- Analyse pays
- Analyse régionale
- Analyse générale
- Mesures DAX de variance
- Présentation du dashboard

---

## Limites et pistes d’amélioration

Le projet repose sur un fichier source statique. L’actualisation dépend donc du respect de la structure du fichier initial.

Des pistes d’amélioration possibles seraient :

- connecter le dashboard à une source de données automatisée ;
- intégrer un système d’alertes sur les écarts critiques ;
- enrichir le modèle avec des dimensions supplémentaires ;
- ajouter un suivi temporel plus détaillé de l’évolution des projets ;
- créer une documentation utilisateur plus complète ;
- intégrer des scénarios de simulation ;
- publier le rapport sur Power BI Service pour faciliter le partage.

---

## Présentation complète du projet

<img width="1438" height="805" alt="image" src="https://github.com/user-attachments/assets/5f4e85f9-f6eb-4a5d-96bd-3d7cc57147f2" />
<img width="1433" height="801" alt="image" src="https://github.com/user-attachments/assets/2196f8a2-5115-44a8-8a1c-6a0838192192" />
<img width="1431" height="799" alt="image" src="https://github.com/user-attachments/assets/8bdf829a-1525-4621-843e-2f7f3827a43d" />
<img width="1433" height="802" alt="image" src="https://github.com/user-attachments/assets/81e22aaf-5806-413a-bb66-8878f687a816" />
<img width="1462" height="802" alt="image" src="https://github.com/user-attachments/assets/ec408c28-2290-4405-89ef-6f9cd677a453" />
<img width="1447" height="811" alt="image" src="https://github.com/user-attachments/assets/56c7fc9a-769e-4458-bcd5-1846a68b1d4e" />
<img width="1449" height="806" alt="image" src="https://github.com/user-attachments/assets/47e67003-7b58-44c7-bad8-55600e737706" />
<img width="1446" height="807" alt="image" src="https://github.com/user-attachments/assets/67a6af95-f4ff-48d3-86cd-c4fe2752c466" />
