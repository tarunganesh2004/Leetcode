# Snakes and Ladders LC 909

from collections import deque


board = [
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 35, -1, -1, 13, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 15, -1, -1, -1, -1],
]

def snakesAndLadders(board):
    n=len(board)

    def getPos(pos):
        row= (pos - 1) // n
        col = (pos - 1) % n

        if row % 2 == 1:
            col = n - 1 - col
        return n - 1 - row, col
    
    visited=set()
    queue=deque([(1, 0)])  # (position, steps)
    while queue:
        pos,moves= queue.popleft()
        for i in range(1, 7):
            next_pos = pos + i
            if next_pos > n * n:
                continue
            
            r, c = getPos(next_pos)
            if board[r][c] != -1:
                next_pos = board[r][c]
            
            if next_pos == n * n:
                return moves + 1
            
            if next_pos not in visited:
                visited.add(next_pos)
                queue.append((next_pos, moves + 1))
    return -1  # If not reachable

print(snakesAndLadders(board))  # Output: 4