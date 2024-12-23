int removeElement(int* nums, int numsSize, int val){
    if (numsSize == 0) {
        return 0;
    }
    // ret_pos will store the number of non val elements
    //   that we have come across
    int ret_pos;
    if (nums[0] == val){
        ret_pos = 0;
    } else {
        ret_pos = 1;
    }
    // it will also represent where we should insert the next non val
    //   element in nums
    for (int i = 1; i < numsSize; i++){
        if (nums[i] != val){
            nums[ret_pos] = nums[i];
            ret_pos++;
        }
    }
    return ret_pos;
}
