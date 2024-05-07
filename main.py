import pandas as pd
import os
from twilio.rest import Client

account_sid = 'ACee98a0396c004b238080f26bdd7a6791'
auth_token = '5f49b2bcfd45aa6cf745ba92016b68ba'

client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses: 
    #print(mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    #print(tabela_vendas)
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas ['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas ['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor:{vendedor}, Vendas: {vendas}')
        message = client.messages.create(
                     body=f'No mês {mes} alguém bateu a meta. Vendedor:{vendedor}, Vendas: {vendas}',
                     from_='+12705618229',
                     to='+5581996997171'
                 )

print(message.sid)









