from algorithm import MemoTable

vertices = ["A", "B", "C", "D", "E"]
graph = [
    {'from': "S", 'to': "A", 'cost': 4},
    {'from': "S", 'to': "E", 'cost': 2},
    {'from': "A", 'to': "D", 'cost': 3},
    {'from': "A", 'to': "C", 'cost': 6},
    {'from': "A", 'to': "B", 'cost': 5},
    {'from': "B", 'to': "A", 'cost': 3},
    {'from': "C", 'to': "B", 'cost': 1},
    {'from': "D", 'to': "C", 'cost': 3},
    {'from': "D", 'to': "A", 'cost': 1},
    {'from': "E", 'to': "D", 'cost': 1}
]

memo = MemoTable(vertices)


def evaluate(vertex):
    edges = [v for v in graph if v['from'] == vertex['name']]
    for edge in edges:
        current_vertex_cost = memo.get_cost(edge['from'])
        to_vertex_cost = memo.get_cost(edge['to'])
        tentative_cost = current_vertex_cost + edge['cost']
        if tentative_cost < to_vertex_cost:
            memo.set_current_cost(edge['to'], tentative_cost)
    memo.set_as_visited(vertex['name'])
    next_vertex = memo.next_vertex()
    if next_vertex:
        evaluate(next_vertex)


evaluate(memo.S)
print(memo)
