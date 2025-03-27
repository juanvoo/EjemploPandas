import pandas as pd

# Crear un DataFrame a partir de un diccionario
data = {
    'Nombre': ['Ana', 'Juan', 'Pedro', 'Maria'],
    'Edad': [23, 34, 45, 28],
    'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia']
}

df = pd.DataFrame(data)

# Mostrar el DataFrame
print("DataFrame completo:")
print(df)

# Acceder a una columna
print("\nColumna 'Nombre':")
print(df['Nombre'])

# Filtrar filas según una condición
print("\nPersonas mayores de 30 años:")
print(df[df['Edad'] > 30])

# Agregar una nueva columna
df['Trabajo'] = ['Ingeniera', 'Abogado', 'Médico', 'Diseñadora']

# Mostrar el DataFrame actualizado
print("\nDataFrame con la nueva columna 'Trabajo':")
print(df)
