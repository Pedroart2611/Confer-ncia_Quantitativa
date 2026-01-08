import os
from src.utils import extract_identifiers


def scan_folder(folder_path):
    duplicates = {}

    for filename in os.listdir(folder_path):
        identifier = extract_identifiers(filename)
        if not identifier:
            continue

        if isinstance(identifier, dict):
            setor = identifier.get("setor")
            codigo = identifier.get("código")
        elif isinstance(identifier, (tuple, list)) and len(identifier) >= 2:
            setor, codigo = identifier[0], identifier[1]
        else:
            continue

        if not setor or not codigo:
            continue

        key = f"{setor}_{codigo}"
        if key not in duplicates:
            duplicates[key] = []
        duplicates[key].append(filename)

    print(f"{filename} -> {identifier}")

    return duplicates
