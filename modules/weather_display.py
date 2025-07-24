from traducao import translations
from .api_service import get_weather_data, get_historical_data
from feedback_model import Feedback
from .data_manager import load_feedbacks, save_feedbacks, feedback_list

def previsao(language):
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


def tempo(language):
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

def alertas(language):
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

def history(language):
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
    
def feedback(language):

    location = input('Qual a localização? ') 
    condition = input('Qual a condição do clima? ') 
    temperature_str = input('Qual a temperatura? ') 

    try:
        temperature = float(temperature_str)
    except ValueError:
        print("Temperatura inválida. Por favor, digite um número.")
        return

    comment = input('Escreva um comentário ou apenas digite "x" para prosseguir') # OK

    new_feedback = Feedback(location, condition, temperature, comment) # OK
    
    feedbacks = load_feedbacks() 
    feedbacks.append(new_feedback)

    save_feedbacks(feedbacks)
    
    print(translations[language].get('feedback_saved_message', 'Feedback salvo com sucesso!')) 
