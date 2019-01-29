def find_seller(graph):
    queue = graph['you']
    searched = []  # prevent infinite loop
    while queue:
        name = queue.pop(0)
        searched.append(name)
        if name[-1] == 'c':
            return print('Found cloest seller {}'.format(name))
        else:
            if graph[name]:
                for item in graph[name]:
                    if item not in searched:
                        queue.append(item)
    return print('Couldn\'d find seller')


if __name__ == '__main__':
    # Create Graph
    graph = {}
    graph['you'] = ['alice', 'bob', 'claire']
    graph['alice'] = ['peggy']
    graph['bob'] = ['anuj', 'peggy']
    graph['claire'] = ['thom', 'jonny']
    graph['anuj'] = []
    graph['peggy'] = ['alice']  # create a loop
    graph['thom'] = []
    graph['jonny'] = []
    find_seller(graph)
