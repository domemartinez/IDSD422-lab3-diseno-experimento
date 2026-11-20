# Plantilla de protocolo — Experimento de ubicación de producto

 **Nombre:** Doménica Martínez · **Fecha:** 19/11/2026
 **Repositorio (fork):** https://github.com/domemartinez/IDSD422-lab3-diseno-experimento.git
 **Caso:** RetailAndina, Estadística y Programación para Ciencia de Datos I · 2026-B · Práctica 3 (Tópico 3)

## 1. Pregunta e hipótesis

Ubicar el producto estrella de RetailAndina S.A. en el **pasillo principal** incrementa el promedio semanal de **unidades vendidas** por tienda en comparación con mantenerlo en su **ubicación habitual**, evaluado a lo largo de un horizonte experimental de **4 semanas** consecutivas bajo condiciones operativas equivalentes.

### Formulación operativa y criterio de decisión

* **Condición de contraste:** Exhibición destacada en el **pasillo principal** frente a exhibición regular en la **ubicación habitual**.
* **Métrica de evaluación:** Promedio de **unidades vendidas** del producto estrella por semana-tienda, complementado con el análisis pareado de la diferencia media entre ambas condiciones dentro de cada tienda.
* **Horizonte temporal:** Seguimiento semanal durante **4 semanas** consecutivas, alternando la condición asignada por semana dentro de cada tienda.
* **Sentido de la comparación:** Se busca determinar si el cambio al **pasillo principal** produce un incremento positivo y consistente en las ventas respecto a la **ubicación habitual** en el mismo establecimiento.


## 2. Unidad experimental

* **Unidad experimental:** **Semana-tienda**, definida como cada combinación individual de tienda y semana calendario en la que se aplica una condición de ubicación específica.
* **Tamaño muestral:** $N = 40$ semanas-tienda, obtenidas al observar **10 tiendas** de la cadena durante **4 semanas**, con **20 unidades** asignadas a `pasillo_principal` y **20 unidades** asignadas a `habitual`.

### Justificación técnica y operativa

El diseño abarca 10 locales representativos en distintas ciudades del país durante 4 semanas, logrando un balance exacto en el que cada tienda experimenta **2 semanas** en `pasillo_principal` y **2 semanas** en `habitual`. Esta estructura permite realizar comparaciones pareadas dentro de cada tienda, controlar diferencias estructurales de tamaño o demanda base entre locales y alcanzar $N = 40$ observaciones sin comprometer todo el inventario simultáneamente.

## 3. Factor, niveles y tratamiento

* **Factor:** Ubicación física del producto estrella dentro del piso de venta.
* **Niveles del factor:**
  * **`pasillo_principal`:** Exhibición destacada en el corredor principal de alto flujo peatonal.
  * **`habitual`:** Anaquel o góndola estándar donde el producto se comercializa regularmente.
* **Tratamiento:** Asignar y mantener físicamente el producto estrella en el nivel **`pasillo_principal`** durante las semanas sorteadas para cada tienda, mientras que en las semanas restantes la misma tienda opera bajo el nivel **`habitual`**.

### Distinción conceptual

El **pasillo principal** es un nivel del factor de ubicación y no el tratamiento en sí. El **tratamiento** consiste en la intervención efectiva sobre la unidad semana-tienda al trasladar y sostener el producto en ese nivel durante toda la semana asignada.

## 4. Grupo de control

* **Definición del grupo de control:** Conjunto de **20 semanas-tienda** en las que el producto estrella permanece en su **ubicación habitual** sin modificaciones en su exhibición ordinaria.
* **Rol en el diseño:** Actúa como referencia contrafactual directa tanto a nivel agregado como dentro de cada tienda. Dado que cada local pasa 2 semanas en `habitual` y 2 semanas en `pasillo_principal` en secuencias alternadas aleatoriamente, el grupo de control permite aislar el efecto propio de la ubicación frente a la demanda base de cada tienda y la tendencia semanal general.

## 5. Aleatorización

* **Método y justificación:** Aleatorización balanceada por tienda mediante un esquema cruzado alternado con semilla fija `1234597`. Para cada una de las 10 tiendas se sortea aleatoriamente la condición inicial de la semana 1 entre `pasillo_principal` y `habitual`, y se alterna en las semanas siguientes. De este modo, ninguna tienda queda fija en una sola condición, se evita el sesgo de selección administrativa y se garantiza que cada local tenga exactamente 2 semanas de tratamiento y 2 semanas de control.

### Código ejecutado

```python
import pandas as pd
import numpy as np

tiendas = [
    "Quit Norte", "Quito sur", "Guayaquil centro", "Guayaquil norte",
    "Cuenca centro", "Cuenca sur", "ambato centro", "Manta", "Loja", "Machala"
]
semanas = [1, 2, 3, 4]

rng = np.random.default_rng(1234597)
primera = rng.choice(["pasillo_principal", "habitual"], size=len(tiendas))

filas = []
for tienda, cond in zip(tiendas, primera):
    otra = "habitual" if cond == "pasillo_principal" else "pasillo_principal"
    for s in semanas:
        filas.append({
            "tienda": tienda,
            "semana": s,
            "ubicacion": cond if s % 2 == 1 else otra
        })

diseno = pd.DataFrame(filas)
print("Semilla: 1234597")
print(f"Total de unidades experimentales: {len(diseno)}")
print("\nConteo por grupo:")
print(diseno["ubicacion"].value_counts())
print("\nAsignacion por tienda y semana:")
print(diseno.pivot(index="tienda", columns="semana", values="ubicacion"))
```
### Salida de la corrida

* **Semilla:** `1234597`
* **Total de unidades experimentales:** `40`

#### Conteo por grupo

