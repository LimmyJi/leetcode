// quicksort
void sort(int* nums, int numsSize){
    if (numsSize == 1 || numsSize == 0){
        return;
    }
    int *left = malloc(sizeof(int) * numsSize);
    int size_left = 0;
    int *right = malloc(sizeof(int) * numsSize);
    int size_right = 0;
    int pivot = nums[0];

    for (int i = 1; i < numsSize; i++){
        if (nums[i] <= pivot){
            left[size_left] = nums[i];
            size_left++;
        }
        else{
            right[size_right] = nums[i];
            size_right++;
        }
    }
    sort(left, size_left);
    sort(right, size_right);

    for (int i = 0; i < size_left; i++){
        nums[i] = left[i];
    }
    nums[size_left] = pivot;
    for (int i = size_left + 1; i < numsSize; i++){
        nums[i] = right[i - size_left - 1];
    }
    free(left);
    free(right);
}

int specialArray(int* nums, int numsSize) {
    // sort nums
    sort(nums, numsSize);
    int ret = numsSize;
    // start at numsSize, then decrease as we find elements greater than
    for (int i = 0; i < numsSize; i++){
        if (nums[i] >= ret && (i == 0 || nums[i-1] < ret)){
            return ret;
        }
        else{
            ret--;
        }
    }
    return -1;
}
