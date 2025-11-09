import sys
from app.utils.randomic_number import get_random_number

def main():
    number = get_random_number()
    if number is not None:
        print(f"Número gerado: {number}")

if __name__ == "__main__":
    try:
        main()
        print("Executado com sucesso!")
        sys.exit(0)

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)