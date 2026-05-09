import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import NearestNeighbors


def entrenar_modelo(df: pd.DataFrame) -> tuple[NearestNeighbors, pd.DataFrame, LabelEncoder]:
    le = LabelEncoder()
    df = df.copy()
    df["Producto_ID"] = le.fit_transform(df["Producto"])

    matriz = df.pivot_table(
        index="Cliente",
        columns="Producto_ID",
        values="Cantidad",
        aggfunc="sum",
        fill_value=0,
    )

    modelo = NearestNeighbors(metric="cosine")
    modelo.fit(matriz)

    print(f"\nModelo entrenado -> {matriz.shape[0]} clientes x {matriz.shape[1]} productos")
    return modelo, matriz, le
