import heapq


def dijkstra(graph, start, end):
    # Initialize a min heap with a tuple (cost, current node, path)
    min_heap = [(0, start, [])]
    # Set of visited nodes
    visited = set()

    while min_heap:
        # Extract the tuple from the min heap
        (cost, node, path) = heapq.heappop(min_heap)

        # Check if the node has not been visited before
        if node not in visited:
            # Add the node to the set of visited nodes
            visited.add(node)
            # Append the node to the current path
            path = path + [node]

            # Check if the target node is reached
            if node == end:
                return cost, path

            # Iterate over the neighbors of the current node
            for next_node, weight in graph[node].items():
                # Check if the neighbor has not been visited before
                if next_node not in visited:
                    # Add the neighbor to the min heap with the cumulative cost
                    heapq.heappush(min_heap, (cost + weight, next_node, path))

    # Return infinite value and empty path if the target cannot be reached
    return float("inf"), []
