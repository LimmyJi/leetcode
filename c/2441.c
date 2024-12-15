// get abs val of a num
int abs(int num){
    if (num < 0){
        return -1 * num;
    }
    return num;
}

int findMaxK(int* nums, int numsSize) {
    // since nums[i] is in [-1000, 1000], create a map where
    //   map[i][0] indicates if -i has been found, and map[i][1] for +i
    int map[1000][2] = {};
    for (int i = 0; i < 1000; i++){
        map[i][0] = 0;
        map[i][1] = 0;
    }

    for (int i = 0; i < numsSize; i++){
        if (nums[i] < 0){
            map[abs(nums[i]) - 1][0] = 1;
        }
        else{
            map[abs(nums[i]) - 1][1] = 1;
        }
    }

    for (int i = 999; i >= 0; i--){
        if (map[i][0] && map[i][1]){
            return i + 1;
        }
    }
    return -1;
}
