# Lección 8 — Soluciones

## Ejercicio 1: Solución: Primer DataFrame

```
import pandas as pd
df = pd.DataFrame({
    "producto":["A","B","C","D","E"],
    "precio":[10,25,60,5,30],
    "categoria":["x","y","x","z","y"]
})
print(df[df["precio"]>20][["producto","precio"]])
```

## Ejercicio 2: Solución: CSV → DataFrame → JSON

```
import pandas as pd
df = pd.read_csv("productos.csv", encoding="utf-8")
print(df.info())
subset = df[["nombre","precio"]]
subset.to_json("subset.json", orient="records", force_ascii=False, indent=2)
```

## Ejercicio 3: Solución: Agrupamiento

```
import pandas as pd
df = pd.DataFrame({
    "producto":["A","B","C","D","E"],
    "precio":[10,25,60,5,30],
    "categoria":["x","y","x","z","y"]
})
print(df.groupby("categoria")["precio"].agg(["count","mean"]))
```
