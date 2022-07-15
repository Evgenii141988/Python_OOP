class Vertex:
    """ представления вершин графа (на карте это могут быть: здания, остановки, достопримечательности и т.п.)"""

    def __init__(self):
        self._links = []

    @property
    def links(self):
        return self._links


class Link:
    """для описания связи между двумя произвольными вершинами графа (на карте: маршруты, время в пути и т.п.)"""

    def __init__(self, v1: Vertex, v2: Vertex):
        self._v1 = v1
        self._v2 = v2
        self._dist = 1

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, value):
        self._dist = value


class LinkedGraph:
    """для представления связного графа в целом (карта целиком)"""

    def __init__(self):
        self._links = []
        self._vertex = []

    def add_vertex(self, v: Vertex):
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link: Link):
        if self.__check_vertex(link):
            self._links.append(link)
            self.add_vertex(link.v1)
            self.add_vertex(link.v2)
            link.v1.links.append(link)
            link.v2.links.append(link)

    def __check_vertex(self, link: Link):
        return not any(({link.v1, link.v2} == {l.v1, l.v2} for l in self._links))

    def find_path(self, start_v: Vertex, stop_v: Vertex):
        graph = self.get_graph(start_v, stop_v)
        costs = self.get_costs(start_v)
        parents = self.get_parents(start_v)
        processed = []

        vertex = self.find_lowest_cost_vertex(costs, processed)
        while vertex is not None:
            cost = costs[vertex]
            neighbors = graph[vertex]
            for n in neighbors.keys():
                new_cost = cost + neighbors[n]
                if costs[n] > new_cost:
                    costs[n] = new_cost
                    parents[n] = vertex
            processed.append(vertex)
            vertex = self.find_lowest_cost_vertex(costs, processed)
        res_vertexes = self.get_result_vertexes(stop_v, parents)
        res_links = self.get_result_links(res_vertexes, self._links)
        return res_vertexes, res_links

    @staticmethod
    def get_result_links(res_vertexes: list, links):
        res_links = []
        for i in range(len(res_vertexes) - 1):
            for link in links:
                if {link.v1, link.v2} == {res_vertexes[i], res_vertexes[i + 1]}:
                    res_links.append(link)
                    break
        return res_links

    @staticmethod
    def get_result_vertexes(stop_v: Vertex, parents: dict):
        res_vertexes = [stop_v]
        vertex = stop_v
        while vertex in parents:
            vertex = parents[vertex]
            res_vertexes.append(vertex)
        return res_vertexes[::-1]

    @staticmethod
    def find_lowest_cost_vertex(costs: dict, processed: list):
        lowest_cost = float('inf')
        lowest_cost_vertex = None
        for vertex in costs:
            cost = costs[vertex]
            if cost < lowest_cost and vertex not in processed:
                lowest_cost = cost
                lowest_cost_vertex = vertex
        return lowest_cost_vertex

    def get_graph(self, start_v: Vertex, stop_v: Vertex):
        graph = {}
        for vertex in self._vertex:
            graph[vertex] = {}
            for link in vertex.links:
                neighbor_v = link.v2 if link.v1 == vertex else link.v1
                if neighbor_v != start_v:
                    graph[vertex][neighbor_v] = link.dist
        graph[stop_v] = {}
        return graph

    def get_costs(self, start_v: Vertex):
        infinity = float('inf')
        costs = {}
        neighbors = {link.v2 if link.v1 == start_v else link.v1: link.dist for link in start_v.links}
        for vertex in self._vertex:
            if vertex != start_v:
                costs[vertex] = infinity if vertex not in neighbors else neighbors[vertex]
        return costs

    def get_parents(self, start_v: Vertex):
        parents = {}
        neighbors = [link.v2 if link.v1 == start_v else link.v1 for link in start_v.links]
        for vertex in self._vertex:
            if vertex != start_v:
                parents[vertex] = start_v if vertex in neighbors else None
        return parents


class Station(Vertex):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class LinkMetro(Link):
    def __init__(self, v1: Station, v2: Station, dist: (int, float)):
        super().__init__(v1, v2)
        self.dist = dist


if __name__ == '__main__':
    map_metro = LinkedGraph()
    v1 = Station("Сретенский бульвар")
    v2 = Station("Тургеневская")
    v3 = Station("Чистые пруды")
    v4 = Station("Лубянка")
    v5 = Station("Кузнецкий мост")
    v6 = Station("Китай-город 1")
    v7 = Station("Китай-город 2")

    map_metro.add_link(LinkMetro(v1, v2, 1))
    map_metro.add_link(LinkMetro(v2, v3, 1))
    map_metro.add_link(LinkMetro(v1, v3, 1))

    map_metro.add_link(LinkMetro(v4, v5, 1))
    map_metro.add_link(LinkMetro(v6, v7, 1))

    map_metro.add_link(LinkMetro(v2, v7, 5))
    map_metro.add_link(LinkMetro(v3, v4, 3))
    map_metro.add_link(LinkMetro(v5, v6, 3))

    print(len(map_metro._links))
    print(len(map_metro._vertex))
    path = map_metro.find_path(v1, v6)  # от сретенского бульвара до китай-город 1
    print(path[0])  # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
    print(sum([x.dist for x in path[1]]))  # 7

    # print(v1)
    # print(map_metro.get_graph(v1, v6))
    # print(map_metro.get_costs(v1))
    # print(map_metro.get_parents(v1))
    # print()

    # map_metro.find_path(v1, v6)
