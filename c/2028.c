/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* missingRolls(int* rolls, int rollsSize, int mean, int n, int* returnSize) {
    int* ret = malloc(sizeof(int) * n);
    // get current total
    int total = 0;
    for (int i = 0; i < rollsSize; i++){
        total = total + rolls[i];
    }
    // and remaining
    int remain = mean * (n + rollsSize) - total;
    // if its possible
    if (remain >= n && remain <= n * 6){
        int base = remain / n;
        int extra = remain % n;
        for (int i = 0; i < n; i++){
            ret[i] = base;
            if (i < extra){
                ret[i] = ret[i] + 1;
            }
        }
        *returnSize = n;
        return ret;
    }
    else{
        *returnSize = 0;
        return ret;
    }
}
