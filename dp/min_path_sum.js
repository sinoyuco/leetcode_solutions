var minPathSum = function(grid) {
    const h = grid.length
    const w = grid[0].length
    for(let i = 0; i<h; i++){
        for(let j = 0; j < w; j++){
            if(i==0 && j>0){
                grid[i][j] += grid[i][j-1]
            }
            else if(j==0 && i>0){
                grid[i][j] += grid[i-1][j]
            }else if(j>0 && i >0){
                grid[i][j] += Math.min(grid[i-1][j],grid[i][j-1])
            }
        }
    }
    return grid[h-1][w-1]
};