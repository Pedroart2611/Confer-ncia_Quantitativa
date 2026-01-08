import os


def scan_folder(folder_path: str) -> list[str]:
    """Retorna a lista de arquivos dentro da pasta."""
    return [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f))
    ]
