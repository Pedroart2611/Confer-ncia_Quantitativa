from src.core.models import Carta
from src.utils import extract_identifiers


def parse_files(arquivos: list[str]) -> list[Carta]:
    """Transforma nomes de arquivos em objetos Carta."""
    cartas = []
    for nome in arquivos:
        identifier = extract_identifiers(nome)
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

        cartas.append(
            Carta(setor=setor, codigo=codigo, nome_arquivo=nome, origem="pasta")
        )
    return cartas
