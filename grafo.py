import networkx as nx
import matplotlib.pyplot as plt

def create_directed_graph():
    # Crear un grafo dirigido
    G = nx.DiGraph()
    
    # Agregar los nodos
    nodes = range(1, 21)  # Nodos del 1 al 20
    G.add_nodes_from(nodes)
    
    # Agregar las aristas según el diagrama
    edges = [
        (1, 2), (1, 4), (1, 3),
        (2, 5), (2, 6),
        (3, 15), (3, 17),
        (4, 7),
        (5, 6),
        (6, 11),
        (7, 8),
        (8, 10),
        (10, 13),
        (11, 12),
        (12, 14),
        (13, 14),
        (14, 19),
        (15, 16),
        (16, 19),
        (17, 18),
        (18, 20),
        (19, 20)
    ]
    G.add_edges_from(edges)
    
    return G

def visualize_graph(G):
    # Configurar el tamaño de la figura
    plt.figure(figsize=(12, 8))
    
    # Establecer el layout del grafo
    pos = nx.spring_layout(G, k=1, iterations=50)
    
    # Dibujar el grafo
    nx.draw(G, pos,
            with_labels=True,
            node_color='lightblue',
            node_size=500,
            arrowsize=20,
            font_size=12,
            font_weight='bold',
            arrows=True)
    
    # Mostrar el grafo
    plt.title("Grafo Dirigido")
    plt.axis('off')
    return plt

# Crear y visualizar el grafo
G = create_directed_graph()

# Algunas métricas útiles del grafo
print("Número de nodos:", G.number_of_nodes())
print("Número de aristas:", G.number_of_edges())
print("Grados de entrada:", dict(G.in_degree()))
print("Grados de salida:", dict(G.out_degree()))

# Encontrar todos los caminos desde el nodo 1 al nodo 20
paths = list(nx.all_simple_paths(G, 1, 20))
print("\nTodos los caminos posibles del nodo 1 al 20:")
for i, path in enumerate(paths, 1):
    print(f"Camino {i}: {path}")

# Visualizar el grafo
plt = visualize_graph(G)
plt.show()
