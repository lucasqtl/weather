import requests
import pandas as pd
from traducao import translations, display_menu
import placeholders

API_KEY = "3be1c4471e774f6d828141159251807"

def get_weather_data(query, forecast_days=1, lang="en"):
    base_url = "http://api.weatherapi.com/v1"
    endpoint = "/forecast.json"
    
    params = {
        "key": API_KEY,
        "q": query,
        "days": forecast_days, 
        "alerts": "yes",
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
    
def get_historical_data(query, date, lang):
    base_url = "http://api.weatherapi.com/v1"
    endpoint = "/history.json"
    
    params = {
        "key": API_KEY,
        "q": query,
        "dt": date, 
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
    print(f'{translations[language]['text_city']}: {city.title()}')
    for day_data in weather_data['forecast']['forecastday']:
        print('\n' + '='*30)
        count+=1
        print(f'Dia {count}:')
        print(f'{translations[language]['day']}: {day_data['date']}')
        print(f'{translations[language]['max_temp']}: {day_data['day']['maxtemp_c']}°')
        print(f'{translations[language]['min_temp']}: {day_data['day']['mintemp_c']}°')
        print(f'{translations[language]['conditions']}: {day_data['day']['condition']['text']}')
        print(f'{translations[language]['sunrise']}: {day_data['astro']['sunrise']}')
        print(f'{translations[language]['sunset']}: {day_data['astro']['sunset']}')
        print('='*30)

    option = input('Digite "c" para consultar outra cidade ou "m" para voltar ao menu: ')
    if option == 'c':
        tempo()
    elif option == 'm':
        return
    else:
        print('Entrada inválida, retornando ao menu')
        return


def tempo():
    city = input(translations[language]['enter_city'])
    weather_data = get_weather_data(city, 1, language)

    print('\n' + '='*30)
    print(f'Como está o tempo em {city.title()}')
    print(f'Temperatura: {weather_data['current']['temp_c']}°')
    print(f'Condição: {weather_data['current']['condition']['text']}')
    print(f'Umidade: {weather_data['current']['humidity']}%')
    print(f'Velocidade do vento: {weather_data['current']['wind_kph']}km/h')
    print(f'Precipitação: {weather_data['current']['precip_mm']}mm')
    print('='*30)
    
    option = input('Digite "c" para consultar outra cidade ou "m" para voltar ao menu: ')
    if option == 'c':
        tempo()
    elif option == 'm':
        return
    else:
        print('Entrada inválida, retornando ao menu')
        return

def alertas():
    city = input('Digite a cidade que você quer consultar se há alertas: ')
    weather_data = get_weather_data(city, 7, language)
                                    
    if 'alerts' in weather_data:
        if weather_data['alerts']['alert']:
            print(f'Temos alertas climáticos nos próximos 7 dias em : {city.title()}')
            for alert in weather_data['alerts']['alert']: 
                print('\n' + '='*30)
                print(f"Título: {alert.get('headline', 'N/A')}")
                print(f"Descrição: {alert.get('desc', 'N/A')}")
                print(f"Severidade: {alert.get('severity', 'N/A')}")
                print(f"Urgência: {alert.get('urgency', 'N/A')}")
                print(f"Áreas afetadas: {alert.get('areas', 'N/A')}")
                print('='*30)
        else:
            print('\n' + '='*30)
            print('Não existem alertas climáticos para a sua cidade nos próximos 7 dias.')
            print('='*30)

def history():
    print('\n' + '='*30)
    city = input('Digite a cidade que você quer consultar: ')
    print('OBS: Temoss dados históricos a partir de 1° de Janeiro de 2010')
    print('Digite a data no formato: yyyy-MM-dd')
    date = input('Digite a data que você quer consultar: ')
    print('='*30)

    historical_data = get_historical_data(city, date, language)
    day_data = historical_data['forecast']['forecastday'][0]

    print('\n' + '='*30)
    print(f'Como estava o tempo no dia: {day_data['date']} em {city.title()}')
    print(f'{translations[language]['max_temp']}: {day_data['day']['maxtemp_c']}°')
    print(f'{translations[language]['min_temp']}: {day_data['day']['mintemp_c']}°')
    print(f'{translations[language]['conditions']}: {day_data['day']['condition']['text']}')
    print(f'Precipitação Total: {day_data['day']['totalprecip_mm']}mm')
    print(f'Velocidade Máxima do Vento: {day_data['day']['maxwind_kph']}km/h')
    print(f'Umidade media: {day_data['day']['avghumidity']}%')
    print(f'{translations[language]['sunrise']}: {day_data['astro']['sunrise']}')
    print(f'{translations[language]['sunset']}: {day_data['astro']['sunset']}')
    print('='*30)
    
    option = input('Digite "c" para consultar outra cidade ou "m" para voltar ao menu: ')
    if option == 'c':
        tempo()
    elif option == 'm':
        return
    else:
        print('Entrada inválida, retornando ao menu')
        return


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
                tempo()
                
            elif op == 3:
                history()

            elif op == 4:
                city = input(translations[language]['enter_city'])
                placeholders.mapa(city)

            elif op == 5:
                placeholders.widget()

            elif op == 6:
                placeholders.report()
                
            elif op == 7:
                placeholders.analise()
            elif op == 8:
                alertas()

            elif op == 9:
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