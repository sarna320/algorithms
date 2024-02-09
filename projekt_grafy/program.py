import sys
import load
import dijkstra
import draw


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python program.py <file_path>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
        board = load.load_board(file_path)
        for raw in board:
            # print(raw)
            pass
        graph, search_1, search_2 = load.load_graph(board)
        for key in graph:
            # print(f"{key}: {graph[key]}")
            pass
        cost, shortest_path = dijkstra.dijkstra(graph, search_1, search_2)
        # print(shortest_path)
        draw.draw(board, shortest_path)
