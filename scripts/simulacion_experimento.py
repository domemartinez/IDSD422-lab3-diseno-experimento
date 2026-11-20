import pandas as pd
import numpy as np
import json
from scipy import stats

tiendas = [
    "Quit Norte", "Quito sur", "Guayaquil centro", "Guayaquil norte",
    "Cuenca centro", "Cuenca sur", "ambato centro", "Manta", "Loja", "Machala"
]
semanas = [1, 2, 3, 4]

rng = np.random.default_rng(1234597)
primera = rng.choice(["pasillo_principal", "habitual"], size=len(tiendas))

filas = []
# 1. Primero construimos todas las filas de todas las tiendas y semanas
for tienda, cond in zip(tiendas, primera):
    otra = "habitual" if cond == "pasillo_principal" else "pasillo_principal"
    for s in semanas:
        filas.append({
            "tienda": tienda,
            "semana": s,
            "ubicacion": cond if s % 2 == 1 else otra
        })

# 2. Fuera de los bucles, creamos el DataFrame completo
diseno = pd.DataFrame(filas)
print(diseno.head())

# 3. Simulamos las ventas para todo el DataFrame
rng = np.random.default_rng(1234598)
efecto_tienda = dict(zip(tiendas, rng.normal(1100, 120, len(tiendas))))
efecto_semana = {1: 0, 2: 30, 3: 60, 4: 90}

diseno["ventas_producto"] = (
    diseno["tienda"].map(efecto_tienda) +
    diseno["semana"].map(efecto_semana) +
    (diseno["ubicacion"] == "pasillo_principal") * 220 +
    rng.normal(0, 90, len(diseno))
).round(0).astype(int)

# 4. Promoción simultánea registrada
diseno["promocion_simulacion"] = "no"
diseno.loc[(diseno["tienda"] == "Guayaquil centro") & (diseno["semana"] == 1), "promocion_simulacion"] = "si"
diseno.loc[diseno["promocion_simulacion"] == "si", "ventas_producto"] += 180

diseno.to_csv("resultado_simulacion.csv", index=False)

# 5. Análisis pareado: una fila por tienda con sus condiciones
piv = diseno.groupby(["tienda", "ubicacion"])["ventas_producto"].mean().unstack()
print("Columnas de la tabla pivote:", piv.columns)

# Corregimos la resta con el operador '-' y aseguramos las dos columnas
piv["diferencia"] = piv["pasillo_principal"] - piv["habitual"]

media = piv["diferencia"].mean()
dev = piv["diferencia"].std(ddof=1)

print("Media de las diferencias:", media)
print("Desviación estándar:", dev)
n = len(piv)

t_critic = stats.t.ppf(0.975, df=9)
ic_inf = media - (t_critic * dev / n**0.5)
ic_sup = media + (t_critic * dev / n**0.5)
print("IC 95% inferior:", ic_inf)
print("IC 95% superior:", ic_sup)
