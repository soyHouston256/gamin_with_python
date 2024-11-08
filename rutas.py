import numpy as np
import random 
import matplotlib.pyplot as plt

def generate_clients(n):
    coordinates = np.random.rand(n, 2) * 100  # Coordenadas aleatorias
    demands = np.random.randint(1, 10, size=n)  # Demandas aleatorias
    time_windows = [(np.random.randint(0, 50), np.random.randint(51, 100)) for _ in range(n)]
    return list(zip(coordinates, demands, time_windows))

def plot_routes(routes):
    for route in routes:
        x = [client[0][0] for client in route]
        y = [client[0][1] for client in route]
        plt.plot(x, y, marker='o')
    plt.show()

def generate_routes(clients, num_routes):
    routes = []
    for _ in range(num_routes):
        # Seleccionar un número aleatorio de clientes para la ruta
        num_clients_in_route = random.randint(1, len(clients))
        route_clients = random.sample(clients, num_clients_in_route)
        routes.append(route_clients)
    return routes

# Generar 100 rutas aleatorias
num_routes = 100
clients = generate_clients(25)
routes = generate_routes(clients, num_routes)
plot_routes(routes)