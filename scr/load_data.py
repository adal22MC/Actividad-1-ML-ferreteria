from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def cargar_datos(nombre_archivo: str = "ventas.xlsx") -> pd.DataFrame:
    ruta = DATA_DIR / nombre_archivo
    if not ruta.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {ruta}")

    df = pd.read_excel(ruta)
    print(f"Datos cargados desde {ruta.name} -> {df.shape[0]} filas, {df.shape[1]} columnas")
    return df
