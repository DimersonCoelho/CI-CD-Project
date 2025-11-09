import requests


def get_random_number(min_number: int = 0, max_number: int = 100, number_quant: int = 1):
    print(f"Gerando {number_quant} número(s) aleatório entre {min_number} e {max_number}...\n\n")

    response = requests.get(f"https://www.randomnumberapi.com/api/v1.0/random?min={min_number}&max={max_number}&count={number_quant}")

    if response.status_code == 200:
        return response.json()[0]
    
    else:
        print("Erro ao gerar número. Status:", response.status_code)
        return None