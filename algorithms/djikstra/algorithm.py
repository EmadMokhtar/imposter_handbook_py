import math


class MemoTable:
    def __init__(self, vertices):
        self.S = {"name": "S", "cost": 0, "visited": False}
        self.table = [self.S]
        for vertex in vertices:
            self.table.append({"name": vertex, "cost": math.inf,
                               "visited": False})

    def get_candidate_vertices(self):
        return [v for v in self.table if not v['visited']]

    def next_vertex(self):
        candidates = self.get_candidate_vertices()
        if not candidates:
            return None
        return min(candidates, key=lambda x: x.get('cost'))

    def set_current_cost(self, vertex_name, cost):
        self.get_entry(vertex_name)['cost'] = cost

    def set_as_visited(self, vertex_name):
        self.get_entry(vertex_name)['visited'] = True

    def get_entry(self, vertex_name):
        for v in self.table:
            if v['name'] == vertex_name:
                return v
        return None

    def get_cost(self, vertex_name):
        return self.get_entry(vertex_name).get('cost')

    def __str__(self):
        return str(self.table)
