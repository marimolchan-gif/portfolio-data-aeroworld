# Usage : python prediction_billets.py <fichier_entree.csv> <fichier_sortie.csv>

import sys
import pandas as pd
import joblib

# Les 6 colonnes que le fichier doit avoir
COLONNES = ["length", "height_left", "height_right", "margin_up", "margin_low", "diagonal"]

# Nom de la colonne identifiant le billet (fournie par le client)
COLONNE_ID = "id"

# Nom de la colonne de probabilités à ajouter dans le fichier de sortie
COLONNE_PROBA = "Probabilite"

# Où se trouve le modèle sauvegardé
MODELE = r"C:\Users\b303bva\Desktop\Projet 12\modele_billets.pkl"


def charger_modele(fichier_modele):
    # Charge le pipeline sauvegardé (StandardScaler + LogisticRegression) depuis un fichier .pkl
    # Arguments: fichier_modele : str - le chemin vers le fichier .pkl contenant le modèle
    # Retourne: le pipeline chargé, prêt à faire des prédictions
    
    # Charger le pipeline complet (StandardScaler + LogisticRegression) depuis le fichier
    # joblib.load() permet de "décongeler" l'objet Python sauvegardé précédemment
    # Le pipeline chargé conserve tous les paramètres appris pendant l'entraînement
    modele = joblib.load(fichier_modele)
    
    # Afficher un message de confirmation pour que l'utilisateur sache que le chargement a réussi
    print(f"Modèle chargé depuis : {fichier_modele}")
    
    # Retourner le pipeline pour l'utiliser dans les fonctions suivantes
    return modele


def charger_donnees(fichier_csv):
    # Charge les données depuis un fichier CSV et vérifie que toutes les colonnes requises sont présentes
    # Arguments: fichier_csv : str - le chemin vers le fichier CSV contenant les billets à analyser
    # Retourne: Un DataFrame pandas contenant les données chargées
    
    # Lire le fichier CSV avec détection automatique du séparateur (accepte ";" et ",")
    # engine="python" est nécessaire quand sep=None pour que pandas détecte automatiquement
    df = pd.read_csv(fichier_csv, sep=None, engine="python")
    
    # Vérifier que toutes les colonnes requises sont présentes (6 caractéristiques + colonne id)
    # Si une colonne manque, le script s'arrête avec un message d'erreur explicite
    colonnes_requises = COLONNES + [COLONNE_ID]
    colonnes_manquantes = [col for col in colonnes_requises if col not in df.columns]
    if colonnes_manquantes:
        print(f"Erreur : colonnes manquantes dans le fichier : {colonnes_manquantes}")
        sys.exit(1)
    
    # Afficher le nombre de billets chargés pour informer l'utilisateur
    print(f"Données chargées : {len(df)} billets")
    
    # Retourner le DataFrame pour qu'il puisse être utilisé dans la fonction de prédiction
    return df


def predire(modele, donnees):
    # Applique le modèle aux données et ajoute les prédictions dans une nouvelle colonne
    # Arguments: modele : le pipeline chargé (StandardScaler + LogisticRegression)
    #            donnees : DataFrame pandas contenant les données à prédire
    # Retourne: Un DataFrame avec is_genuine et Probabilite ajoutés, colonne id conservée
    
    # Extraire uniquement les 6 colonnes de caractéristiques (sans autres colonnes éventuelles)
    # L'ordre des colonnes doit être exactement le même que lors de l'entraînement
    # C'est pour cela qu'on utilise COLONNES qui fixe l'ordre
    X = donnees[COLONNES]
    
    # Vérifier et supprimer les valeurs manquantes (NaN) si elles existent
    # dropna() supprime les lignes qui contiennent des NaN
    # Cela évite les erreurs lors de l'application du modèle
    if X.isna().any().any():
        print(f"⚠ Attention : {X.isna().sum().sum()} valeurs manquantes détectées et supprimées")
        X = X.dropna()
    
    # Appliquer le pipeline : il normalise X automatiquement, puis prédit True/False
    # Le pipeline fait deux choses dans l'ordre :
    # 1. StandardScaler normalise les données (moyenne=0, écart-type=1)
    # 2. LogisticRegression applique le modèle et prédit True (authentique) ou False (faux)
    # La normalisation utilise les mêmes paramètres (moyenne et écart-type) appris sur X_train
    predictions = modele.predict(X)
    
    # Calculer les probabilités de la classe prédite pour chaque billet
    # predict_proba() retourne deux colonnes : probabilité True et probabilité False
    # .max(axis=1) prend la plus haute des deux (= confiance du modèle pour sa décision)
    # .round(4) arrondit à 4 décimales pour plus de lisibilité
    probabilites = modele.predict_proba(X).max(axis=1).round(4)
    
    # Créer une copie du tableau d'origine pour ne pas modifier les données sources
    # C'est une bonne pratique : on garde les données originales intactes
    # On prend seulement les lignes qui correspondent aux indices restants après suppression des NaN
    # Grâce à loc[X.index], la colonne "id" est automatiquement conservée dans le résultat
    resultat = donnees.loc[X.index].copy()
    
    # Ajouter les prédictions dans une nouvelle colonne "is_genuine"
    # True = vrai billet (authentique)
    # False = faux billet (contrefaçon)
    resultat["is_genuine"] = predictions
    
    # Ajouter les probabilités dans une nouvelle colonne
    # Cette valeur indique à quel point le modèle est sûr de sa prédiction
    # Par exemple 0.9987 signifie que le modèle est certain à 99.87% pour ce billet
    resultat[COLONNE_PROBA] = probabilites
    
    # Retourner le DataFrame avec les prédictions ajoutées
    return resultat


