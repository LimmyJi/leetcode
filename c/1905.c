// will return 1 if (row, col) is part of a subisland
//   og determines if this is the original call or not
int sub(int** grid1, int grid1Size, int* grid1ColSize, int** grid2, int grid2Size, int* grid2ColSize, int row, int col, int og) {
    int ret = 1;
    if (grid2[row][col]){
        if (grid1[row][col]){
            // recurse in every direction if this is land in both grid1 and grid2
            grid2[row][col] = 0;  // mark the current cell as water, so we dont revisit in recursive calls
            int up;
            int down;
            int left;
            int right;
            if (row) {
                up = sub(grid1, grid1Size, grid1ColSize, grid2, grid2Size, grid2ColSize, row - 1, col, 0);
            }
            else {
                up = 1;
            }
            if (row < grid2Size - 1) {
                down = sub(grid1, grid1Size, grid1ColSize, grid2, grid2Size, grid2ColSize, row + 1, col, 0);
            }
            else {
                down = 1;
            }
            if (col) {
                left = sub(grid1, grid1Size, grid1ColSize, grid2, grid2Size, grid2ColSize, row, col - 1, 0);
            }
            else {
                left = 1;
            }
            if (col < *grid2ColSize - 1) {
                right = sub(grid1, grid1Size, grid1ColSize, grid2, grid2Size, grid2ColSize, row, col + 1, 0);
            }
            else {
                right = 1;
            }
            // the initial cell is part of a subisland iff all the recursive calls are
            ret = (down && up && left && right);
        }
        else {
            ret = 0;
        }
    }
    return ret;
}

int countSubIslands(int** grid1, int grid1Size, int* grid1ColSize, int** grid2, int grid2Size, int* grid2ColSize) {
    int ret = 0;
    for (int row = 0; row < grid2Size; row++){
        for (int col = 0; col < *grid2ColSize; col++){
            // if we find a potential subisland candidate, call our helper func
            if (grid2[row][col] && grid1[row][col]){
                ret = ret + sub(grid1, grid1Size, grid1ColSize, grid2, grid2Size, grid2ColSize, row, col, 1);
            }
        }
    }
    return ret;
}
