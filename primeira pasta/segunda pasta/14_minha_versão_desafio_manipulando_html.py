from pathlib import Path

def retornar_itens_lista(arquivo):
    
def menu():
    html_a_ser_alterado = Path(input('Insira o caminho absoluto do html a ser alterado: '))
    if html_a_ser_alterado.suffix == '.html':
        with open(html_a_ser_alterado) as html:
            while True:
                linhas = html.readlines()
                posicao = 1
                lista = []
                for i, linha in enumerate(linhas):
                    if linha.strip() == '<li class="list-group-item border-0 d-flex align-items-center ps-0">':
                        item_lista = linhas[i + 2]
                        print(f'Item {posicao}: {item_lista.strip()}')
                        posicao += 1
                        lista.append(item_lista)
                if posicao > 1:
                    item_a_excluir = int(input('Qual dos itens deseja excluir? '))
                    excluir_itens_lista(linhas, item_a_excluir, lista[item_a_excluir - 1])
                else:
                    abrir_outro_arquivo = input('Essa lista lista está vazia. Se quiser abrir outro arquivo digite "s". ')
                    if abrir_outro_arquivo == 's':
                        menu()
    else:
        abrir_outro_arquivo = input('Esse arquivo não é html. Se quiser abrir outro arquivo digite "s". ')
        if abrir_outro_arquivo == 's':
            menu()

def excluir_itens_lista(lista, posicao, valor_item):
    i = encontrar_posicao(lista, valor_item, posicao)
    del lista[i-2:i+1]
    print('Lista atualizada')
    posicao = 1
    for i, linha in enumerate(lista):
        if linha.strip() == '<li class="list-group-item border-0 d-flex align-items-center ps-0">':
            item_lista = linhas[i + 2]
            print(f'Item {posicao}: {item_lista.strip()}')
            posicao += 1
    excluir_outro_item = input('Deseja excluir outro item? Se quiser digite o número do item. (Para sair digite "s") ')
    if excluir_outro_item == 's':
        None
    else:
        excluir_itens_lista(lista, excluir_outro_item)

def encontrar_posicao(lista, item, n_ocorrencia):
    contador = 0
    for i, valor in enumerate(lista):
        if valor == item:
            contador += 1
            if contador == n_ocorrencia:
                return i
    return -1

def criar_arquivo_lista_atualizada(arquivo, linha_a_excluir):


menu()