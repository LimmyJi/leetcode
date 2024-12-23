int removeDuplicates(int* nums, int numsSize){
    // keep track of prev
    int prev = nums[0];
    // ret_pos will be the # of remaining unique elements
    int ret_pos = 1;
    // ret_pos will also keep track of where we should insert
    //   newly found unique elements
    for (int i = 1; i < numsSize; i++){
        if (nums[i] != prev){
            prev = nums[i];
            nums[ret_pos] = nums[i];
            ret_pos++;
        }
    }
    return ret_pos;
}
