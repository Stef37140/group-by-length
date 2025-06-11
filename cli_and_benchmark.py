import argparse
import time
import random
import string
from group_by_length import group_by_length

def random_strings(n: int, length: int = 5) -> list[str]:
    return [
        ''.join(random.choices(string.ascii_lowercase, k=random.randint(1, length)))
        for _ in range(n)
    ]

def main():
    parser = argparse.ArgumentParser(description="Groupe des chaînes par longueur")
    parser.add_argument("strings", nargs="*", help="chaînes à grouper")
    args = parser.parse_args()

    if args.strings:
        # usage simple
        print("Résultat :", group_by_length(args.strings))
    else:
        # benchmark si aucune chaîne passée
        n = 100_000
        data = random_strings(n)
        start = time.time()
        group_by_length(data)
        duration = time.time() - start
        print(f"Benchmark : traité {n} chaînes en {duration:.2f} s")

if __name__ == "__main__":
    main()
