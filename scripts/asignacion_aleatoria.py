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
