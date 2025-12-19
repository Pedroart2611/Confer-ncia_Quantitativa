from src.scanner import scan_folder
from src.report import generate_report


def main():

    import sys
    if len(sys.argv) < 2:
        print("Uso: python main.py <\"C:\\Users\\pedro.murillo.est\\ARTERIS S A\\REGULATÓRIO AF AFD - Documentos\\Correspondências\\AFL\\ANTT - enviadas\\2025\\11_2025\">")
        return
    
    folder_path = sys.argv[1]

    duplicates = scan_folder(folder_path)

    if not duplicates:
        print("Nenhum arquivo duplicado encontrado.")
    else:
        print("Duplicatas encontradas: ")
        for key, files in duplicates.items():
            print(f"{key} -> {len(files)} arquivos")
            for f in files:
                print(f"  - {f}")

    generate_report(duplicates, "reports/Conferência Quantitativa.docx")

if __name__ == "__main__":
    main()