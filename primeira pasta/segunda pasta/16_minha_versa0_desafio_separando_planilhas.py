from pathlib import Path
import pandas as pd

pasta_atual = Path(__file__).parent

def separar_planilha(caminho):
    planilha = pd.ExcelFile(caminho)
    for aba in planilha.sheet_names:
        pd.read_excel(caminho, sheet_name=aba).to_excel(caminho.parent / f'{aba}.xlsx', index=False)

def juntar_planilhas(*planilhas:Path):
    with pd.ExcelWriter(pasta_atual / 'nova_planilha.xlsx') as nova_planilha:
        for planilha in planilhas:
            tabela = pd.read_excel(planilha)
            tabela.to_excel(nova_planilha, sheet_name=planilha.stem, index=False)

# separar_planilha(Path(__file__).parent / 'clientes.xlsx')
juntar_planilhas(
    pasta_atual / 'PR.xlsx',
    pasta_atual / 'RS.xlsx', 
    pasta_atual / 'SC.xlsx', 
    pasta_atual / 'SP.xlsx'
    )