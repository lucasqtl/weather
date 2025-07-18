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
    print(translations[lang]['current_weather_data'])
    print(translations[lang]['historical_data'])
    print(translations[lang]['your_location'])
    print(translations[lang]['region_map'])
    print(translations[lang]['customizable_widgets'])
    print(translations[lang]['report_local_weather'])
    print(translations[lang]['climate_analysis'])
    print(translations[lang]['severe_weather_alerts'])
    print(translations[lang]['select_language'])
    print(translations[lang]['close_menu'])
    print('='*30)