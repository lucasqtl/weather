import func1, func2, func3, func4, func5, func6, func7, func8, func9, func10

# Dicionário para gerenciar as traduções
translations = {
    'pt': {
        'select_feature': 'Selecione uma funcionalidade:',
        'weather_forecast': '1 - Previsão do Tempo:',
        'historical_data': '2 - Dados Históricos:',
        'current_weather_data': '3 - Dados do clima atual:',
        'your_location': '4 - Sua localização:',
        'region_map': '5 - Mapa da Região:',
        'customizable_widgets': '6 - Widgets Personalizáveis:',
        'report_local_weather': '7 - Reportar Clima Local:',
        'climate_analysis': '8 - Análise do Clima:',
        'severe_weather_alerts': '9 - Alertas de Clima Severo:',
        'select_language': '10 - Selecionar Idioma:',
        'close_menu': '0 - Fechar Menu:',
        'choose_option': 'Qual opção deseja? ',
        'enter_city': 'Digite a sua cidade: '
    },
    'en': {
        'select_feature': 'Select a feature:',
        'weather_forecast': '1 - Weather Forecast:',
        'historical_data': '2 - Historical Data:',
        'current_weather_data': '3 - Current Weather Data:',
        'your_location': '4 - Your Location:',
        'region_map': '5 - Region Map:',
        'customizable_widgets': '6 - Customizable Widgets:',
        'report_local_weather': '7 - Report Local Weather:',
        'climate_analysis': '8 - Climate Analysis:',
        'severe_weather_alerts': '9 - Severe Weather Alerts:',
        'select_language': '10 - Select Language:',
        'close_menu': '0 - Close Menu:',
        'choose_option': 'Which option do you want? ',
        'enter_city': 'Enter your city: '
    },
    'es': {
        'select_feature': 'Seleccione una funcionalidad:',
        'weather_forecast': '1 - Pronóstico del Tiempo:',
        'historical_data': '2 - Datos Históricos:',
        'current_weather_data': '3 - Datos del clima actual:',
        'your_location': '4 - Su ubicación:',
        'region_map': '5 - Mapa de la Región:',
        'customizable_widgets': '6 - Widgets Personalizables:',
        'report_local_weather': '7 - Reportar Clima Local:',
        'climate_analysis': '8 - Análisis Climático:',
        'severe_weather_alerts': '9 - Alertas de Clima Severo:',
        'select_language': '10 - Seleccionar Idioma:',
        'close_menu': '0 - Cerrar Menú:',
        'choose_option': '¿Qué opción desea? ',
        'enter_city': 'Ingrese su ciudad: '
    }
}

def display_menu(lang):
    """Exibe o menu de opções no idioma selecionado."""
    print('\n' + '='*30)
    print(translations[lang]['select_feature'])
    print(translations[lang]['weather_forecast'])
    print(translations[lang]['historical_data'])
    print(translations[lang]['current_weather_data'])
    print(translations[lang]['your_location'])
    print(translations[lang]['region_map'])
    print(translations[lang]['customizable_widgets'])
    print(translations[lang]['report_local_weather'])
    print(translations[lang]['climate_analysis'])
    print(translations[lang]['severe_weather_alerts'])
    print(translations[lang]['select_language'])
    print(translations[lang]['close_menu'])
    print('='*30)

if __name__ == '__main__':
    print('\n' + '='*30)
    print('Português: pt')
    print('Inglês: en')
    print('Espanhol: es')
    language = input('Escolha um Idioma: ').lower()
    print('='*30)

    # Garante que o idioma selecionado seja válido, caso contrário, define para português
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
                city = input(translations[language]['enter_city'])
                func1.previ(city)
            elif op == 2:
                city = input(translations[language]['enter_city'])
                func2.dados(city)
            elif op == 3:
                city = input(translations[language]['enter_city'])
                func3.clima(city)
            elif op == 4:
                func4.locate()
            elif op == 5:
                city = input(translations[language]['enter_city'])
                func5.mapa(city)
            elif op == 6:
                func6.widget()
            elif op == 7:
                func7.report()
            elif op == 8:
                func8.analise()
            elif op == 9:
                city = input(translations[language]['enter_city'])
                func9.alert(city)
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