import argparse
import os
from src.core.reconcile import find_duplicates
from src.core.scanner import scan_folder
from src.core.parsing import parse_files


def main():
    parser = argparse.ArgumentParser(description="Sistema de Conferência Quantitativa")
    parser.add_argument("pasta", help="Caminho da pasta com os arquivos")
    args = parser.parse_args()

    if not os.path.exists(args.pasta):
        print(f"Erro: a pasta '{args.pasta}' não foi encontrada.")
        return

    try:
        arquivos = scan_folder(args.pasta)
        cartas = parse_files(arquivos)
        resultado = find_duplicates(cartas)
        print("Resultado da conferência:")
        print(resultado)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    main()
