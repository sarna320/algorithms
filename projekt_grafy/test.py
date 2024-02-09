import dijkstra


def run_dijkstra_tests():
    def assert_equal(actual, expected, message):
        assert actual == expected, message

    # Define a basic test graph
    graph = {
        "A": {"B": 1, "C": 4},
        "B": {"A": 1, "C": 2, "D": 5},
        "C": {"A": 4, "B": 2, "D": 1},
        "D": {"B": 5, "C": 1},
    }

    # Test 1: Basic Functionality
    cost, path = dijkstra.dijkstra(graph, "A", "D")
    assert_equal(cost, 4, "Basic Functionality: Cost incorrect")
    assert_equal(path, ["A", "B", "C", "D"], "Basic Functionality: Path incorrect")

    # Test 2: No Path Available
    cost, path = dijkstra.dijkstra(graph, "A", "E")
    assert_equal(cost, float("inf"), "No Path: Cost should be infinite")
    assert_equal(path, [], "No Path: Path should be empty")

    # Test 3: Start Equals End
    cost, path = dijkstra.dijkstra(graph, "A", "A")
    assert_equal(cost, 0, "Start Equals End: Cost should be 0")
    assert_equal(path, ["A"], "Start Equals End: Path should be ['A']")

    # Additional tests (Large Graph, Graph with Loops, Negative Weights, etc.) go here

    print("All tests passed!")


if __name__ == "__main__":
    run_dijkstra_tests()
