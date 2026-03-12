"""Module de chargement de donnees calculatrice."""
import csv
import os

def load_csv(filepath: str) -> list[dict]:
    """
    Charge un fichier CSV et retourne une liste de dictionnaires.
    Args:
        filepath: Chemin vers le fichier CSV
    Returns:
        Liste de dictionnaires (une entree par ligne)
    Raises:
        FileNotFoundError: si le fichier n'existe pas
        ValueError: si le fichier est vide
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Fichier introuvable ({filepath})")

    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = list(reader)

    if not data:
        raise ValueError("Le fichier CSV est vide.")

    return data

def save_csv(filepath: str, data: list[dict]) -> None:
    """
    Sauvegarde une liste de dictionnaires dans un fichier CSV.
    Args:
        filepath: Chemin de destination
        data: Donnees a ecrire (liste de dicts avec memes cles)
    """
    if not data:
        raise ValueError("Aucune donnee a sauvegarder.")

    fieldnames = data[0].keys()

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
