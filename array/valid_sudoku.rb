def is_valid_sudoku(board)
    hash = {}
    board.each_with_index do |row,i|
        row.each_with_index do |spot, j|
            if(spot != '.' && !hash[spot])
                hash[spot] = [[i,j]]
            elsif(spot != '.' && hash[spot])
                hash[spot].each do |ele|
                    if i == ele[0] || j == ele[1] || ((i/3) == (ele[0]/3) && (j/3) == (ele[1]/3))       
                        return false
                    end
                end
                hash[spot].push([i,j])
            end
        end
    end
    return true
end

test = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

is_valid_sudoku(test)