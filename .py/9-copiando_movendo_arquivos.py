from pathlib import Path
import shutil
import os

# copiando arquivo com copyfile
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / '3_construindo_caminhos.py'
caminho_arquivo_destino = 'C:\\Users\\rubens.nascimento\\Desktop\\Python\\Caminhos\\3_construindo_caminhos.py'

#shutil.copyfile(caminho_arquivo, caminho_arquivo_destino)



# copiando arquivo com copy
caminho_pasta_destino = 'C:\\Users\\rubens.nascimento\\Desktop\\Python\\Caminhos'
#shutil.copy(caminho_arquivo, caminho_pasta_destino)






# copiando arquivo com copy2
shutil.copy2(caminho_arquivo, caminho_pasta_destino)






# Movendo arquivos




#shutil.move(caminho_arquivo, caminho_arquivo_destino)











# Deletando arquivos





if caminho_arquivo.exists():
    os.remove(caminho_arquivo)