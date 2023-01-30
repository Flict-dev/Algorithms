def dfs(graph: dict, start, end):
    """
    Processed variable need for know which points already processed :)
    """

    processed, parrents = [], {}

    def __find_lowest_node(costs: dict):
        min_cost = float("inf")
        res = None
        for k, v in costs.items():
            if v < min_cost and not k in processed:
                min_cost = v
                res = k
        return res

    def __unpack_parrents(parrents: dict):
        cur, res = parrents[end], ""
        while cur != start:
            res += cur
            cur = parrents[cur]
        return res[::-1]

    """
    Fill parrents table {'B': 'A', 'C': 'A', 'D': None}
    Start point will be the parent for its points 

    Others points will be 'None' parent by default
    """
    for k in filter(lambda x: x != start, graph.keys()):
        if k not in graph[start].keys():
            parrents[k] = None
        else:
            parrents[k] = start

    """
    Fill costs table {'B': 6, 'C': 2, 'D': inf}
    Childs of start point with edge value

    Other points will be with 'inf' value by default
    """
    costs = {k: float("inf") for k in filter(lambda x: x != start, graph.keys())}
    for k, v in graph[start].items():
        costs[k] = v

    # main logic
    node = __find_lowest_node(costs)
    while node is not None:  # while all nodes not in processed
        neighbors = graph[node]
        node_cost = costs[node]
        for k, v in neighbors.items():
            if costs[k] > v + node_cost:  # compare current cost with new
                costs[k] = v + node_cost
                parrents[k] = node
        processed.append(node)
        node = __find_lowest_node(costs)  # next node

    return (start + __unpack_parrents(parrents) + end, costs[end])
