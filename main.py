import time
import random
from pathlib import Path
import argparse
from arbol import clasificar_lista

DATA_DIR = Path("data")
DATA_FILE = DATA_DIR / "numeros_1000.txt"
UMBRAL_DEFECTO = 50

def verificar_y_generar(file_path: Path, cantidad: int = 1000, minimo: int = 1, maximo: int = 100) -> int:
    if file_path.exists():
        return 0
    file_path.parent.mkdir(parents=True, exist_ok=True)
    semilla = int(time.time())
    random.seed(semilla)
    with file_path.open("w", encoding="utf-8") as f:
        for _ in range(cantidad):
            f.write(f"{random.randint(minimo, maximo)}\n")
    return semilla

def leer_numeros(file_path: Path) -> list:
    with file_path.open("r", encoding="utf-8") as f:
        return [int(line.strip()) for line in f if line.strip()]

def imprimir_resultados(clasificaciones: list, tiempo_seg: float, semilla: int):
    primeros = clasificaciones[:10]
    ejemplos = ", ".join([f"{n} → {et}" for n, et in primeros])
    altos = sum(1 for _, et in clasificaciones if et == "Alto")
    bajos = sum(1 for _, et in clasificaciones if et == "Bajo")
    if semilla:
        print(f"Archivo generado con semilla: {semilla}")
    print("Ejemplos (primeros 10):")
    print(ejemplos)
    print(f"Altos: {altos}")
    print(f"Bajos: {bajos}")
    print(f"Tiempo total de ejecución: {tiempo_seg:.6f} segundos")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--umbral", type=int, default=UMBRAL_DEFECTO)
    args = parser.parse_args()
    inicio = time.time()
    semilla = verificar_y_generar(DATA_FILE)
    numeros = leer_numeros(DATA_FILE)
    clasificaciones = clasificar_lista(numeros, args.umbral)
    fin = time.time()
    imprimir_resultados(clasificaciones, fin - inicio, semilla)

if __name__ == "__main__":
    main()
