class Node:
    def __init__(self, vertex=0, distance=0) -> None:
        self.vertex = vertex
        self.distance = distance
    
    def __str__(self) -> str:
        return f'vertext: {self.vertex} | distance: {self.distance}'


def minimum_dice_throw(board, N):
    """board is an array containing steps, N is the total number of steps"""
    # The graph has N vertices. Mark all
    # the vertices as not visited
    visited = [0] * N

    queue = []

    visited[0] = True
    queue.append(Node(0, 0))

    node = Node()
    while len(queue) > 0:
        node = queue.pop(0)
        vertex = node.vertex

        # If front vertex is the destination
        # vertex, we are done
        if vertex == N - 1:
            break

        j = vertex + 1
        while j <= vertex + 6 and j < N:
            if visited[j] == 0:
                temp_node = Node()
                temp_node.distance = node.distance + 1
                visited[j] = True

                temp_node.vertex = board[j] if board[j] != -1 else j

                queue.append(temp_node)
            j += 1
    return node.distance


# driver code
N = 30
moves = [-1] * N

# Ladders
moves[2] = 21
moves[4] = 7
moves[10] = 25
moves[19] = 28

# Snakes
moves[26] = 0
moves[20] = 8
moves[16] = 3
moves[18] = 6

print("Min Dice throws required is {0}".format(minimum_dice_throw(moves, N)))