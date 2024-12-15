/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* createTargetArray(int* nums, int numsSize, int* index, int indexSize, int* returnSize) {
    int* ret = malloc(numsSize * sizeof(int));
    // init to -1 to indicate index is empty
    for (int i = 0; i < numsSize; i++){
        ret[i] = -1;
    }
    *returnSize = numsSize;
    for (int i = 0; i < numsSize; i++){
        // if index is empty we will insert
        if (ret[index[i]] < 0){
            ret[index[i]] = nums[i];
        }
        else{
            // else shift existing entries over
            for (int j = numsSize - 1; j > index[i]; j--){
                ret[j] = ret[j - 1];
            }
            ret[index[i]] = nums[i];
        }
    }
    return ret;
}
