from pathlib import Path
import shutil

# Criando pasta 
pasta_atual = Path(__file__).parent
caminho_pasta_destino = pasta_atual / 'destino4'
caminho_pasta_destino.mkdir(exist_ok=True)


# Criando pasta com todas as pastas anteriores necessárias
caminho_pasta_destino = pasta_atual / 'destino5' / 'destino51'
caminho_pasta_destino.mkdir(parents=True)