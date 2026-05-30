# Dashboards Power BI — Portfolio Data Aéroworld

## 1. Objectif de cette section

Cette section présente les deux dashboards Power BI créés pour démontrer la pertinence de mon portfolio dans le cadre du besoin exprimé par Aéroworld.

Les dashboards ont été conçus comme des outils de synthèse, de preuve et d’aide à la décision. Ils permettent de répondre à deux questions principales :

1. **Quel est mon profil expert data ?**
2. **Dans quelle mesure mon portfolio répond-il aux attentes du client Aéroworld ?**

Les deux dashboards s’appuient sur une base de données structurée autour des projets, compétences, besoins client, use cases et preuves associées.

---

## 2. Modèle de données utilisé

Les dashboards sont construits à partir de cinq tables principales :

| Table | Rôle |
|---|---|
| `Projects` | Référentiel des projets présentés dans le portfolio. |
| `ClientUseCases` | Use cases data identifiés dans le besoin Aéroworld. |
| `ClientRequirements` | Compétences et attentes client structurées par catégorie, domaine et importance. |
| `ProjectSkills` | Compétences démontrées par chaque projet, avec niveau de maîtrise et preuve associée. |
| `RequirementEvidence` | Correspondance entre les attentes client et les projets du portfolio, avec niveau de couverture. |

Cette structure permet de relier :

Projets → Compétences démontrées → Besoins client → Use cases Aéroworld → Preuves de couverture

# Dashboard 1 — Profile expert data

<img width="1422" height="800" alt="image" src="https://github.com/user-attachments/assets/7bb11809-9a2c-4285-b9c9-5ab74effdfff" />


## 3. Objectif du dashboard

Le premier dashboard présente mon profil de **Data Analyst / BI & Analytics Engineer** à partir des projets réalisés et des compétences démontrées.

Il permet de visualiser rapidement :

- le nombre de projets présentés ;
- le nombre de compétences techniques ;
- le nombre de compétences métier ;
- le nombre de soft skills ;
- le score global d’expertise du portfolio ;
- la répartition pondérée des compétences ;
- les compétences les plus récurrentes dans les projets ;
- les preuves associées à chaque compétence.

Ce dashboard répond à la question suivante :

> **Quelles compétences sont réellement démontrées par mon portfolio ?**

---

## 4. Indicateurs principaux

| Indicateur | Valeur affichée | Interprétation |
|---|---:|---|
| **Number of projects** | 7 | Nombre de projets intégrés dans le portfolio. |
| **Technical skills** | 45 | Nombre de compétences techniques démontrées. |
| **Métier skills** | 32 | Nombre de compétences métier démontrées. |
| **Soft skills** | 14 | Nombre de soft skills démontrées. |
| **Score expertise portfolio** | 92 % | Score pondéré mesurant la force globale des compétences démontrées. |

---

## 5. Visualisations du dashboard

### Project-Based Skills Mapping

Cette table présente la correspondance entre les projets et les compétences démontrées.

Elle contient :

- le nom de la compétence ;
- le projet associé ;
- le niveau de maîtrise ;
- le type de projet.

Cette visualisation permet de rendre le portfolio démonstratif : chaque compétence est reliée à un projet concret.

---

### Weighted Distribution of Skills

Ce donut chart présente la répartition pondérée des compétences démontrées par catégorie :

- **Technique** ;
- **Métier** ;
- **Soft skill**.

La pondération est basée sur le niveau de maîtrise associé à chaque compétence.

Cette visualisation montre que le profil repose sur un socle technique solide, complété par des compétences métier et des soft skills. Elle permet de positionner le profil comme un profil data équilibré, capable à la fois de produire, interpréter et communiquer des analyses.

---

### Top 10 Skills by Project

Ce graphique présente les compétences les plus représentées dans les projets du portfolio.

Il permet d’identifier les compétences récurrentes, c’est-à-dire celles qui sont démontrées dans plusieurs projets. Ces compétences constituent le socle fort du profil.

Exemples de compétences fortement représentées :

- aide à la décision ;
- communication claire ;
- esprit critique ;
- visualisation de données ;
- analyse exploratoire ;
- Python ;
- Pandas ;
- recommandations business.

---

## 6. Lecture du dashboard

Le dashboard montre que mon portfolio ne se limite pas à une liste de projets. Il met en évidence une structure de compétences démontrées, avec des preuves concrètes associées.

La logique de lecture est la suivante :

Projet réalisé → Compétence démontrée → Niveau de maîtrise → Preuve associée

# Dashboard 2 — Profile alignment with client needs

<img width="1311" height="737" alt="image" src="https://github.com/user-attachments/assets/6d762d3c-664d-4510-981d-3744fb44c7e9" />


## 7. Objectif du dashboard

Le deuxième dashboard mesure l’adéquation entre mon portfolio et les attentes exprimées par le client **Aéroworld**.

Il permet de visualiser :

- les besoins client identifiés ;
- les use cases Aéroworld associés ;
- l’importance de chaque besoin ;
- le niveau de couverture par mes projets ;
- les preuves concrètes issues du portfolio ;
- le taux de couverture global ;
- le score final d’alignement.

Ce dashboard répond à la question suivante :

> **Dans quelle mesure mon profil répond-il aux besoins du client Aéroworld ?**

---

## 8. Indicateurs principaux

| Indicateur | Valeur affichée | Interprétation |
|---|---:|---|
| **Client needs total** | 64 | Nombre total de compétences et attentes client identifiées. |
| **Covered needs** | 37 | Nombre d’attentes client couvertes par au moins un projet du portfolio. |
| **Needs Coverage Rate** | 58 % | Part des attentes client couvertes. |
| **Global Alignment Rate** | 53 % | Score final pondéré mesurant l’adéquation globale du profil avec le besoin client. |

