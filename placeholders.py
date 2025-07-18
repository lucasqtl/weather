def dados(city):
    print(f"\n--- Dados Históricos ---")
    print(f"Acessando dados meteorológicos históricos para {city}:")
    print(f"Média de temperatura em julho nos últimos 10 anos: 25°C.")
    print(f"Dia mais chuvoso registrado (últimos 5 anos): 15/03/2022 com 50mm.")

def clima(city):
    print(f"\n--- Dados do Clima Atual ---")
    print(f"Coletando dados do clima atual para {city}:")
    print(f"Temperatura: 22°C")
    print(f"Umidade: 70%")
    print(f"Vento: 10 km/h (Norte)")
    print(f"Condição: Parcialmente nublado")

def locate():
    print(f"\n--- Sua Localização ---")
    print("Determinando sua localização atual...")
    location = "São Paulo, Brasil"
    print(f"Sua localização atual é: {location}.")
    print(f"Clima em {location}: Parcialmente nublado, 20°C.")

def mapa(city):
    print(f"\n--- Mapa da Região ---")
    print(f"Exibindo mapa interativo de padrões climáticos para a região de {city}.")
    print("Você pode ver frentes frias, áreas de chuva e temperaturas no mapa simulado.")

def widget():
    print(f"\n--- Widgets de Clima Personalizáveis ---")
    print("Configurando widgets de clima personalizáveis.")
    print("Opções: Widget de temperatura atual, previsão de 3 dias, radar de chuva.")
    print("Escolha seu estilo e dados preferidos para integrar em seu site ou aplicativo.")

def report():
    print(f"\n--- Reportar Clima ---")
    local_condition = input("Por favor, descreva as condições climáticas locais (ex: 'chuva forte', 'sol intenso', 'neblina'): ")
    print(f"Obrigado por reportar: '{local_condition}'.")
    print("Seu feedback é valioso e ajuda a melhorar as previsões!")

def analise():
    print(f"\n--- Análise do Clima ---")
    print("Gerando relatório de análise climática:")
    print("Tendência de aumento de 0.5°C na temperatura média anual na última década.")
    print("Aumento na frequência de eventos extremos (tempestades, ondas de calor).")

def alert(city):
    print(f"\n--- Alertas de Clima Severo ---")
    print(f"Verificando alertas de clima severo para {city}...")
    print(f"ALERTA: Possibilidade de tempestades fortes com granizo em {city} nas próximas 3 horas. Mantenha-se seguro!")
    print("Recomenda-se evitar áreas abertas e procurar abrigo.")