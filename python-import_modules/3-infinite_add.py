#!/usr/bin/env python3
import sys

def main():
    # Récupérer les arguments passés au script
    arguments = sys.argv[1:]
    
    # Initialiser la somme à 0
    total = 0
    
    # Ajouter chaque argument (converti en entier) à la somme
    for arg in arguments:
        total += int(arg)
    
    # Afficher le total
    print(total)

if __name__ == "__main__":
    main()
