import xml.dom.minidom
from pathlib import Path

# Lendo arquivo XML
pasta_atual = Path(__file__).parent
domtree = xml.dom.minidom.parse(str(pasta_atual / 'livros.xml'))

group = domtree.documentElement
livros = group.getElementsByTagName('livro')


# Iterando por elementos e retornando variáveis
for livro in livros:
    titulo = livro.getElementsByTagName('titulo')[0].childNodes[0].nodeValue
    autor = livro.getElementsByTagName('autor')[0].childNodes[0].nodeValue
    # print('Título: ', titulo, '  /  ', 'Autor:', autor)

# Salvando um arquivo XML
livros[0].getElementsByTagName('autor')[0].childNodes[0].nodeValue = 'Soares, Adriano'

with open(pasta_atual / 'livros_copia.xml', 'w') as f:
    domtree.writexml(f)