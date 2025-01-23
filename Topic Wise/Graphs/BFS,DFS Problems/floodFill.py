# # Flood Fill LC 733
# You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill:

# Begin with the starting pixel and change its color to color.
# Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
# Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
# The process stops when there are no more adjacent pixels of the original color to update.
# Return the modified image after performing the flood fill.

image=[[1,1,1],[1,1,0],[1,0,1]]
sr=1
sc=1
newColor=2

# here dfs is better than bfs because we are changing the color of the pixel and then checking the neighbors of the pixel
def floodFill(image,sr,sc,newColor):
    dir=[[0,1],[1,0],[0,-1],[-1,0]]
    m=len(image)
    n=len(image[0])
    color=image[sr][sc]
    if color==newColor:
        return image
    def dfs(x,y):
        if x<0 or y<0 or x>=m or y>=n or image[x][y]!=color:
            return
        image[x][y]=newColor
        for d in dir:
            dfs(x+d[0],y+d[1])
    dfs(sr,sc)
    return image

print(floodFill(image,sr,sc,newColor))