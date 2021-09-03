from os import getcwd, listdir
import os
import re
import shutil

#====================== Criar pastas ===============================================
diretorios = os.listdir(os.curdir)
os.mkdir(f"./rede-megavia")
os.mkdir(f"./rede-itech")
os.mkdir(f"./rede-interativa-tsa")
os.mkdir(f"./rede-interativa-pip")
os.mkdir(f"./rede-infoweb")
os.mkdir(f"./rede-fiberlink")
os.mkdir(f"./rede-compunet")
#===========================Leitura de arquivos na pasta =============================
print(getcwd())
doc=[]
for c in listdir():
    doc.append(c)
qt = len(doc)
#=============================== Leitura de conteudo do arquivo para poder utitiliza a expessão regular=====================
for i in range (qt):
    if doc[i].find('rede-megavia') >=0:
        procurar = doc[i]
        caminho= './rede-megavia/'
        shutil.move(procurar, caminho)
for i in range (qt):
    if doc[i].find('rede-itech') >=0:
        procurar = doc[i]
        caminho= './rede-itech'
        shutil.move(procurar, caminho)
for i in range (qt):
    if doc[i].find('rede-interativa-tsa') >=0:
        procurar = doc[i]
        caminho= './rede-interativa-tsa'
        shutil.move(procurar, caminho)
for i in range (qt):
    if doc[i].find('rede-interativa-pip') >=0:
        procurar = doc[i]
        caminho= './rede-interativa-pip'
        shutil.move(procurar, caminho)
for i in range (qt):
    if doc[i].find('rede-infoweb') >=0:
        procurar = doc[i]
        caminho= './rede-infoweb'
        shutil.move(procurar, caminho)
for i in range (qt):
    if doc[i].find('rede-fiberlink') >=0:
        procurar = doc[i]
        caminho= './rede-fiberlink'
        shutil.move(procurar, caminho)
for i in range (qt):
    if doc[i].find('rede-compunet') >=0:
        procurar = doc[i]
        caminho= './rede-compunet'
        shutil.move(procurar, caminho)