| Ubicación | Unidades asignadas |
| :--- | :---: |
| `habitual` | 20 |
| `pasillo_principal` | 20 |

#### Asignación por tienda y semana

| Tienda | Semana 1 | Semana 2 | Semana 3 | Semana 4 |
| :--- | :--- | :--- | :--- | :--- |
| **Cuenca centro** | `habitual` | `pasillo_principal` | `habitual` | `pasillo_principal` |
| **Cuenca sur** | `habitual` | `pasillo_principal` | `habitual` | `pasillo_principal` |
| **Guayaquil centro** | `habitual` | `pasillo_principal` | `habitual` | `pasillo_principal` |
| **Guayaquil norte** | `habitual` | `pasillo_principal` | `habitual` | `pasillo_principal` |
| **Loja** | `habitual` | `pasillo_principal` | `habitual` | `pasillo_principal` |
| **Machala** | `habitual` | `pasillo_principal` | `habitual` | `pasillo_principal` |
| **Manta** | `habitual` | `pasillo_principal` | `habitual` | `pasillo_principal` |
| **Quit Norte** | `habitual` | `pasillo_principal` | `habitual` | `pasillo_principal` |
| **Quito sur** | `habitual` | `pasillo_principal` | `habitual` | `pasillo_principal` |
| **ambato centro** | `habitual` | `pasillo_principal` | `habitual` | `pasillo_principal` |


## 6. Respuesta y medición

* **Variable respuesta:** Número total de **unidades vendidas** del producto estrella registradas en cada semana-tienda.
* **Período y responsable de registro:** Acumulado semanal de lunes a domingo, extraído directamente del sistema de punto de venta POS y auditado por el equipo de *Business Intelligence* junto con la administración de cada local.
* **Condición de ciego:** No es posible aplicar ciego a clientes ni al personal de tienda debido a que la exhibición en el **pasillo principal** es visible en el piso de venta. Para minimizar el sesgo de medición o reporte manual, los datos se obtienen de forma automatizada desde las transacciones reales del POS y se concilian con el inventario semanal.
## 7. Factores a controlar (mínimo 4)

| Factor | Riesgo experimental | Mecanismo de control, bloqueo o registro |
| :--- | :--- | :--- |
| **Efecto tienda** | Diferencias de tamaño, ciudad y demanda base entre los 10 locales | Bloqueo dentro de cada tienda asignando 2 semanas de tratamiento y 2 de control por local. |
| **Tendencia semanal o temporada** | Variación natural de ventas entre la semana 1 y la semana 4 | Alternancia aleatorizada de condición inicial entre tiendas para repartir ambas condiciones a lo largo de las 4 semanas. |
| **Promociones simultáneas** | Descuentos o campañas locales que elevan artificialmente las ventas | Estandarización de condiciones comerciales y registro explícito en la columna `promocion_simulacion` para detectar o ajustar eventos puntuales. |
| **Disponibilidad de stock** | Quiebres de inventario que limiten la venta real durante la semana | Monitoreo diario de inventario y reposición oportuna en ambos niveles de ubicación. |
| **Precio unitario** | Cambios de precio que modifiquen la demanda del producto | Mantener el mismo precio de lista en las 10 tiendas durante las 4 semanas. |

## 8. Limitaciones del diseño

* **Falta de ciego en piso:** Clientes y colaboradores perciben el cambio de exhibición, lo que puede generar un efecto novedad transitorio o mayor atención operativa cuando el producto está en el **pasillo principal**.
* **Posible efecto arrastre entre semanas:** Al alternar semanas dentro de una misma tienda, compras adelantadas o recordación del cliente tras una semana en el pasillo principal pueden influir parcialmente en la semana siguiente en ubicación habitual.
* **Interferencia de eventos locales:** Si ocurre una promoción puntual o evento externo en una semana-tienda específica, puede distorsionar el promedio individual si no se registra y controla adecuadamente.
* **Validez externa acotada:** Los hallazgos se aplican al producto estrella y a las 10 tiendas evaluadas durante el horizonte de 4 semanas, sin garantizar el mismo impacto en productos de baja rotación o temporadas atípicas.

## 9. Comparación en código (Python)

### Código ejecutado

```python
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
```

### Salida obtenida

* **Total de filas leídas:** `4`

#### Datos del registro (`plantillas/registro_experimento.csv`)

| unidad_id | tienda | semana | ubicacion | ventas_producto |
| :--- | :--- | :---: | :--- | :---: |
| U01 | Quito Norte | 1 | `pasillo_principal` | 310 |
| U02 | Quito Norte | 2 | `habitual` | 265 |
| U03 | Quito Sur | 1 | `pasillo_principal` | 290 |
| U04 | Quito Sur | 2 | `habitual` | 250 |

#### Resumen por grupo

| ubicacion | n | media | sd | min | max |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `habitual` | 2 | 257.5 | 10.61 | 250 | 265 |
| `pasillo_principal` | 2 | 300.0 | 14.14 | 290 | 310 |

### Interpretación de los límites del análisis

Con apenas **4 filas** en `plantillas/registro_experimento.csv`, el promedio calculado por grupo **no prueba nada**. Este archivo cumple únicamente la función de plantilla de formato para verificar la estructura de registro y la ejecución del script:

* **Ausencia de potencia estadística:** Con solo dos observaciones por grupo no es posible estimar con fiabilidad la media real ni la variabilidad entre tiendas y semanas.
* **Vulnerabilidad total a valores extremos:** Un solo registro atípico altera por completo el promedio de un grupo.
* **Sin validez inferencial:** A diferencia del diseño completo de $N = 40$ unidades pareadas en las 10 tiendas, una tabla de 4 filas no permite realizar pruebas de hipótesis ni respaldar decisiones gerenciales.
