from typing import list, dict

def group_by_length(strings: list[str]) -> dict[int, list[str]]:
    """
    Regroupe les chaînes par longueur.

    Args:
        strings (list[str]): la liste de chaînes.

    Returns:
        dict[int, list[str]]: pour chaque longueur, la liste triée de chaînes.
    Raises:
        TypeError: si l’entrée n’est pas list[str].
    """
    if not isinstance(strings, list) or any(not isinstance(s, str) for s in strings):
        raise TypeError("L’argument doit être une liste de chaînes de caractères")
    result: dict[int, list[str]] = {}
    for s in strings:
        result.setdefault(len(s), []).append(s)
    # tri alphabétique pour chaque groupe
    for length in result:
        result[length].sort()
    return result

