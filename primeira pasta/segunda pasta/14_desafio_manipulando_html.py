from pathlib import Path

def retornar_itens_lista(html_a_ser_alterado):
    with open(html_a_ser_alterado) as html:
        linhas = html.readlines()
        posicao = 1
        for i, linha in enumerate(linhas):
            if linha.strip() == '<input class="form-check-input me-3" type="checkbox" value="" aria-label="..." />':
                if i + 1 < len(linhas):
                    print(f'Item {posicao}: {linhas[i + 1].strip()}')
                    posicao += 1

html_a_ser_alterado = input('Insira o caminho absoluto do html a ser alterado: ')