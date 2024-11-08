import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Crear una malla de puntos
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)

# Calcular Z
Z = np.sqrt(9 - X**2 - Y**2)

# Manejar valores no definidos (donde x^2 + y^2 > 9)
Z = np.where(np.isreal(Z), Z, np.nan)

# Crear la figura y el eje 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Crear el gráfico de superficie
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

# Configurar etiquetas y título
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Gráfico de Z = √(9 - x² - y²)')

# Añadir una barra de color
fig.colorbar(surf)

# Mostrar el gráfico
plt.show()