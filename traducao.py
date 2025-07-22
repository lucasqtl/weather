# Dicionário para gerenciar as traduções
translations = {
    'pt': {
        'select_feature': 'Selecione uma funcionalidade:',
        'weather_forecast': '1 - Previsão do Tempo:',
        'current_weather_data': '2 - Dados do clima atual:',
        'historical_data': '3 - Dados Históricos:',
        'region_map': '4 - Mapa da Região:',
        'customizable_widgets': '5 - Widgets Personalizáveis:',
        'report_local_weather': '6 - Reportar Clima Local:',
        'climate_analysis': '7 - Análise do Clima:',
        'severe_weather_alerts': '8 - Alertas de Clima Severo:',
        'select_language': '9 - Selecionar Idioma:',
        'close_menu': '0 - Fechar Menu:',
        'choose_option': 'Qual opção deseja? ',
        'enter_city': 'Digite a sua cidade: ',
        'text_city': 'Previsão para os próximos 7 dias em',
        'day': 'Dia',
        'max_temp': 'Temperatura máxima',
        'min_temp': 'Temperatura mínima',
        'conditions': 'Condições',
        'sunrise': 'Nascer do Sol',
        'sunset': 'Pôr do Sol',
    },
    'en': {
        'select_feature': 'Select a feature:',
        'weather_forecast': '1 - Weather Forecast:',
        'current_weather_data': '2 - Current Weather Data:',
        'historical_data': '3 - Historical Data:',
        'region_map': '4 - Region Map:',
        'customizable_widgets': '5 - Customizable Widgets:',
        'report_local_weather': '6 - Report Local Weather:',
        'climate_analysis': '7 - Climate Analysis:',
        'severe_weather_alerts': '8 - Severe Weather Alerts:',
        'select_language': '9 - Select Language:',
        'close_menu': '0 - Close Menu:',
        'choose_option': 'Which option do you want? ',
        'enter_city': 'Enter your city: ',
        'text_city': 'Forecast for the next 7 days in',
        'day': 'Day',
        'max_temp': 'Maximum Temperature',
        'min_temp': 'Minimum Temperature',
        'conditions': 'Conditions',
        'sunrise': 'Sunrise',
        'sunset': 'Sunset',
    },
    'es': {
        'select_feature': 'Seleccione una funcionalidad:',
        'weather_forecast': '1 - Pronóstico del Tiempo:',
        'current_weather_data': '2 - Datos del clima actual:',
        'historical_data': '3 - Datos Históricos:',
        'region_map': '4 - Mapa de la Región:',
        'customizable_widgets': '5 - Widgets Personalizables:',
        'report_local_weather': '6 - Reportar Clima Local:',
        'climate_analysis': '7 - Análisis Climático:',
        'severe_weather_alerts': '8 - Alertas de Clima Severo:',
        'select_language': '9 - Seleccionar Idioma:',
        'close_menu': '0 - Cerrar Menú:',
        'choose_option': '¿Qué opción desea? ',
        'enter_city': 'Ingrese su ciudad: ',
        'text_city': 'Pronóstico para los próximos 7 días en',
        'day': 'Día',
        'max_temp': 'Temperatura máxima',
        'min_temp': 'Temperatura mínima',
        'conditions': 'Condiciones',
        'sunrise': 'Amanecer',
        'sunset': 'Atardecer'
    }
}

def display_menu(lang):
    """Exibe o menu de opções no idioma selecionado."""
    print('\n' + '='*30)
    print(translations[lang]['select_feature'])
    print(translations[lang]['weather_forecast'])
    print(translations[lang]['current_weather_data'])
    print(translations[lang]['historical_data'])
    print(translations[lang]['region_map'])
    print(translations[lang]['customizable_widgets'])
    print(translations[lang]['report_local_weather'])
    print(translations[lang]['climate_analysis'])
    print(translations[lang]['severe_weather_alerts'])
    print(translations[lang]['select_language'])
    print(translations[lang]['close_menu'])
    print('='*30)