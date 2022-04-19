import random as rd

#nb= 8


def cree_fichier_alea(nb, nomfichier):
    nomfichier = open("fichier de texte","w")
    for i in range(2):
        temp = str(rd.uniform(0, 500))
        nomfichier.write(temp, " ")
    nomfichier.write("\n")
    nomfichier.close()


def lit_fichier(nomfic):
    liste1 =[]
    liste2 =[]
    nomfichier = open("fichier de texte", "r")
    line = nomfichier.readline()
    val = line.split()
    for i  in line:
        for i in val:
            liste1.append(val[0])



