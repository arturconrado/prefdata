import requests
import pandas as pd
import json
from xml.etree import ElementTree as ET

def fetch_data_for_year(year, data_type):
    print(f'Baixando dados para o ano {year}...')
    url = f'https://saomateus-es.portaltp.com.br/api/transparencia.asmx/json_{data_type}?ano={year}'
    response = requests.get(url)

    if response.status_code != 200:
        print(f'Erro na requisição para o ano {year}: {response.status_code}')
        return None

    try:
        tree = ET.fromstring(response.content)
        json_str = tree.text

        if not json_str:
            print(f'Nenhum JSON encontrado para o ano {year}.')
            return None

        return pd.DataFrame(json.loads(json_str))

    except Exception as e:
        print(f'Erro ao processar dados para o ano {year}: {e}')
        return None

def fetch_data_for_years(year_range, data_type):
    return {year: fetch_data_for_year(year, data_type) for year in year_range}

def save_data_to_single_json(data_frames, data_type):
    all_data = {}
    for year, df in data_frames.items():
        if df is not None:
            all_data[str(year)] = json.loads(df.to_json(orient='records'))
            print(f'Adicionando dados para o ano {year} ao arquivo JSON.')
    filename = f'all_years_data_{data_type}.json'
    with open(filename, 'w') as f:
        json.dump(all_data, f)
    print(f'Todos os dados foram salvos em {filename}')

if __name__ == '__main__':
    years_to_fetch = range(2017, 2024)
    data_type = "orcamento_receitas"  # Você pode alterar isso para o tipo de dado que está baixando
    data_frames = fetch_data_for_years(years_to_fetch, data_type)
    save_data_to_single_json(data_frames, data_type)
