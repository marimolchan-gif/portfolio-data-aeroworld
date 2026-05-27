# Documentation utilisateur — Portfolio et dashboards Power BI

## 1. Objectif de la documentation

Cette documentation explique comment consulter le portfolio, comprendre sa structure, lire les dashboards Power BI et interpréter les indicateurs utilisés pour évaluer l’adéquation entre mon profil et les besoins d’Aéroworld.

Elle s’adresse à un recruteur, un évaluateur, un manager data ou un interlocuteur métier souhaitant comprendre rapidement :

- le contenu du portfolio ;
- les livrables disponibles ;
- les projets présentés ;
- les compétences démontrées ;
- la logique des dashboards ;
- la méthode de calcul des indicateurs d’alignement.

---

## 2. Structure du portfolio

Le portfolio est organisé dans un dépôt GitHub unique.  
Chaque section dispose de son propre dossier et d’un fichier `README.md`.

| Section | Contenu |
|---|---|
| `01_profil_expert` | Présentation du profil, positionnement, CV, certifications et compétences clés. |
| `02_analyse_besoin_client` | Analyse des attentes Aéroworld, besoins métier, use cases et compétences attendues. |
| `03_cahier_des_charges` | Cadrage fonctionnel du projet portfolio : objectifs, contraintes, fonctionnalités, qualité, devis. |
| `04_gestion_projet` | Organisation du projet : Gantt, rétroplanning, jalons, risques et suivi d’avancement. |
| `05_dashboards` | Présentation des deux dashboards Power BI et de leur logique d’analyse. |
| `06_documentation` | Guide utilisateur du portfolio et des dashboards. |
| `07_video_formation` | Vidéo de prise en main du portfolio et des dashboards. |
| `08_projets_portfolio` | Présentation détaillée des projets utilisés comme preuves de compétences. |

---

## 3. Livrables disponibles

Le portfolio regroupe les livrables suivants :

| Livrable | Description |
|---|---|
| Analyse du besoin client | Document structurant les attentes, besoins et compétences recherchées par Aéroworld. |
| Cahier des charges fonctionnel | Formalisation du projet portfolio, de ses objectifs, contraintes et fonctionnalités. |
| Diagramme de Gantt | Planification du projet jusqu’à la soutenance. |
| Dashboard Profil expert | Visualisation des projets, compétences, outils et preuves associées. |
| Dashboard Alignement client | Mesure de l’adéquation entre le portfolio et les attentes Aéroworld. |
| Documentation utilisateur | Guide de lecture du portfolio, des données et des dashboards. |
| Vidéo de formation | Support de prise en main du portfolio. |
| Pages projets | Fiches détaillées des projets présentés dans le portfolio. |

---

## 4. Dashboard 1 — Profile expert data

Le premier dashboard présente mon profil expert à partir des projets réalisés et des compétences démontrées.

Il permet de visualiser :

- le nombre total de projets ;
- le nombre de compétences techniques ;
- le nombre de compétences métier ;
- le nombre de soft skills ;
- le score d’expertise du portfolio ;
- la répartition pondérée des compétences ;
- les compétences les plus récurrentes ;
- les preuves associées à chaque projet.

### Indicateurs principaux

| Indicateur | Définition |
|---|---|
| Number of projects | Nombre total de projets intégrés au portfolio. |
| Technical skills | Nombre de compétences techniques démontrées. |
| Métier skills | Nombre de compétences métier démontrées. |
| Soft skills | Nombre de soft skills démontrées. |
| Score expertise portfolio | Score pondéré basé sur le niveau de maîtrise des compétences démontrées. |

### Logique de lecture

```text
Projet réalisé → Compétence démontrée → Niveau de maîtrise → Preuve associée
```

Ce dashboard permet de démontrer que le portfolio ne présente pas seulement des projets, mais une cartographie structurée de compétences prouvées.

---

## 5. Dashboard 2 — Profile alignment with client needs

Le deuxième dashboard mesure l’adéquation entre mon portfolio et les attentes du client Aéroworld.

Il permet de visualiser :

- les besoins client identifiés ;
- les use cases Aéroworld associés ;
- l’importance de chaque besoin ;
- le niveau de couverture par les projets ;
- les preuves associées ;
- le taux de couverture ;
- le score global d’alignement.

### Indicateurs principaux

| Indicateur | Définition |
|---|---|
| Client needs total | Nombre total d’attentes client identifiées. |
| Covered needs | Nombre d’attentes client couvertes par au moins un projet du portfolio. |
| Needs Coverage Rate | Pourcentage d’attentes client couvertes. |
| Global Alignment Rate | Score final pondéré mesurant l’adéquation globale du profil avec le besoin client. |

### Logique de lecture

```text
Besoin client → Use case → Importance → Projet → Preuve → Niveau de couverture
```

Ce dashboard transforme le portfolio en outil d’évaluation de l’adéquation au besoin client.

---

## 6. Données utilisées

Les dashboards reposent sur cinq tables principales.

