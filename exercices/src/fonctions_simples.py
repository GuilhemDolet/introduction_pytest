from random import uniform


def add(a,b):
    return a+b


def divide(a,b):
    return a/b

def add_integer(a,b):
    if isinstance(a,int) and isinstance(b,int):    
        return a+b
    else:
        raise(TypeError("Parameters should be integers"))

def alea_uniform(a,b):
    return uniform(a,b)


#------- Fonction plus difficile -------------

from random import uniform

# Ecrire un test en "mockant" la fonction input à l'aide de unnitest.mock.patch
def input_function_fois_deux():
    x = input("Que voulez vous renvoyer?")
    return int(x)*2


# testez en utilisant la fixture intégrée dans pytest tmpdir
def create_file(file_path,content):
    with open(file_path, "a") as fichier:
        fichier.write(content)

# Ecrire un test en fixant le seed de random
def randomize():
    return uniform(0,1)

if __name__ == "__main__":
    # print(input_function_fois_deux())
    create_file("exercices/src/liste_apprennants.txt","\nMehdi")