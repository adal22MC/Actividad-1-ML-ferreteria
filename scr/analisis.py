import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def producto_top(df: pd.DataFrame, ax: plt.Axes | None = None) -> pd.Series:
    ranking = df.groupby("Producto")["Total"].sum().sort_values(ascending=False)

    if ax is None:
        _, ax = plt.subplots(figsize=(10, 6))

    sns.barplot(
        x=ranking.index,
        y=ranking.values,
        hue=ranking.index,
        palette="Blues_r",
        legend=False,
        ax=ax,
    )
    ax.set_title(f"Producto top: {ranking.index[0]} (${ranking.iloc[0]:,.0f})")
    ax.set_xlabel("")
    ax.set_ylabel("Total ($)")
    ax.tick_params(axis="x", rotation=45)
    return ranking


def cliente_top(df: pd.DataFrame, top_n: int = 10, ax: plt.Axes | None = None) -> pd.Series:
    ranking = df.groupby("Cliente")["Total"].sum().sort_values(ascending=False).head(top_n)

    if ax is None:
        _, ax = plt.subplots(figsize=(10, 6))

    sns.barplot(
        x=ranking.index,
        y=ranking.values,
        hue=ranking.index,
        palette="Oranges_r",
        legend=False,
        ax=ax,
    )
    ax.set_title(f"Cliente top: {ranking.index[0]} (${ranking.iloc[0]:,.0f})")
    ax.set_xlabel("")
    ax.set_ylabel("Total ($)")
    ax.tick_params(axis="x", rotation=45)
    return ranking


def categoria_top(df: pd.DataFrame, ax: plt.Axes | None = None) -> pd.Series:
    ranking = df.groupby("Categoria")["Total"].sum().sort_values(ascending=False)

    if ax is None:
        _, ax = plt.subplots(figsize=(8, 6))

    sns.barplot(
        x=ranking.index,
        y=ranking.values,
        hue=ranking.index,
        palette="Greens_r",
        legend=False,
        ax=ax,
    )
    ax.set_title(f"Categoría top: {ranking.index[0]} (${ranking.iloc[0]:,.0f})")
    ax.set_xlabel("")
    ax.set_ylabel("Total ($)")
    return ranking
