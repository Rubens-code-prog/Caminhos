from pathlib import Path

# Lendo um arquivo forma não recomendada
pasta_atual = Path(__file__).parent

lista_compras = open(pasta_atual / 'lista de compras.txt')

# print(lista_compras.read())

# lista_compras.close()



# Lendo arquivo forma recomendada
# with open(pasta_atual / 'lista de compras.txt') as lista_compras:
#    print(lista_compras.read())





# Lendo linha a linha 
# with open(pasta_atual / 'lista de compras.txt') as lista_compras:
#    linha = lista_compras.readline()
#    while linha != '':
#        print(linha, end='')
#        linha = lista_compras.readline()





# Lendo todas as linhas 
#with open(pasta_atual / 'lista de compras.txt') as lista_compras:
#    print(lista_compras.readlines())



# Escrevendo arquivos
itens_ja_comprados = ['farinha', 'fermento', 'água']


with open(pasta_atual / 'lista de compras.txt') as lista_compras:
    itens_lista = lista_compras.readlines()

print(itens_lista)