def clasificar_numero(numero: int, umbral: int) -> str:
    if numero >= umbral:
        return "Alto"
    return "Bajo"

def clasificar_lista(numeros: list, umbral: int) -> list:
    return [(n, clasificar_numero(n, umbral)) for n in numeros]
