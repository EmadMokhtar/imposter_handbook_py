import math


def bellman_ford(vertices, edges):
    travel_cost = {
        "S": 0,
        "A": math.inf,
        "B": math.inf,
        "C": math.inf,
        "D": math.inf,
        "E": math.inf,
    }
    for i in range(len(vertices)):
        for vertex in vertices:
            v_edges = [e for e in edges if e['from'] == vertex]
            for edge in v_edges:
                cost = travel_cost[edge['from']] + edge['cost']
                if cost < travel_cost[edge['to']]:
                    travel_cost[edge['to']] = cost
    return travel_cost
