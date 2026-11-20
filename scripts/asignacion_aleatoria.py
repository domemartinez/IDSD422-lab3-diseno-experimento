import random

SEMILLA = 42
random.seed(SEMILLA)

unidades = [f"unidad_{i:02d}" for i in range(1, 13)]
sorteo = unidades.copy()
random.shuffle(sorteo)

mitad = len(sorteo) // 2
grupo_a = sorted(sorteo[:mitad])
grupo_b = sorted(sorteo[mitad:])

print(f"Semilla: {SEMILLA}")
print("Grupo A (Tratamiento - pasillo principal):", grupo_a)
print("Grupo B (Control - ubicacion habitual):   ", grupo_b)
