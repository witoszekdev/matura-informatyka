# Algorytm Dijkstry


def dijkstra(graph):
    parents = {}
    costs = {}
    processed = []
    # load initial data
    for node in graph.keys():
        costs[node] = float("inf")
    for neighbour in graph["start"].keys():
        parents[neighbour] = "start"
        costs[neighbour] = graph["start"][neighbour]
    parents["start"] = None

    # finding lowest node
    def find_lowest_cost_node():
        lowest_cost = float("inf")
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    node = find_lowest_cost_node()
    while node is not None:
        cost = costs[node]
        neighbours = graph[node]
        for neighbour in neighbours.keys():
            new_cost = cost + neighbours[neighbour]
            if costs[neighbour] > new_cost:
                costs[neighbour] = new_cost
                parents[neighbour] = node
        processed.append(node)
        node = find_lowest_cost_node()

    # display the shortest route from calculated consts
    print("koszt dotarcia do mety: ", costs["meta"])
    print("ścieżka do mety: ")

    results = []
    node = "meta"
    while node is not None:
        results.append(node)
        node = parents[node]

    for result in results[::-1]: # array in reverse
        if result == "meta":
            print("meta")
        else:
            print(result, end=' -> ')

if __name__ == "__main__":
    # wymóg: wierzchołek początkowy musi się nazywać "start", a końcowy "meta"!
    graph = {
        "start": {
            "A": 4,
            "B": 2
        },
        "A": {
            "C": 6
        },
        "B": {
            "C": 7,
        },
        "C": {
            "D": 2,
            "E": 6
        },
        "D": {
            "meta": 10
        },
        "E": {
            "meta": 3
        },
        "meta": {}
    }
    dijkstra(graph)
