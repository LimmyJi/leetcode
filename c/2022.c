/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** construct2DArray(int* original, int originalSize, int m, int n, int* returnSize, int** returnColumnSizes) {
    int** ret = malloc(sizeof(int*) * m);
    int* ColumnSizes = malloc(sizeof(int) * m);
    // if dims work
    if (m * n != originalSize){
        *returnSize = 0;
        return ret;
    }

    for (int i = 0; i < m; i++){
        ret[i] = malloc(sizeof(int) * n);
        ColumnSizes[i] = n;
    }
    // linearly go thru original array, copying to new 2d array
    for (int i = 0; i < originalSize; i++){
        ret[i / n][i % n] = original[i];
    }

    *returnSize = m;
    *returnColumnSizes = ColumnSizes;
    return ret;
}
