def draw(board, shortest_path):
    for i in range(len(board)):
        for j in range(len(board[i])):
            # Check if the current position is part of the shortest path
            # print(f"{i}{j}")

            if f"{i},{j}" in shortest_path:
                # If it is part of the path, print the element without moving to a new line
                print(board[i][j], end=" ")
                # print(f"{i},{j}")
            else:
                # If it's not part of the path, print a space without moving to a new line
                print(" ", end=" ")
        # After finishing a row, print a newline character to move to the next row
        print()
