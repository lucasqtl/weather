from traducao import translations, display_menu
from modules.weather_display import previsao, tempo, alertas, history, feedback 
from modules.data_manager import load_feedbacks, save_feedbacks


language = "pt" 

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

    all_feedbacks = load_feedbacks()

    while True:
        display_menu(language)
        
        try:
            op = int(input(translations[language]['choose_option']))

            if op == 0:
                save_feedbacks(all_feedbacks)
                break
            elif op == 1:
                previsao(language)

            elif op == 2:
                tempo(language)
                
            elif op == 3:
                history(language)

            elif op == 4:
                city = input(translations[language]['enter_city'])
                placeholders.mapa(city)

            elif op == 5:
                placeholders.widget()

            elif op == 6:
                feedback(language)
                
            elif op == 7:
                placeholders.analise()
            elif op == 8:
                alertas(language)

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