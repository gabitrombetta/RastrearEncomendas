import requests
from bs4 import BeautifulSoup

option = 's'
while(option.lower() == 's'):
    print('\n====RASTREAR OBJETOS | CORREIOS====')
    codigo = input('Informe o código de rastreamento: ')
    url = f'https://www.linkcorreios.com.br/?id={codigo}'

    try:
        if (requests.get(url).status_code == 200):
            html = requests.get(url).text

            soup = BeautifulSoup(html, 'html.parser')

            rastreio = soup.find('ul', class_="linha_status")

            print(f'{rastreio.get_text()}\n')
        else:
            print('Serviço indisponível no momento')
    except Exception as e:
        print('\n=> Objeto não encontrado.\n')

    option = input('Deseja rastrear outro objeto? [s/n] ')

