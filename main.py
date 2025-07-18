import placeholders
from traducao import translations, display_menu

import requests
import pandas as pd

API_KEY = "3be1c4471e774f6d828141159251807"

def get_weather_data(query, forecast_days=1, lang="en"):
    base_url = "http://api.weatherapi.com/v1"
    endpoint = "/forecast.json"
    
    params = {
        "key": API_KEY,
        "q": query,
        "days": forecast_days, 
        "alerts": "no", # Pode ser 'yes' se quiser alertas
        "lang": lang
    }

    try:
        response = requests.get(f"{base_url}{endpoint}", params=params)
        response.raise_for_status() 
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição à WeatherAPI.com: {e}")
        return None

def previsao():
    city = input(translations[language]['enter_city'])
    weather_data = get_weather_data(city, 7, language)

    count = 0
    print(f'{translations[language]['text_city']}: {city}')
    for day_data in weather_data['forecast']['forecastday']:
        print('\n' + '='*30)
        count+=1
        print(f'Dia {count}:')
        print(f'{translations[language]['day']}: {day_data['date']}')
        print(f'{translations[language]['max_temp']}: {day_data['day']['maxtemp_c']}')
        print(f'{translations[language]['min_temp']}: {day_data['day']['mintemp_c']}')
        print(f'{translations[language]['conditions']}: {day_data['day']['condition']['text']}')
        print(f'{translations[language]['sunrise']}: {day_data['astro']['sunrise']}')
        print(f'{translations[language]['sunset']}: {day_data['astro']['sunset']}')
        print('='*30)

if __name__ == '__main__':
    print('\n' + '='*30)
    print('Português: pt')
    print('Inglês: en')
    print('Espanhol: es')
    language = input('Escolha um Idioma: ').lower()
    print('='*30)

    if language not in translations:
        print("Idioma inválido. Usando Português (pt) por padrão.")
        language = 'pt'

    while True:
        display_menu(language)
        
        try:
            op = int(input(translations[language]['choose_option']))

            if op == 0:
                break
            elif op == 1:
                previsao()

            elif op == 2:
                city = input(translations[language]['enter_city'])
                placeholders.clima(city)
            elif op == 3:
                city = input(translations[language]['enter_city'])
                placeholders.dados(city)
            elif op == 4:
                placeholders.locate()
            elif op == 5:
                city = input(translations[language]['enter_city'])
                placeholders.mapa(city)
            elif op == 6:
                placeholders.widget()
            elif op == 7:
                placeholders.report()
            elif op == 8:
                placeholders.analise()
            elif op == 9:
                city = input(translations[language]['enter_city'])
                placeholders.alert(city)
            elif op == 10:
                print('\n' + '='*30)
                print('Português: pt')
                print('Inglês: en')
                print('Espanhol: es')
                new_language = input('Escolha um Idioma: ').lower()
                print('='*30)
                if new_language in translations:
                    language = new_language
                else:
                    print(f"Idioma '{new_language}' não suportado. Mantendo o idioma atual.")
            else:
                print("Opção inválida. Por favor, tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")