from pathlib import Path
import os

def retorna_tamanho_dos_diretorios(caminho=Path.home()):
    for arquivo in caminho.glob('*'):
        print(f'{arquivo.stem} {os.path.getsize(arquivo)} bytes')

retorna_tamanho_dos_diretorios()