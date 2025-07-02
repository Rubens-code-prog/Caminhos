# pip install pandas
# pip install openpyxl
from pathlib import Path
import pandas as pd

pasta_atual = Path(__file__).parent
#Lendo tabelas com DataFrame
tabela_clientes = pd.read_excel(pasta_atual / 'clientes.xlsx')





# Lendo aba específica
tabela_clientes = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name='SC')


# Modificando header
tabela_clientes = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name='SC', header=0)



# Adicionando coluna de index
tabela_clientes = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name='SC', index_col=0)




# Lendo colunas específicas
tabela_clientes = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name='SC', usecols=[0,1])


# Comentários sobre decimals e thousands
tabela_clientes = pd.read_excel(pasta_atual / 'clientes.xlsx', decimal='.')







tabela_clientes = pd.read_excel(pasta_atual / 'clientes.xlsx', thousands='.')





# Escrevendo planilha 
tabela_clientes = pd.read_excel(pasta_atual / 'clientes.xlsx', thousands='.')
# tabela_clientes.to_excel(pasta_atual / 'copia_clientes.xlsx')


# Escrevendo diversas abas
tabela_clientes_rs = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name='RS')
tabela_clientes_sc = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name='SC')

with pd.ExcelWriter(pasta_atual / 'copia_clientes.xlsx') as nova_planilha:
    tabela_clientes_rs.to_excel(nova_planilha, sheet_name='RS', index = False)
    tabela_clientes_sc.to_excel(nova_planilha, sheet_name='SC', index = False)