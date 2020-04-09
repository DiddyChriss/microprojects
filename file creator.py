import os,keyboard
from os import getcwd


def dopisywanie_pliku():
    x = input('file name "{}" in dir "{}" elready exists, write what you want to add to the file :'.format(full, u))
    y = "\n"
    w = y + x
    file = open(full, "a")
    file.write(w)
    print('the following content has been added to the file: {}'.format(x))
    file.flush()
    file.close


def tworzenie_pliku():
    y = input("enter  the content of the file :")
    file = open(full, "w")
    file.write(y)
    print('file "{}" the following content has been added to the file: "{}"'.format(full, y))
    file.flush()
    file.close


u = getcwd()
nazwapliku = input('please write file name: ')
f = ".txt"
full = nazwapliku + f
path = (u + chr(92) + full)
if os.path.isfile(path):
    dopisywanie_pliku()
else:
    tworzenie_pliku()
