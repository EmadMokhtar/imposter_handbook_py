from algorithm import bellman_ford

vertices = ["S", "A", "B", "C", "D", "E"]

edges = [
    {"from": "S", "to": "A", "cost": 4},
    {"from": "S", "to": "E", "cost": -5},
    {"from": "A", "to": "C", "cost": 6},
    {"from": "B", "to": "A", "cost": 3},
    {"from": "C", "to": "B", "cost": -2},
    {"from": "D", "to": "C", "cost": 3},
    {"from": "D", "to": "A", "cost": 10},
    {"from": "E", "to": "D", "cost": 8},
]

result = bellman_ford(vertices, edges)
print(result)