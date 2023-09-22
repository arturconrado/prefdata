import requests
import json

# List of URLs for each category
compras = [
    'https://saomateus-es.portaltp.com.br/api/compras/api-licitacoes.aspx',
    'https://saomateus-es.portaltp.com.br/api/compras/api-contratos.aspx',
    'https://saomateus-es.portaltp.com.br/api/compras/api-atas.aspx',
    'https://saomateus-es.portaltp.com.br/api/compras/api-ordemcompras.aspx'
]

materiais_bens = [
    'https://saomateus-es.portaltp.com.br/api/materiais/api-entradas.aspx',
    'https://saomateus-es.portaltp.com.br/api/materiais/api-saidas.aspx',
    'https://saomateus-es.portaltp.com.br/api/materiais/api-patrimonio.aspx',
    'https://saomateus-es.portaltp.com.br/api/bens/api-moveis.aspx',
    'https://saomateus-es.portaltp.com.br/api/bens/api-imoveis.aspx',
    'https://saomateus-es.portaltp.com.br/api/frota/api-veiculos.aspx'
]

receita = [
    'https://saomateus-es.portaltp.com.br/api/orcamento/api-orcamentoreceitas.aspx',
    'https://saomateus-es.portaltp.com.br/api/receitas/api-execucaoreceitas.aspx'
]

despesas = [
    'https://saomateus-es.portaltp.com.br/api/orcamento/api-orcamentodespesas.aspx',
    'https://saomateus-es.portaltp.com.br/api/despesas/api-empenhos.aspx',
    'https://saomateus-es.portaltp.com.br/api/despesas/api-liquidacoes.aspx',
    'https://saomateus-es.portaltp.com.br/api/despesas/api-pagamentos.aspx',
    'https://saomateus-es.portaltp.com.br/api/despesas/api-diarias.aspx',
    'https://saomateus-es.portaltp.com.br/api/despesas/api-obras.aspx'
]

repasse = [
    'https://saomateus-es.portaltp.com.br/api/repasses/api-conveniosfirmados.aspx',
    'https://saomateus-es.portaltp.com.br/api/repasses/api-extraorcamentarias.aspx',
    'https://saomateus-es.portaltp.com.br/api/repasses/api-intraorcamentarias.aspx'
]

pessoal = [
    'https://saomateus-es.portaltp.com.br/api/pessoal/api-servidores.aspx',
    'https://saomateus-es.portaltp.com.br/api/pessoal/api-planocarreiras.aspx',
    'https://saomateus-es.portaltp.com.br/api/pessoal/api-cargosconfianca.aspx'
]

# Function to make the API call
def fetch_data(url, params=None):
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Example of how to call the API for the 'compras' category
for url in compras:
    for ano in range(2017, 2024):
        for mes in range(1, 13):
            params = {'ano': ano, 'mes': mes}
            data = fetch_data(url, params)
            if data:
                print(f'Data from {url} for {ano}-{mes}: {data}')
            else:
                print(f'Failed to fetch data from {url} for {ano}-{mes}')

# Do the same for the other categories
for url in materiais_bens:
    for ano in range(2017, 2024):
        for mes in range(1, 13):
            params = {'ano': ano, 'mes': mes}
            data = fetch_data(url, params)
            if data:
                print(f'Data from {url} for {ano}-{mes}: {data}')
            else:
                print(f'Failed to fetch data from {url} for {ano}-{mes}')

for url in receita:
    for ano in range(2017, 2024):
        for mes in range(1, 13):
            params = {'ano': ano, 'mes': mes}
            data = fetch_data(url, params)
            if data:
                print(f'Data from {url} for {ano}-{mes}: {data}')
            else:
                print(f'Failed to fetch data from {url} for {ano}-{mes}')

for url in despesas:
    for ano in range(2017, 2024):
        for mes in range(1, 13):
            params = {'ano': ano, 'mes': mes}
            data = fetch_data(url, params)
            if data:
                print(f'Data from {url} for {ano}-{mes}: {data}')
            else:
                print(f'Failed to fetch data from {url} for {ano}-{mes}')

for url in repasse:
    for ano in range(2017, 2024):
        for mes in range(1, 13):
            params = {'ano': ano, 'mes': mes}
            data = fetch_data(url, params)
            if data:
                print(f'Data from {url} for {ano}-{mes}: {data}')
            else:
                print(f'Failed to fetch data from {url} for {ano}-{mes}')

for url in pessoal:
    for ano in range(2017, 2024):
        for mes in range(1, 13):
            params = {'ano': ano, 'mes': mes}
            data = fetch_data(url, params)
            if data:
                print(f'Data from {url} for {ano}-{mes}: {data}')
            else:
                print(f'Failed to fetch data from {url} for {ano}-{mes}')