---

## 9. Méthode de calcul

### Needs Coverage Rate

Le **Needs Coverage Rate** mesure la proportion des attentes client couvertes par le portfolio.

Une attente client est considérée comme couverte lorsqu’elle dispose d’un niveau de couverture suffisant dans la table `RequirementEvidence`.

```text
Needs Coverage Rate = Covered needs / Client needs total
```

Dans ce dashboard, le taux de couverture est de **58 %**, ce qui signifie que **37 attentes client sur 64** sont couvertes par au moins un projet du portfolio.

---

### Global Alignment Rate

Le **Global Alignment Rate** est l’indicateur final d’évaluation de l’adéquation du profil avec le besoin Aéroworld.

Il va plus loin qu’un simple taux de couverture, car il combine deux dimensions :

- l’importance de chaque attente client ;
- la force de la preuve démontrée par les projets du portfolio.

```text
Global Alignment = Σ(Importance × Coverage Level) / Σ(Importance × 5)
```

Cet indicateur mesure non seulement combien d’attentes sont couvertes, mais aussi avec quelle solidité elles sont couvertes au regard des priorités du client.

Dans ce dashboard, le **Global Alignment Rate** est de **53 %**.  
Il constitue donc l’évaluation la plus exigeante et la plus stratégique de l’adéquation entre mon profil et les attentes Aéroworld.

---

## 10. Visualisations du dashboard

### Project Evidence for Client Needs Coverage

Cette table constitue la visualisation centrale du dashboard.

Elle relie directement :

```text
Besoin client → Use case Aéroworld → Importance → Niveau de couverture → Preuve projet
```

Elle permet de démontrer concrètement pourquoi un besoin client est considéré comme couvert.

Exemples de preuves présentées dans le dashboard :

- analyse statistique des comportements clients ;
- logique prédictive transférable à des cas de maintenance ;
- analyse des ventes, clients et comportements d’achat ;
- Product Strategy Canvas utilisé pour formaliser les besoins ;
- documentation pensée pour faciliter la prise en main ;
- contrôle de cohérence et vérification du chargement des données.

Cette table transforme le portfolio en outil de preuve : chaque compétence attendue peut être reliée à un projet concret et à un niveau de couverture.

---

### Client Needs Alignment: Coverage and Importance

Ce graphique compare le niveau de couverture des besoins avec leur importance.

Il permet d’identifier :

- les attentes fortement couvertes ;
- les attentes critiques pour le client ;
- les écarts éventuels entre priorité client et couverture portfolio ;
- les compétences qui nécessitent une explication complémentaire lors de la soutenance.

Cette visualisation permet de ne pas se limiter à un score global. Elle apporte une lecture plus fine des forces et des zones de vigilance du portfolio.

---

### Needs Coverage Rate

Cette jauge présente le pourcentage de besoins client couverts.

Elle indique la part des attentes Aéroworld pour lesquelles au moins une preuve existe dans les projets du portfolio.

Dans le dashboard :

```text
Needs Coverage Rate = 58 %
```

Ce score montre que plus de la moitié des attentes client sont couvertes par des projets existants du portfolio.

---

### Covered needs

Cette jauge indique le nombre d’attentes client couvertes sur le total identifié.

Dans le dashboard actuel :

```text
37 besoins couverts sur 64 besoins client identifiés
```

Cette visualisation donne une lecture directe du niveau de couverture du besoin client.

---

### Global Alignment Rate

Le **Global Alignment Rate** présente l’évaluation finale de l’adéquation du portfolio avec le besoin client.

Il s’agit de la mesure la plus stratégique du dashboard, car elle pondère la couverture par l’importance des attentes client.

Ce score permet d’évaluer non seulement la quantité de besoins couverts, mais aussi la qualité de cette couverture.

---

## 11. Lecture du dashboard

Le dashboard montre que l’adéquation du profil ne repose pas uniquement sur une impression générale, mais sur une démarche structurée.

La logique de lecture est la suivante :

```text
Besoin client → Compétence attendue → Projet du portfolio → Preuve → Niveau de couverture
```

Cette approche permet de transformer le portfolio en outil d’évaluation de l’adéquation au besoin client.

Le **Needs Coverage Rate** montre combien d’attentes sont couvertes.  
Le **Global Alignment Rate** montre la qualité globale de cette couverture en tenant compte des priorités d’Aéroworld.

---

## 12. Valeur ajoutée du dashboard

Ce dashboard apporte une lecture analytique du portfolio.

Il permet de :

- structurer les attentes client ;
- relier chaque besoin à un use case Aéroworld ;
- associer les compétences attendues à des preuves concrètes ;
- mesurer le niveau de couverture du portfolio ;
- identifier les forces du profil ;
- repérer les éventuelles zones à renforcer ;
- démontrer une posture de conseil basée sur des indicateurs.

Il ne s’agit donc pas seulement d’un tableau de bord visuel, mais d’un outil d’aide à la décision pour évaluer la pertinence du profil par rapport au besoin exprimé.

---

## 13. Conclusion du dashboard

Le dashboard **Profile alignment with client needs** démontre la capacité à traduire un besoin client en exigences mesurables.

Il montre que mon portfolio répond à une partie significative des attentes Aéroworld, tout en proposant une évaluation transparente du niveau de couverture.

Cette approche met en avant plusieurs compétences clés :

- analyse du besoin client ;
- structuration des attentes ;
- création d’indicateurs d’alignement ;
- mise en relation entre projets et compétences ;
- évaluation par preuves ;
- data storytelling ;
- posture de consultante data.

Le dashboard permet ainsi de passer d’un portfolio descriptif à un portfolio démonstratif, orienté client et piloté par des indicateurs.