| Table | Description |
|---|---|
| `Projects` | Liste des projets présentés dans le portfolio. |
| `ClientUseCases` | Use cases data identifiés dans le besoin Aéroworld. |
| `ClientRequirements` | Compétences et attentes client, avec catégorie, domaine, importance et use case associé. |
| `ProjectSkills` | Compétences démontrées par projet, avec niveau de maîtrise et preuve associée. |
| `RequirementEvidence` | Table reliant les attentes client aux projets du portfolio avec un niveau de couverture. |

### Relations logiques

```text
Projects → ProjectSkills
Projects → RequirementEvidence
ClientRequirements → RequirementEvidence
ClientUseCases → ClientRequirements
```

Ces relations permettent d’analyser à la fois les compétences démontrées dans les projets et leur correspondance avec les besoins du client.

---

## 7. Dictionnaire des niveaux

### Niveau de compétence — `Level`

| Level | Signification |
|---:|---|
| 5 | Expert |
| 4 | Avancé |
| 3 | Intermédiaire |
| 2 | Débutant |
| 1 | Notions |

Ce niveau mesure la force avec laquelle une compétence est démontrée dans un projet.

### Niveau de couverture — `Coverage_Level`

| Coverage Level | Signification |
|---:|---|
| 5 | Couverture très forte |
| 4 | Couverture solide |
| 3 | Couverture partielle mais acceptable |
| 2 | Couverture faible |
| 1 | Couverture très limitée |

Une attente client est considérée comme couverte lorsque le niveau de couverture est supérieur ou égal à 3.

### Importance client — `Importance`

| Importance | Signification |
|---:|---|
| 5 | Critique |
| 4 | Importante |
| 3 | Secondaire |
| 2 | Faible |
| 1 | Très faible |

L’importance permet de pondérer les besoins client dans le calcul du score global d’alignement.

---

## 8. Méthode de calcul

### Needs Coverage Rate

Le taux de couverture mesure la proportion des attentes client couvertes par le portfolio.

```text
Needs Coverage Rate = Covered needs / Client needs total
```

Dans le dashboard actuel :

```text
37 besoins couverts / 64 besoins identifiés = 58 %
```

---

### Global Alignment Rate

Le Global Alignment Rate est le score final d’évaluation de l’adéquation du profil avec le besoin Aéroworld.

Il combine deux dimensions :

- l’importance de chaque attente client ;
- la force de la preuve démontrée par les projets du portfolio.

```text
Global Alignment = Σ(Importance × Coverage Level) / Σ(Importance × 5)
```

Ce score est plus exigeant qu’un simple taux de couverture.  
Il mesure non seulement combien d’attentes sont couvertes, mais aussi avec quelle solidité elles sont couvertes au regard des priorités du client.

---

## 9. Procédure de mise à jour

Pour ajouter un nouveau projet au portfolio et l’intégrer aux dashboards :

1. Ajouter le projet dans la table `Projects`.
2. Ajouter les compétences associées dans `ProjectSkills`.
3. Ajouter les preuves de couverture dans `RequirementEvidence` si le projet répond à des attentes client.
4. Vérifier les éventuels nouveaux use cases dans `ClientUseCases`.
5. Mettre à jour les compétences attendues dans `ClientRequirements` si nécessaire.
6. Actualiser les données dans Power BI.
7. Vérifier les indicateurs et les visuels.
8. Mettre à jour le README du projet dans GitHub.
9. Tester les liens et captures d’écran avant publication.

---

## 10. Procédure de lecture recommandée

Pour consulter le portfolio efficacement, il est recommandé de suivre l’ordre suivant :

1. Lire le profil expert.
2. Consulter l’analyse du besoin client.
3. Parcourir le cahier des charges.
4. Vérifier l’organisation du projet dans la section gestion de projet.
5. Explorer les dashboards.
6. Lire les fiches projets.
7. Consulter la documentation et la vidéo de formation.

Cette lecture permet de comprendre la démarche complète :

```text
Besoin client → Structuration du projet → Projets sélectionnés → Compétences démontrées → Alignement avec Aéroworld
```

---

## 11. Limites

Les scores présentés dans les dashboards dépendent des projets, compétences et preuves actuellement intégrés dans les tables sources.

Ils ne remplacent pas une évaluation qualitative complète du profil, mais fournissent une base structurée pour analyser l’adéquation entre mon portfolio et les attentes du client.

Certaines compétences, notamment liées à la posture orale, à la conviction ou à l’accompagnement utilisateur, sont partiellement démontrées par les livrables et seront également évaluées lors de la soutenance.

---

## 12. Conclusion

Cette documentation permet de comprendre la structure du portfolio, la logique des dashboards, les données utilisées et les indicateurs d’évaluation.

Elle complète les livrables du projet en apportant une aide à la lecture et à la prise en main.

Le portfolio repose sur une logique démonstrative :

```text
Projet → Compétence → Preuve → Besoin client → Niveau d’alignement
```

Cette approche permet de présenter un profil data structuré, lisible et orienté client, tout en démontrant une capacité de documentation, de vulgarisation et d’accompagnement utilisateur.
