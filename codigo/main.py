import json
import time
from memory_profiler import memory_usage
from trees.binary_tree import BinaryTreeNode
from trees.m_tree import MNode
from trees.ts_tree import TSNode
from graphviz import Digraph

def visualize_binary_tree(node, graph=None):
    if graph is None:
        graph = Digraph()
        graph.attr('node', shape='circle')

    if node:
        # Adiciona o nó atual ao gráfico com um rótulo que mostra a chave e o valor
        graph.node(str(node.key), label=f"{node.key} ({node.value})")

        # Se existir um filho à esquerda, adicione ao gráfico e conecte com uma linha
        if node.left:
            graph.edge(str(node.key), str(node.left.key))
            visualize_binary_tree(node.left, graph)

        # Se existir um filho à direita, faça o mesmo
        if node.right:
            graph.edge(str(node.key), str(node.right.key))
            visualize_binary_tree(node.right, graph)

    return graph

def visualize_m_tree(node, graph=None, parent=None):
    if graph is None:
        graph = Digraph()
        graph.attr('node', shape='ellipse')
    if node:
        if parent:
            graph.edge(str(parent), str(node.value))
        if node.children:
            for child in node.children:
                visualize_m_tree(child, graph, str(node.value))
    return graph

def visualize_ts_tree(node, graph=None):
    if graph is None:
        graph = Digraph()
        graph.attr('node', shape='circle')
    if node:
        if node.left:
            graph.edge(str(node.date), str(node.left.date))
            visualize_ts_tree(node.left, graph)
        if node.right:
            graph.edge(str(node.date), str(node.right.date))
            visualize_ts_tree(node.right, graph)
    return graph



def load_data_from_json(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    return data['stockData']

def build_binary_tree(data):
    root = None
    for item in data:
        if root is None:
            root = BinaryTreeNode(item['Open'], item['Close'])
        else:
            root.insert(item['Open'], item['Close'])
    return root

def build_m_tree(data):
    if not data:
        return None
    root = MNode(data[0]['Open'])
    for item in data[1:]:
        root.insert(item['Open'])
    return root

def build_ts_tree(data):
    root = None
    for item in data:
        if root is None:
            root = TSNode(item['Date'], item['Close'])
        else:
            root.insert(item['Date'], item['Close'])
    return root

def measure_performance(func, *args, description=""):
    start_time = time.time()
    mem_before = memory_usage(max_iterations=1)
    result = func(*args)
    mem_after = memory_usage(max_iterations=1)
    end_time = time.time()
    print(f"Metodo {func.__name__}:")
    print(f"Tempo de execução: {end_time - start_time:.6f} seconds")
    print(f"Memoria Usada: {mem_after[0] - mem_before[0]:.6f} MiB")
    if result is not None and result != False:
        print(f"{description} Encontrado: {result}")
    else:
        print(f"{description} Não encontrado")
    return result



if __name__ == '__main__':
    json_file_path = 'C:\\xampp\\htdocs\\python\\Trabalho_AED\\codigo\\data_itsa4.json'  
    data = load_data_from_json(json_file_path)


    print("_____________________Metricas criação de arvores_____________________")
    b_tree = measure_performance(build_binary_tree, data, description="Criação Binary Tree")
    m_tree = measure_performance(build_m_tree, data, description="Criação M-Tree")
    ts_tree = measure_performance(build_ts_tree, data, description="Criação TS-Tree")


    new_data = {
        "Date": "2024-06-03",
        "Open": 9.74,
        "High": 9.82,
        "Low": 9.68,
        "Close": 9.69,
        "Adj Close": 9.69,
        "Volume": 9484200
    }


    print("_____________________Metricas inserção de arvores_____________________")
    measure_performance(b_tree.insert, new_data['Open'], new_data['Close'], description="Inserido em Binary Tree")
    measure_performance(m_tree.insert, new_data['Open'], description="Inserido em M-Tree")
    measure_performance(ts_tree.insert, new_data['Date'], new_data['Close'], description="Inserido em TS-Tree")


    print("_____________________Metricas buscas de arvores_____________________")
    measure_performance(b_tree.find, new_data['Open'], description=f"Busca {new_data['Open']} em Binary Tree")
    measure_performance(m_tree.find, new_data['Open'], description=f"Busca {new_data['Open']} em M-Tree")
    measure_performance(ts_tree.find, new_data['Date'], description=f"Busca {new_data['Date']} em TS-Tree")
   

    print("_____________________Metricas remoção de arvores_____________________")
    measure_performance(b_tree.remove, new_data['Open'], description=f"Remoção {new_data['Open']} em Binary Tree")
    measure_performance(m_tree.remove, new_data['Open'], description=f"Remoção {new_data['Open']} em M-Tree")
    measure_performance(ts_tree.remove, new_data['Date'], description=f"Remoção {new_data['Date']} em TS-Tree")


    # Visualizar árvores
    graph_b = visualize_binary_tree(build_binary_tree(data))
    graph_m = visualize_m_tree(build_m_tree(data))
    graph_ts = visualize_ts_tree(build_ts_tree(data))

    # Salvar os gráficos em arquivos de imagem ou PDF
    graph_b.render('C:\\xampp\\htdocs\\python\\Trabalho_AED\\codigo\\output\\binary_tree', view=True)
    graph_m.render('C:\\xampp\\htdocs\\python\\Trabalho_AED\\codigo\\output\\m_tree', view=True)
    graph_ts.render('C:\\xampp\\htdocs\\python\\Trabalho_AED\\codigo\\output\\ts_tree', view=True)