#5a
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datos.csv')
# Mostrar las primeras filas
print(df.head())

# Mostrar la información general
df.info()

# Mostrar las estadísticas descriptivas
print(df.describe())

#5b
#Obtener al menos 2 datos estadísticos claves (máximo, mínimo, promedio, tendencia) que usarás en la conclusión.

# Obtener dos datos estadísticos claves
print("\nPromedio de ventas globales:")
print(df['Global_Sales'].mean())

print("\nVenta global máxima:")
print(df['Global_Sales'].max())

#6dos gráficos diferentes con Matplotlib
# Gráfico de ventas globales por género
ventas_genero = df.groupby('Genre')['Global_Sales'].sum()

fig, ax = plt.subplots(figsize=(8,5))
barras = ax.bar(ventas_genero.index, ventas_genero.values)

ax.set_title('Ventas globales por género')
ax.set_xlabel('Género')
ax.set_ylabel('Ventas globales')

plt.xticks(rotation=45)
plt.show()

#grafico2
# Gráfico de pastel de ventas por región
regiones = ['Norteamérica', 'Europa', 'Japón', 'Otros']
ventas = [
    df['NA_Sales'].sum(),
    df['EU_Sales'].sum(),
    df['JP_Sales'].sum(),
    df['Other_Sales'].sum()
]

fig, ax = plt.subplots(figsize=(7,7))

ax.pie(
    ventas,
    labels=regiones,
    autopct='%1.1f%%'
)

ax.set_title('Distribución de ventas por región')
ax.axis('equal')

plt.show()

