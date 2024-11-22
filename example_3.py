import numpy as np

# 1. Generación de datos y transformación
# Generar scores para 100 estudiantes en 5 materias (0-100)
scores = np.random.uniform(0, 100, size=(100, 5))

# Calcular y añadir la columna de promedio
promedios = np.mean(scores, axis=1)
dataset = np.concatenate((scores, promedios.reshape(-1, 1)), axis=1)

# 2. Análisis estadístico
# Calcular estadísticas para cada materia (primeras 5 columnas)
medias = np.mean(dataset[:, :5], axis=0)
medianas = np.median(dataset[:, :5], axis=0)
desviaciones = np.std(dataset[:, :5], axis=0)

print("Estadísticas por materia:")
print("Medias:", medias)
print("Medianas:", medianas)
print("Desviaciones:", desviaciones)

# Encontrar y reemplazar scores del top 10%
percentil_90 = np.percentile(dataset[:, -1], 90)
top_estudiantes = dataset[:, -1] >= percentil_90
maximos_materias = np.max(dataset[:, :5], axis=0)

# Reemplazar scores del top 10% con máximos
dataset[top_estudiantes, :5] = maximos_materias

# 3. Reshape y ordenamiento
# Reshape a 20x30
dataset_reshape = dataset.reshape(20, 30)
# Ordenar cada fila
dataset_reshape.sort(axis=1)

# 4. Análisis avanzado y masking
# Volver al shape original para continuar el análisis
dataset = dataset_reshape.reshape(100, 6)

# Reemplazar scores < 40 con la media de la materia
for i in range(5):  # Para cada materia
   mask_bajos = dataset[:, i] < 40
   dataset[mask_bajos, i] = medias[i]

# Encontrar scores únicos en orden descendente
scores_unicos = np.unique(dataset[:, :5])
scores_unicos = np.sort(scores_unicos)[::-1]  # Ordenar descendente

# Mostrar resultados
print("\nForma del dataset final:", dataset.shape)
print("\nPrimeras filas del dataset modificado:")
print(dataset[:5])
print("\nScores únicos (descendente):")
print(scores_unicos)

# Estadísticas adicionales
print("\nEstadísticas finales:")
print("Número de estudiantes en top 10%:", np.sum(top_estudiantes))
print("Número de scores únicos:", len(scores_unicos))