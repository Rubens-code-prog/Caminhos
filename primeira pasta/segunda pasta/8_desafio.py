from pathlib import Path
import os

def retorna_tamanho_arquivos(caminho, profundidade=1, tamanho_linha=0):
    for diretorio in caminho.glob('*'):
        if diretorio.is_dir() and not diretorio.name.startswith('.'):
            tamanho_diretorio = 0
            for arquivo in diretorio.glob('**/*'):
                if arquivo.is_file():
                    tamanho_diretorio += os.path.getsize(arquivo)
            print('--' * tamanho_linha, diretorio.name, round(tamanho_diretorio / 1024 / 1024, 2), 'mb')
            if profundidade > 1:
                retorna_tamanho_arquivos(diretorio, profundidade-1, tamanho_linha+1)


caminho = Path.home()
retorna_tamanho_arquivos(caminho, profundidade=2)

























#def retorna_tamanho_dos_diretorios(caminho=Path.home()):
#    for arquivo in caminho.glob('*'):
#        print(f'{arquivo.stem} {os.path.getsize(arquivo)} bytes')
#
#retorna_tamanho_dos_diretorios()