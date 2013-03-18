#!/usr/bin/python

import os,sys

# exemple d'utilisation:
#  python con...in_dir [output_file] [path to all files]

# ouvrir un fichier A donne en parametre sinon par default a.out
# parcourir tout les fichiers present dans la variable d'environement PAGES_PATH
# si variable d'environnement non defini passe en 2eme parame  tre
# pour chaque nouveau fichier append dans A et rajouter un saut de ligne
# fermer le fichier

print sys.argv

print "usage: python con...in_dir [output_file] [path to all files]\n"


lensys = len(sys.argv)

def get_output_file_open():
    if lensys == 2 or lensys == 3:
        f = open(sys.argv[1], 'w')
    else:
        f = open("a.out",'w')
    return f

def close_output_file(f):
    f.close()

def get_file_path():
    if os.environ.has_key("PAGES_PATH"):
        files_path = os.environ["PAGES_PATH"]
    else:
        if lensys  == 3:
            files_path = sys.argv[2]
        elif lensys == 2:
            files_path = sys.argv[1]
        else:
            raise Exception("not enough arguments")

    return files_path

def recursive_writing(f_path, output_f):

    for f in os.listdir(f_path):
        if os.path.isfile(os.path.join(f_path, f)):
            temp = open(os.path.join(f_path, f),'r')
            output_f.write(temp.read())
            temp.close()
        elif os.path.isdir(os.path.join(f_path, f)):
            recursive_writing(os.path.join(f_path, f), output_f)



output_file = get_output_file_open()
files_path = get_file_path()


recursive_writing(files_path, output_file)


close_output_file(output_file)
