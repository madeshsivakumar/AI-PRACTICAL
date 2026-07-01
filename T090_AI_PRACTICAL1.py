#A) Implement the Breadth First Search algorithm to solve a given problem.
print("T090_MADESH SIVAKUMAR")
from collections import deque

# Graph represented as an adjacency list
city_map = {
    'College': ['Bus Stop', 'Library'],
    'Bus Stop': ['Market'],
    'Library': ['Hospital'],
    'Market': ['Railway Station'],
    'Hospital': ['Mall'],
    'Railway Station': ['Airport'],
    'Mall': ['Airport'],
    'Airport': []
}

# A) Breadth First Search (BFS)
def bfs_shortest_path(graph, start, destination):
    queue = deque([(start, [start])])
    visited = set([start])
    nodes_explored_count = 0

    while queue:
        current, path = queue.popleft()
        nodes_explored_count += 1

        if current == destination:
            return path, nodes_explored_count

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None, nodes_explored_count


# B) Iterative Depth First Search (DFS)
def iterative_dfs_path(graph, start, destination):
    stack = [(start, [start])]
    visited = set()
    nodes_explored_count = 0

    while stack:
        current, path = stack.pop()
        nodes_explored_count += 1

        if current == destination:
            return path, nodes_explored_count

        if current not in visited:
            visited.add(current)

            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return None, nodes_explored_count


# Execution
start_node = 'College'
end_node = 'Airport'

bfs_path, bfs_count = bfs_shortest_path(city_map, start_node, end_node)
dfs_path, dfs_count = iterative_dfs_path(city_map, start_node, end_node)

print("----- BFS Results -----")
print("Path Found:", " -> ".join(bfs_path))
print("Total Steps (Edges):", len(bfs_path) - 1)
print("Total Nodes Visited:", bfs_count)

print("\n----- DFS Results -----")
print("Path Found:", " -> ".join(dfs_path))
print("Total Steps (Edges):", len(dfs_path) - 1)
print("Total Nodes Visited:", dfs_count)
