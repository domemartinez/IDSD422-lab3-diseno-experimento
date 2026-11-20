# comparacion_experimento.py — Comparación de grupos (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/comparacion_experimento.py

# TODO 1: carga plantillas/registro_experimento.csv con pandas
# TODO 2: calcula e imprime el promedio de ventas_producto por ubicacion
# TODO 3: imprime el número de registros por grupo (value_counts)
# TODO 4: escribe 2–3 líneas de interpretación (sección 9 de la plantilla):
#         por qué con 4 filas no se puede concluir y qué le faltaría al análisis


from pathlib import Path
import pandas as pd

ruta_csv = Path("plantillas/registro_experimento.csv")
df = pd.read_csv(ruta_csv)

print("=== Datos de plantillas/registro_experimento.csv ===")
print(df.to_string(index=False))
print(f"\nTotal de filas: {len(df)}")

col_grupo = "ubicacion" if "ubicacion" in df.columns else df.select_dtypes(exclude="number").columns[0]
col_ventas = "ventas_producto" if "ventas_producto" in df.columns else df.select_dtypes(include="number").columns[-1]

resumen = (
    df.groupby(col_grupo, dropna=False)[col_ventas]
    .agg(n="count", media="mean", sd="std", min="min", max="max")
    .reset_index()
)

print("\n=== Resumen por grupo ===")
print(resumen.to_string(index=False))
