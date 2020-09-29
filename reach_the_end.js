function reachTheEnd(grid, maxTime) {
    let count = 0;
    let x = 0;
    let y = 0;
    while ((grid[x + 1][y] || grid[x][y + 1]) && (grid[x + 1][y] === '.' || grid[x][y + 1] === '.')) {
        if (grid[x + 1][y] === '.') {
            x += 1;
        } else {
            y += 1;
        }
        count += 1;
    }
    console.log(x, y)
    if (x == grid.length - 1 && y == grid[2].length - 1 && count <= maxTime) {
        return 'Yes'
    } else {
        return 'No'
    }

}
