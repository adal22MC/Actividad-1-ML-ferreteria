from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

from scr.load_data import cargar_datos
from scr.procesamiento import limpiar_datos
from scr.model_ML import entrenar_modelo
from scr.analisis import producto_top, cliente_top, categoria_top
from scr.recomendacion import (
    clientes_potenciales,
    recomendar,
    graficar_recomendacion,
)

PREVIEW_PATH = Path(__file__).resolve().parent / "preview.png"


def main() -> None:
    sns.set_theme(style="whitegrid", palette="muted")

    df = cargar_datos()
    df = limpiar_datos(df)

    modelo, matriz, le = entrenar_modelo(df)
    top3 = clientes_potenciales(df, n=3)
    frecuencias = df.groupby("Cliente").size()
    recos = {c: recomendar(c, modelo, matriz, le, top_n=3) for c in top3}

    fig, axes = plt.subplots(2, 3, figsize=(18, 11))
    fig.suptitle("Análisis de Ventas — Semana 2", fontsize=16, fontweight="bold")

    producto_top(df, ax=axes[0, 0])
    cliente_top(df, ax=axes[0, 1])
    categoria_top(df, ax=axes[0, 2])

    for ax, (cliente, productos) in zip(axes[1], recos.items()):
        graficar_recomendacion(ax, cliente, productos, frecuencia=int(frecuencias[cliente]))

    plt.tight_layout(rect=(0, 0, 1, 0.96))
    plt.subplots_adjust(hspace=0.55)
    fig.text(
        0.5, 0.475,
        "Recomendaciones para los 3 clientes más frecuentes (por número de compras)",
        ha="center", fontsize=12, fontstyle="italic", color="dimgray",
    )
    fig.savefig(PREVIEW_PATH, dpi=100)
    print(f"Preview guardado en: {PREVIEW_PATH}")
    plt.show()


if __name__ == "__main__":
    main()
