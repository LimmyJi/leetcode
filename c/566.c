/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** matrixReshape(int** mat, int matSize, int* matColSize, int r, int c, int* returnSize, int** returnColumnSizes) {
    // if dimesnsions dont have same # of cells, return OG matrix, update returnsizes accordingly
    if (matSize * matColSize[0] != r * c){
        *returnSize = matSize;
        *returnColumnSizes = (int *)malloc(sizeof(int) * matSize);
        for (int i = 0; i < matSize; i++){
            (*returnColumnSizes)[i] = matColSize[0];
        }
        return mat;
    }
    // else, r, c will be new sizes
    *returnSize = r;
    *returnColumnSizes = (int *)malloc(sizeof(int) * r);
    int** ret = malloc(sizeof(int *) * r);
    for (int i = 0; i < r; i++){
        ret[i] = malloc(sizeof(int) * c);
        (*returnColumnSizes)[i] = c;
    }

    int col_old = 0;
    int row_old = 0;
    int col_new = 0;
    int row_new = 0;

    // fill in new matrix by going thru each cell of og matrix
    while (row_old < matSize && row_new < r){
        ret[row_new][col_new] = mat[row_old][col_old];
        col_new++;
        col_old++;
        // keep track of the position we are in either matrix, according to
        //   their sizes
        if (col_new >= c){
            col_new = 0;
            row_new++;
        }
        if (col_old >= matColSize[0]){
            col_old = 0;
            row_old++;
        }
    }
    return ret;
}
