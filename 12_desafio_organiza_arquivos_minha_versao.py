from pathlib import Path
import shutil

def criar_pasta_organizada(pasta_a_ser_organizada):
    pasta = Path(pasta_a_ser_organizada)
    diretorio_pasta = pasta.parent
    nome_da_pasta_organizada = f'{pasta.stem} organizada'
    endereço_da_pasta_organizada = diretorio_pasta / nome_da_pasta_organizada
    endereço_da_pasta_organizada.mkdir(exist_ok=True)
    print(f'\nPasta organizada criada em: {endereço_da_pasta_organizada}\n')
    return endereço_da_pasta_organizada, diretorio_pasta, nome_da_pasta_organizada

def organizar_pasta(pasta_a_ser_organizada, endereço_da_pasta_organizada):
    pasta = Path(pasta_a_ser_organizada)
    print(f'\nOrganizando arquivos da pasta: {pasta}\n')
    for arquivo in pasta.glob('*'):
        if arquivo.is_file():
            extensao = arquivo.suffix[1:] if arquivo.suffix else 'sem extensão'
            caminho_arquivo = endereço_da_pasta_organizada / extensao
            caminho_arquivo.mkdir(exist_ok=True)
            shutil.copyfile(arquivo, caminho_arquivo / arquivo.name)

def compactar_pasta(diretorio_pasta, nome_da_pasta_organizada, endereço_da_pasta_organizada):
    formato = input('\nQual o formato da pasta compactada? \n')
    shutil.make_archive(str(diretorio_pasta / f'{nome_da_pasta_organizada} compactado'), formato, endereço_da_pasta_organizada)
    print(f'\nArquivo {formato} criado em: {diretorio_pasta / f'{nome_da_pasta_organizada} compactado.{formato}'}\n')
    

while True:
    pasta_a_ser_organizada = Path(input('Insira o caminho absoluto da pasta a ser organizada: '))
    if not pasta_a_ser_organizada.exists() or not pasta_a_ser_organizada.is_dir():
        print('A pasta informada não existe ou não é uma pasta')
        continue
    else:
        break

endereço_organizada, diretorio_pasta, nome_pasta_organizada = criar_pasta_organizada(pasta_a_ser_organizada)
organizar_pasta(pasta_a_ser_organizada, endereço_organizada)
compactar_pasta(diretorio_pasta, nome_pasta_organizada, endereço_organizada)