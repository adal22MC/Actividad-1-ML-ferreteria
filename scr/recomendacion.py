import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import LabelEncoder


def clientes_potenciales(df: pd.DataFrame, n: int = 3) -> list[str]:
    return df.groupby("Cliente").size().nlargest(n).index.tolist()


def recomendar(
    cliente: str,
    modelo: NearestNeighbors,
    matriz: pd.DataFrame,
    le: LabelEncoder,
    top_n: int = 3,
) -> list[str]:
    if cliente not in matriz.index:
        raise ValueError(f"Cliente {cliente} no encontrado en la matriz")

    vector = matriz.loc[cliente].values.reshape(1, -1)
    _, indice = modelo.kneighbors(vector, n_neighbors=top_n + 1)

    vecinos = matriz.index[indice.flatten()[1:]]
    recomendaciones = matriz.loc[vecinos].mean().sort_values(ascending=False)
    productos = le.inverse_transform(recomendaciones.index.astype(int))

    return list(productos[:top_n])


def graficar_recomendacion(
    ax: plt.Axes,
    cliente: str,
    productos: list[str],
    frecuencia: int | None = None,
) -> None:
    ranks = list(range(len(productos), 0, -1))
    sns.barplot(
        x=ranks,
        y=productos,
        hue=productos,
        palette="Purples_r",
        legend=False,
        ax=ax,
    )
    titulo = f"{cliente} — {frecuencia} compras" if frecuencia is not None else f"Recomendaciones: {cliente}"
    ax.set_title(titulo)
    ax.set_xlabel("Ranking (mayor = mejor)")
    ax.set_ylabel("")
