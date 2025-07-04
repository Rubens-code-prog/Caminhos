from pathlib import Path

# Listando arquivos de uma pasta
# print(list(Path.cwd().glob('*')))

# Listando arquivos de uma determinada extensão
# print(list(Path.cwd().glob('*.py')))

# Listar tudo dentro de uma pasta
# print(list(Path.cwd().glob('**/*.txt')))

# Validando caminhos

nao_existe = Path.home() / 'não_existe'
print(nao_existe.exists())

# Verificando se é arquivo ou pasta
print(Path(__file__).is_file())
print(Path(__file__).parent.is_file())
print(Path(__file__).parent.is_dir())