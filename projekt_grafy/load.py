def load_graph(board):
    rows, cols = len(board), len(board[0])
    graph = {}

    # Initialize two variables to store special nodes (if any) on the board
    search_1, search_2 = None, None

    for i in range(rows):
        for j in range(cols):
            # Create a unique key for each cell based on its coordinates
            current_key = f"{i},{j}"

            # Check if the current cell is a special node (marked as '0')
            if board[i][j] == 0:
                # Assign the first and second special nodes when found
                if search_1 is None:
                    search_1 = current_key
                else:
                    search_2 = current_key

            # Dictionary to hold the neighbors of the current cell
            neighbors = {}

            # Check and add left and right neighbors
            if j > 0:
                neighbors[f"{i},{j-1}"] = int(board[i][j - 1])
            if j < cols - 1:
                neighbors[f"{i},{j+1}"] = int(board[i][j + 1])

            # Check and add top and bottom neighbors
            if i > 0:
                neighbors[f"{i-1},{j}"] = int(board[i - 1][j])
            if i < rows - 1:
                neighbors[f"{i+1},{j}"] = int(board[i + 1][j])

            # Add the current cell and its neighbors to the graph
            graph[current_key] = neighbors

    return graph, search_1, search_2


def load_board(path):
    with open(path) as f:
        # Read each line, strip off newline characters, and create a list of characters
        lines = [list(line.strip("\\\n")) for line in f]
        # Convert each character to an integer to form the board
        lines = [[int(char) for char in row] for row in lines]
    if not lines:
        return lines

    first_list_length = len(lines[0])
    for inner_list in lines:
        if len(inner_list) != first_list_length:
            print("Bad format of list")
            return []  # Found an inner list with a different length

    return lines  # All inner lists have the same length
