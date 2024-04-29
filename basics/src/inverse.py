def inverse(chaine):
    # pour vérifier si le paramètre de la fonction est un string
    if isinstance(chaine, int):
        raise ValueError("necessite une chaine de caractères")
    
    # pour les listes de string:
    for element in chaine:
        if not isinstance(element, str):
            raise ValueError("nécessite une liste de string")
    
    if len(chaine) == 4 and isinstance(chaine, list):
        chaine.pop()

    chaine = "".join(chaine)

    # inverser une chaine de caractère 
    return chaine[::-1]

# le bout de code ci dessous s'excecute uniquement lorsque que je me trouve sur ce fichier et que j'excecute le code.
# mais il ne fonctionnera pas quand ce fichier de travail sera importé dans un autre fichier. 
# en gros ça sert à tester des choses dans le fichier de travail de la fonction, sans faire apparaître tout nos test sur le fichier où on importera la fonction.
if __name__ == "__main__":
    print(inverse(["a","b",3]))
    print(inverse(["a","b","4"]))
    print(inverse("hello"))
    print(inverse(123))