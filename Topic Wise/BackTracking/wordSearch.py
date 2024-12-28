# Word Search LC 79

# Given a 2D board and a word, find if the word exists in the grid.

board=[["A","B","C","E"],
       ["S","F","C","S"],
        ["A","D","E","E"]]
word="ABCCED"

def exist(board,word):
    rows,cols=len(board),len(board[0])
    path=set() # to keep track of visited cells(since we dont revisit cells set is used)

    # use dfs to search for the word
    def dfs(r,c,cur_char): # r is row, c is column, cur_char is the current character in the word
        if cur_char==len(word):
            return True
        
        if (r<0 or r>=rows or c<0 or c>=cols or word[cur_char]!=board[r][c] or (r,c) in path):
            return False # if the cell is out of bounds or the cell is already visited or the cell does not match the current character in the word
        
        path.add((r,c)) # add the cell to the path

        # check the neighbors
        res=(dfs(r+1,c,cur_char+1) or # top
             dfs(r-1,c,cur_char+1) or # bottom
            dfs(r,c+1,cur_char+1) or # right
            dfs(r,c-1,cur_char+1) # left
             )
        
        path.remove((r,c)) # remove the cell from the path

        return res
    
    for r in range(rows):
        for c in range(cols):
            if dfs(r,c,0) and board[r][c]==word[0]:
                return True
    return False

print(exist(board,word)) # True