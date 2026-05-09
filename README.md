# Actividad 1 — ML Ferretería

Análisis de ventas y sistema de recomendación para una ferretería usando Python, scikit-learn y seaborn.

## Objetivo

A partir del dataset `data/ventas.xlsx` (3000 ventas, 100 clientes, 7 productos, 3 categorías) responder cuatro preguntas de negocio:

1. ¿Cuál es el **producto más vendido**? — por monto total ($).
2. ¿Cuál es el **cliente top**? — por monto total ($).
3. ¿Cuál es la **categoría más importante**? — por monto total ($).
4. ¿Quiénes son los **3 clientes potenciales** y qué productos les recomendamos? — top 3 por frecuencia de compra + recomendaciones KNN.

## Estructura del proyecto

```
Actividad-1-ML-ferreteria/
├── data/
│   └── ventas.xlsx           # dataset original
├── scr/
│   ├── load_data.py          # carga el Excel desde data/
│   ├── procesamiento.py      # limpieza: nulos, fechas, filtros
│   ├── model_ML.py           # entrena KNN coseno sobre matriz Cliente × Producto
│   ├── analisis.py           # rankings (producto / cliente / categoría) por $
│   └── recomendacion.py      # clientes potenciales + recomendaciones personalizadas
├── main.py                   # orquestador — produce el dashboard
├── requirements.txt
└── README.md
```

## Pipeline

`main.py` ejecuta de forma secuencial:

1. **Carga** → `cargar_datos()` lee `data/ventas.xlsx` con rutas vía `pathlib`.
2. **Limpieza** → `limpiar_datos(df)` elimina nulos, convierte `Fecha` a datetime y filtra `Cantidad > 0`, `Precio_Unitario > 0`.
3. **Modelo** → `entrenar_modelo(df)` codifica productos con `LabelEncoder`, arma matriz pivote Cliente × Producto (suma de cantidades) y entrena `NearestNeighbors` con métrica coseno.
4. **Rankings** → `producto_top`, `cliente_top`, `categoria_top` (todos por suma de `Total`).
5. **Recomendaciones** → `clientes_potenciales(df, n=3)` selecciona los 3 clientes más frecuentes; para cada uno, `recomendar()` devuelve los 3 productos más relevantes según los vecinos coseno.
6. **Dashboard** → matplotlib + seaborn, layout 2×3 en una sola figura.

## Cómo ejecutar

```bash
pip install -r requirements.txt
python main.py
```

Se abre una ventana matplotlib con 6 paneles:

| Fila | Panel 1 | Panel 2 | Panel 3 |
|---|---|---|---|
| **Superior** | Producto top ($) | Cliente top ($) | Categoría top ($) |
| **Inferior** | Recomendaciones cliente potencial #1 | #2 | #3 |

Los títulos de la fila inferior incluyen el número de compras de cada cliente para hacer explícito el criterio de selección.

## Tecnologías

- **pandas** — carga, limpieza, agregaciones.
- **scikit-learn** — `LabelEncoder` + `NearestNeighbors` (KNN coseno).
- **matplotlib** + **seaborn** — visualización del dashboard.

## Notas técnicas

- Las rutas en `scr/load_data.py` usan `pathlib` ancladas al script, así que el código corre desde cualquier directorio.
- El modelo KNN se entrena una sola vez y se reutiliza para las 3 recomendaciones.
- El criterio "cliente top" (panel superior) y "clientes potenciales" (panel inferior) son distintos a propósito: monto vs frecuencia. Por eso pueden no coincidir los mismos nombres.
