import requests
import json
import xml.etree.ElementTree as ET

# URL base da API
define_url = 'https://saomateus-es.portaltp.com.br/api/transparencia.asmx/json_execucao_receitas'

# Lista para armazenar todos os dados coletados
data_list = []

# Loop para coletar dados de 2017 a 2023
for year in range(2017, 2024):
    for month in range(1, 13):
        # Parâmetros da API
        params = {'ano': str(year), 'mes': str(month)}

        # Fazendo a requisição
        response = requests.get(define_url, params=params)

        # Verificando se a requisição foi bem-sucedida
        if response.status_code == 200:
            # Parse do XML
            root = ET.fromstring(response.content)

            # Extraindo o JSON do XML
            json_data = json.loads(root.text)

            # Adicionando ao data_list
            data_list.extend(json_data)
        else:
            print(f'Erro ao coletar dados para o ano {year} e mês {month}')

# Salvando os dados em um arquivo JSON
with open('data_sao_mateus.json', 'w') as f:
    json.dump(data_list, f)

print('Dados coletados e salvos com sucesso.')