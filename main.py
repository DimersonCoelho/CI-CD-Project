import sys
from app.utils.randomic_number import get_random_number
from var.environment_variables import NOME_ARQUIVO

def salvar_lista_em_arquivo(lista: list = [], nome_arquivo: str = "random_numbers_list.txt"):
    with open(nome_arquivo, 'w') as arquivo:
        for numero in lista:
            arquivo.write(f"{numero}\n")

def main():
    lista_de_numeros = []
    for i in range(3):
        number = get_random_number()
        if number is not None:
            print(f"Número gerado: {number}")
            lista_de_numeros.append(number)
    
    salvar_lista_em_arquivo(lista_de_numeros, NOME_ARQUIVO)


if __name__ == "__main__":
    try:
        main()
        print("Executado com sucesso!")
        sys.exit(0)

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)