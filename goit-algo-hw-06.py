##### ДЗ. Тема 6. Графи

### Завдання 1

'''

Створіть граф за допомогою бібліотеки networkX для моделювання певної реальної мережі (наприклад, транспортної мережі міста, соціальної мережі, інтернет-топології).

info
📖 Реальну мережу можна вибрати на свій розсуд, якщо немає можливості придумати свою мережу, наближену до реальності.
Візуалізуйте створений граф, проведіть аналіз основних характеристик (наприклад, кількість вершин та ребер, ступінь вершин).

Критерії прийняття:
Створено та візуалізовано граф — модель певної реальної мережі.
Проведено аналіз основних характеристик.
'''

import networkx as nx
import matplotlib.pyplot as plt

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'E'],
    'E': ['B', 'H'],
    'F': ['C', 'I', 'G'],
    'G': ['C'],
    'H': ['E'],
    'I': ['F']
}

G = nx.Graph(graph)
print(G)

# Кількість вершин та ребер графа
number_of_nodes = G.number_of_nodes() 
number_of_edges = G.number_of_edges()
print(number_of_nodes)  # 9 вершини
print(number_of_edges)  # 10 ребр

# Ступінь кожної з вершин
for node in G.nodes():
    node_degree = len(list(G.neighbors(node)))
    print(f'node_degree for node {node} = {node_degree}')

'''
Виведення:

node_degree for node A = 2
node_degree for node B = 3
node_degree for node C = 3
node_degree for node D = 2
node_degree for node E = 3
node_degree for node F = 3
node_degree for node G = 2
node_degree for node H = 1
node_degree for node I = 1
'''

import pydot
from networkx.drawing.nx_pydot import graphviz_layout

# Візуалізація графа завдання 2
pos = graphviz_layout(G, prog="dot")  #  https://graphviz.org/download/ -> add to Path
options = {
    "node_color": "lightgreen",
    "edge_color": "lightblue",
    "node_size": 500,
    "width": 3,
    "with_labels": True
    }
nx.draw(G, pos, **options)
plt.show()


### Завдання 2
'''
Напишіть програму, яка використовує алгоритми DFS і BFS для знаходження шляхів у графі, який було розроблено у першому завданні.
Далі порівняйте результати виконання обох алгоритмів для цього графа, висвітлить різницю в отриманих шляхах. Поясніть, чому шляхи для алгоритмів саме такі.

Критерії прийняття:
Програмно реалізовано алгоритми DFS і BFS для знаходження шляхів у графі, який було розроблено у першому завданні.
Здійснено порівняння результатів алгоритмів для цього графа, пояснено різницю в отриманих шляхах. Обґрунтовано, чому шляхи для алгоритмів саме такі.
Висновки оформлено у вигляді файлу readme.md домашнього завдання.
'''

# DFS
dfs_tree = nx.dfs_tree(G, source='A')
dfs_tree_search_way = list(dfs_tree.edges()) 
print(f'DFS_tree search way \n {dfs_tree_search_way}')  # виведе ребра DFS-дерева з коренем у вузлі A

# BFS
bfs_tree = nx.bfs_tree(G, source='A')
bfs_tree_search_way = list(bfs_tree.edges())
print(f'BFS_tree search way \n {bfs_tree_search_way}')  # виведе ребра BFS-дерева з коренем у вузлі A


# У цьому завданні реалізовано два пошукові алгоритми — глибини (DFS) та ширини (BFS) — для графа, створеного в Завданні 1. 
# Ми побудували дерева обходу, які демонструють, у якому порядку алгоритми обходять вузли та які ребра використовуються для формування дерева пошуку.

# ## Результати
#     * DFS (Depth-First Search) DFS_tree search way   [('A', 'B'), ('B', 'D'), ('D', 'E'), ('E', 'H'), ('A', 'C'), ('C', 'F'), ('F', 'I'), ('F', 'G')]
#     * BFS (Breadth-First Search) BFS_tree search way [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G'), ('E', 'H'), ('F', 'I')]

#     * Пояснення різниці
#         ** DFS (обхід у глибину) прямує якомога глибше по одній гілці, перш ніж повернутись назад. Це видно у результаті: спочатку він повністю проходить шлях A → B → D → E → H, і лише потім повертається до вузла A та переходить до C.
#         ** BFS (обхід у ширину) проходить усіх сусідів поточного вузла, перш ніж переходити до наступного рівня. У результаті BFS одразу відкриває вузли B і C з A, потім D, E, F, G і далі.

# ## Висновок
# * DFS підходить для задач, де потрібно дістатися до глибоких вузлів, або знайти будь-який шлях до цілі.
# * BFS ефективніший, коли потрібно знайти найкоротший шлях у графі (у кількості кроків).
# * Обидва алгоритми генерують дерево пошуку, яке залежить від порядку обходу сусідів. Якщо ви хочете контролювати точний порядок — варто задавати sorted() або вручну впорядкований список суміжностей.




### Завдання 3
'''
Реалізуйте алгоритм Дейкстри для знаходження найкоротшого шляху в розробленому графі: додайте у граф ваги до ребер та знайдіть найкоротший шлях між всіма вершинами графа.

Критерії прийняття:
У граф додано ваги ребер, програмно реалізовано алгоритм Дейкстри для знаходження найкоротшого шляху в розробленому графі.
'''

# Додаємо ваги до ребер графу
G['A']['B']['weight'] = 1
G['A']['C']['weight'] = 2
G['B']['D']['weight'] = 3
G['B']['E']['weight'] = 4
G['C']['F']['weight'] = 5
G['C']['G']['weight'] = 1
G['D']['E']['weight'] = 2
G['E']['H']['weight'] = 3
G['F']['I']['weight'] = 4
G['F']['G']['weight'] = 1


# Застосування алгоритму Дейкстри
shortest_paths = nx.single_source_dijkstra_path(G, source='A')
shortest_path_lengths = nx.single_source_dijkstra_path_length(G, source='A')

print(f'Найкоротші шляхи від вузла \'A\' до всіх інших вузлів: {shortest_paths}')                 # виведе найкоротші шляхи від вузла 'A' до всіх інших вузлів
print(f'Довжини найкоротших шляхів від вузла \'A\' до всіх інших вузлів{shortest_path_lengths}')  # виведе довжини найкоротших шляхів від вузла 'A' до всіх інших вузлів


# Візуалізація графа завдання 3

import pydot
from networkx.drawing.nx_pydot import graphviz_layout

labels = nx.get_edge_attributes(G, 'weight')
pos = graphviz_layout(G, prog="dot")  #  https://graphviz.org/download/ -> add to Path
options = {
    "node_color": "lightgreen",
    "edge_color": "lightblue",
    "node_size": 500,
    "width": 3,
    "with_labels": True
    }

nx.draw(G, pos, **options)
# Окремо підписуємо ваги ребер
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
