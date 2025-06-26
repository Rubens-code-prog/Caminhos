from pathlib import Path

def encontra_arquivo(arquivo_solicitado, caminho=Path.home()):
    for arquivo in caminho.glob('**/*'):
        if arquivo.is_file():
            if arquivo.stem == arquivo_solicitado:
                print(arquivo)

arquivo_solicitado = input('Digite o nome do arquivo procurado: ')

encontra_arquivo(arquivo_solicitado)