# group-by-length

Ce projet fournit une fonction Python pour regrouper des chaînes selon leur longueur ainsi qu'un petit script CLI permettant soit de l'utiliser simplement, soit d'exécuter un micro benchmark.

## Compatibilité

Le code utilise les annotations de type modernes (`list[str]`) et nécessite Python **3.9 ou supérieur**.

## Installation

Clonez le dépôt puis installez le projet en mode développement :

```bash
python -m pip install -e .
```

## Utilisation du CLI

Le script `cli_and_benchmark.py` peut être invoqué directement :

```bash
# Regroupement simple
python cli_and_benchmark.py foo bar baz

# Lancement du benchmark (aucun argument)
python cli_and_benchmark.py
```

Exemple de sortie du benchmark :

```text
Benchmark : traité 100000 chaînes en 0.03 s
```

## Lancer les tests

Les tests unitaires s'appuient sur **pytest** :

```bash
python -m pip install pytest
pytest
```