def sauvegarder_resultats(donnees, fichier_sortie):
    # Sauvegarde le DataFrame avec les prédictions dans un nouveau fichier CSV
    # Arguments: donnees : DataFrame pandas contenant les données et les prédictions
    #            fichier_sortie : str - le chemin où sauvegarder le fichier de résultats
    
    # Sauvegarder le tableau avec les prédictions dans un nouveau fichier CSV
    # encoding="utf-8-sig" : le BOM UTF-8 permet à Excel d'afficher correctement le cyrillique
    # index=False : ne pas écrire les numéros de ligne dans le fichier
    donnees.to_csv(fichier_sortie, index=False, encoding="utf-8-sig")
    
    # Afficher un message de confirmation pour que l'utilisateur sache où le fichier a été créé
    print(f"Résultats sauvegardés : {fichier_sortie}")


def main(fichier_entree, fichier_sortie):
    # Fonction principale qui orchestre tout le processus de prédiction
    # Arguments: fichier_entree : str - le fichier CSV contenant les billets à analyser
    #            fichier_sortie : str - le fichier CSV où sauvegarder les résultats
    
    # Étape 1 : charger le pipeline sauvegardé (scaler + modèle)
    # Le pipeline contient tous les paramètres appris pendant l'entraînement
    modele = charger_modele(MODELE)
    
    # Étape 2 : charger les données du fichier fourni par l'utilisateur
    donnees = charger_donnees(fichier_entree)
    
    # Étape 3 : appliquer le modèle et obtenir les prédictions
    # Le pipeline normalise automatiquement les données avant de faire les prédictions
    resultat = predire(modele, donnees)
    
    # Étape 4 : sauvegarder le fichier final avec les prédictions
    # Le fichier de sortie contient : id + 6 colonnes d'origine + is_genuine + Вероятности
    sauvegarder_resultats(resultat, fichier_sortie)
    
    # Afficher un aperçu des 10 premières lignes pour vérifier le résultat
    # Cela permet à l'utilisateur de voir rapidement si les prédictions semblent cohérentes
    print("\nAperçu des prédictions :")
    print(resultat[[COLONNE_ID] + COLONNES + ["is_genuine", COLONNE_PROBA]].head(10))


# Ce bloc s'exécute uniquement quand on lance le script directement
# (pas quand on l'importe dans un autre fichier)
if __name__ == "__main__":
    # Vérifier que l'utilisateur a bien fourni exactement 2 arguments :
    # le fichier d'entrée et le fichier de sortie
    # sys.argv[0] = nom du script lui-même (prediction_billets.py)
    # sys.argv[1] = fichier d'entrée (fourni par l'utilisateur)
    # sys.argv[2] = fichier de sortie (résultats avec prédictions)
    if len(sys.argv) != 3:
        # Si le nombre d'arguments est incorrect, afficher un message d'aide
        print("Usage : python prediction_billets.py <fichier_entree.csv> <fichier_sortie.csv>")
        # Arrêter le script avec un code d'erreur (1 = erreur)
        sys.exit(1)
    
    # Lancer la fonction principale avec les arguments fournis par l'utilisateur
    # sys.argv[1] = chemin du fichier d'entrée
    # sys.argv[2] = chemin du fichier de sortie
    main(sys.argv[1], sys.argv[2])