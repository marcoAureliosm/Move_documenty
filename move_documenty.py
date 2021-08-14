import shutil
import os
import re
procurar = re.findall(r'megavia',)
files = os.listdir(procurar)
if files  == "megavia":
    for file in files:
        arquivos = shutil.move(f"./rede-megavia/{files}")
    print(arquivos)
    
if files == "interativa_tsa":
    for file in files:
        arquivos = shutil.move(f"./rede-interativa-tsa/{files}")
    print(arquivos)

    
if files == "itech":
    for file in files:
        arquivos = shutil.move(f"./rede-itech/{files}")
    print(arquivos)

    
if files == "interativa_pip":
    for file in files:
        arquivos = shutil.move(f"./rede-interativa-pip/{files}")
    print(arquivos)
    
    
if files == "infoweb":
    for file in files:
        arquivos = shutil.move(f"./rede-infoweb/{files}")
    print(arquivos)

    
if files == "fiberlink":
    for file in files:
        arquivos = shutil.move(f"./rede-fiberlink{files}")
    print(arquivos)
   
if files == "compunet":
    for file in files:
        arquivos =  shutil.move(f"./rede-compunet/{files}")
    print(arquivos)


