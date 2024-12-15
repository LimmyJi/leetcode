// abs val
int abs(int num){
    if (num < 0){
        return num * -1;
    }
    else{
        return num;
    }
}

// max
int max(int num1, int num2){
    if (num1 < num2){
        return num2;
    }
    else{
        return num1;
    }
}

int minimumAverageDifference(int* nums, int numsSize){
    // total
    long long int total = 0;
    for (int j = 0; j < numsSize; j++){
        total = total + nums[j];
    }
    // current = left sum, get right sum from total - left sum
    long long int current = nums[0];
    int lowest_index = 0;
    int lowest_avg_diff = abs(current - (total - current) / max((numsSize - 1), 1));
    // find index with min avg diff, using the left sum to calculate it
    for (int i = 1; i < numsSize; i++){
        current = current + nums[i];
        int candidate = abs(current / (i + 1) - (total - current) / max((numsSize - 1 - i), 1));
        if (candidate < lowest_avg_diff){
            lowest_index = i;
            lowest_avg_diff = candidate;
        }
    }
    return lowest_index;
}
