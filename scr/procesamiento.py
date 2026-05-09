import pandas as pd


def limpiar_datos(df: pd.DataFrame) -> pd.DataFrame:
    print("\nValores nulos por columna:")
    print(df.isnull().sum())

    df = df.dropna()
    df["Fecha"] = pd.to_datetime(df["Fecha"])
    df = df[(df["Cantidad"] > 0) & (df["Precio_Unitario"] > 0)]

    print(f"\nDatos limpios -> {df.shape[0]} filas")
    return df.reset_index(drop=True)
