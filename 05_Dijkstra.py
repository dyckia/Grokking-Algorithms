# global variable
processed = []  # processed node history


def next_lowest_node(costs):
    global processed
    lowest_cost = float("inf")
    lowest_node = None
    for node in costs:
        if lowest_cost > costs[node] and node not in processed:
            lowest_node = node
            lowest_cost = costs[node]
    return lowest_node


def dijkstra(graph, costs, parents):
    global processed
    node = next_lowest_node(costs)
    while node is not None:
        for neighbor in graph[node]:
            new_cost = costs[node] + graph[node][neighbor]
            if costs[neighbor] > new_cost:
                costs[neighbor] = new_cost
                parents[neighbor] = node
        processed.append(node)
        node = next_lowest_node(costs)
    return costs, parents


if __name__ == "__main__":
    # the graph dictionary
    graph = {}
    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2

    graph["a"] = {}
    graph["a"]["fin"] = 1

    graph["b"] = {}
    graph["b"]["a"] = 3
    graph["b"]["fin"] = 5

    graph["fin"] = {}

    # the cost dictionary
    costs = {}
    costs["a"] = 6
    costs["b"] = 2
    costs["fin"] = float("inf")

    # the parents dictionary
    parents = {}
    parents["a"] = "start"
    parents["b"] = "start"
    parents["fin"] = None

    costs, parents = dijkstra(graph, costs, parents)

    print(costs)
    print(parents)
