import os
import re

def extract_identifiers(filename):
    name, _ = os.path.splitext(filename)

    # Normaliza separadores
    name = name.replace("-", "_").replace(" ", "_")

    # Procura setor (duas letras maiúsculas) e código (8 dígitos)
    sector_match = re.search(r"_[A-Z]{2}_", name)
    code_match = re.search(r"\d{8}", name)

    if sector_match and code_match:
        # Remove underscores extras do setor
        setor = sector_match.group().replace("_", "")
        codigo = code_match.group()
        return {"setor": setor, "código": codigo}

    return None
