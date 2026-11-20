# Plantilla de protocolo — Experimento de ubicación de producto

 **Nombre:** Doménica Martínez · **Fecha:** 19/11/2026
 **Repositorio (fork):** https://github.com/domemartinez/IDSD422-lab3-diseno-experimento.git
 **Caso:** RetailAndina, Estadística y Programación para Ciencia de Datos I · 2026-B · Práctica 3 (Tópico 3)

## 1. Pregunta e hipótesis

Ubicar el producto estrella de RetailAndina S.A. en el **pasillo principal** incrementa el promedio de **unidades vendidas** por semana en comparación con mantenerlo en su **ubicación habitual**, durante un período experimental de **1 semana** de operación continua bajo condiciones operativas equivalentes.

### Formulación operativa y criterio de decisión

* **Condición de contraste:** Exhibición destacada en el **pasillo principal** frente a exhibición regular en la **ubicación habitual**.
* **Métrica de evaluación:** Promedio semanal de **unidades vendidas** del producto estrella por unidad experimental, complementado con el registro de ventas brutas y netas para verificar coherencia comercial.
* **Horizonte temporal:** Una ventana cerrada de **1 semana** calendario de lunes a domingo, con medición al cierre del domingo.
* **Sentido de la comparación:** El protocolo busca evaluar si el promedio de unidades vendidas bajo el tratamiento supera al promedio observado en el grupo de control en el mismo período, o si los datos no respaldan una diferencia clara.


## 2. Unidad experimental

* **Unidad experimental:** **Semana-tienda**, entendida como una tienda específica operando durante una semana completa del experimento.
* **Tamaño muestral:** $N = 12$ semanas-tienda, distribuidas de forma balanceada en **6 unidades** para el grupo de tratamiento y **6 unidades** para el grupo de control.

### Justificación técnica y operativa

Elegir **semana-tienda** como unidad experimental permite observar varias tiendas y semanas de manera estructurada, reduciendo el riesgo de que el resultado dependa de un solo local o de un único día atípico. Un tamaño de $N = 12$ unidades ofrece réplicas suficientes en ambas condiciones sin obligar a mover todo el inventario de la cadena de golpe ni sobrecargar la operación diaria de piso. Al tratarse de un protocolo de diseño y no de ejecución en campo, este tamaño es razonable y viable para una evaluación inicial antes de escalar el experimento.

## 3. Factor, niveles y tratamiento

* **Factor:** Ubicación física del producto estrella dentro de la tienda.
* **Niveles del factor:**
  * **Pasillo principal:** Exhibición visible y accesible en el corredor principal de alto flujo peatonal dentro del local.
  * **Ubicación habitual:** Góndola, anaquel o sección estándar donde el producto se comercializa normalmente.
* **Tratamiento:** Asignar de manera efectiva una unidad experimental al nivel **pasillo principal** durante toda la semana prevista, mientras que las unidades del grupo de control mantienen el producto en su **ubicación habitual**.

### Precisión conceptual

El **pasillo principal** corresponde a un nivel del factor de ubicación, no al tratamiento en sí. El **tratamiento** es la intervención aplicada a la unidad experimental al colocar y sostener el producto estrella en ese nivel durante toda la semana del experimento, garantizando una distinción clara frente a la condición de control.

## 4. Grupo de control

* **Definición del grupo de control:** Conjunto de **6 semanas-tienda** en las que el producto estrella permanece en su **ubicación habitual** sin modificar su exhibición ordinaria.
* **Rol dentro del diseño experimental:** Cumple la función de referencia contrafactual simultánea. Permite comparar las ventas obtenidas en el **pasillo principal** frente a lo que habría ocurrido en condiciones normales durante el mismo intervalo temporal, aislando el efecto de la ubicación frente a variaciones generales de demanda, quincenas o fin de mes, clima o tendencias del mercado que afectan a toda la red de tiendas.

## 5. Aleatorización

* **Método y justificación:** Asignación aleatoria con semilla fija para distribuir las unidades experimentales entre tratamiento y control sin intervención discrecional ni sesgo de selección. Al sortear las unidades, se reduce el riesgo de asignar deliberadamente los mejores locales o las mejores semanas al **pasillo principal**, favoreciendo el balance de factores no observados entre ambos grupos.

### Código ejecutado

```python
import random

SEMILLA = 42
random.seed(SEMILLA)

unidades = [f"semana_tienda_{i:02d}" for i in range(1, 13)]
sorteo = unidades.copy()
random.shuffle(sorteo)

mitad = len(sorteo) // 2
grupo_tratamiento = sorted(sorteo[:mitad])
grupo_control = sorted(sorteo[mitad:])

print(f"Semilla: {SEMILLA}")
print(f"Total de unidades: {len(unidades)}")
print("Grupo Tratamiento - pasillo principal:", grupo_tratamiento)
print("Grupo Control - ubicacion habitual:   ", grupo_control)
## 6. Respuesta y medición

- Variable respuesta:
- Período de medición:
- Quién registra y cómo (¿ciego?):

## 7. Factores a controlar (mínimo 4)

| Factor a controlar | Cómo se controla o registra |
|---|---|
| 1. | |
| 2. | |
| 3. | |
| 4. | |

## 8. Limitaciones del diseño

*¿Qué podría invalidar el experimento si no se controla? ¿Qué no se podrá concluir?*

## 9. Comparación en código (Python/R)

*Escribe `scripts/comparacion_experimento.py` (o `.R`): debe cargar `plantillas/registro_experimento.csv` y calcular el promedio de `ventas_producto` por `ubicacion`. Incluye la salida y responde:*

- ¿Qué grupo muestra mayor venta promedio en la plantilla?
- ¿Por qué con 4 filas no se puede concluir nada sobre el efecto de la ubicación?
- Si el experimento se ejecutara con tu protocolo, ¿qué le faltaría a este análisis para ser justo?
