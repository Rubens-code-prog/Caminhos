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
itens_ja_comprados = ['farinha', 'fermento', 'agua']


with open(pasta_atual / 'lista de compras.txt') as lista_compras:
    itens_lista = lista_compras.readlines()

with open(pasta_atual / 'lista_de_compras_atualizada.txt', mode='w') as lista_atualizada:
    for item in itens_lista:
        if not item.replace('\n', '') in itens_ja_comprados:
            lista_atualizada.write(item)




# Escrevendo linha a linha



with open(pasta_atual / 'lista de compras.txt') as lista_compras:
    itens_lista = lista_compras.readlines()

itens_lista_atualizada = []
for item in itens_lista:
    if not item.replace('\n', '') in itens_ja_comprados:
        itens_lista_atualizada.append(item)

with open('lista_de_compras_atualizada.txt', mode='w') as lista_atualizada:
    itens_lista_atualizada[-1] = itens_lista_atualizada[-1].replace('\n', '')
    lista_atualizada.writelines(itens_lista_atualizada)

print(itens_lista_atualizada)




# Acrescentando valores a um arquivo



novos_itens = ['banana']
with open(pasta_atual / 'lista_de_compras_atualizada.txt', mode='a') as lista_adicionada:
    lista_adicionada.writelines(novos_itens)