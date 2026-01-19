import os
import re
from typing import List

from core.models import Carta

def extract_identifiers(filepath: str) -> Carta | None:

    """
    Extrai o setor (duas letras maiúsculas) e o código (8 digitos) do nome de um arquivo ou pasta
    Retorna objetos de Carta com status de padrão ou fora do padrão
    """

    filename = os.path.basename(filepath)

    #ReGex flexível para capturar diferentes tipos de sepaadores
    pattern = r"^([A-Z]{2})[-_]?([A-Z]{2,3})[-_]?(\d{8})(?:[-_]?([A-Za-z0-9]+))?(?:\.pdf)?$"

    match = re.match(pattern, filename)
    if not match:

        return None
    
    sede = match.group(1)
    setor = match.group(2)
    codigo = match.group(3)
    assunto = match.group(4) if match.group(4) else None

        # Verifica se o nome segue o padrão oficial de nomeação
        #Padrão oficial: XX_XX_XXXXXXXX_assunto

    oficial_pattern = f"{sede}_{setor}_{codigo}"
    if assunto:
        oficial_pattern += f"_{assunto}"
    if filename.startswith(oficial_pattern):
        status = "Padrão"
    else:
        status = "Fora do padrão"

    return Carta(
        setor = setor,
        codigo = codigo,
        nome_arquivo = filepath,
        origem = "Pasta",
        status = status
    )

def parse_files(arquivos: List[str]) -> List[Carta]:
    
    """
    Transforma nome de arquivos em objetos Carta
    """

    cartas: List[Carta] = []
    for nome in arquivos:
        identifier = extract_identifiers(nome)
        if not identifier:
            continue

        setor = identifier.get("setor")
        codigo = identifier.get("código")
        if not setor or not codigo:
            continue

        cartas.append(Carta(setor=setor, codigo=codigo, nome_arquivo=nome, origem="pasta"))
    return cartas