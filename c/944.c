int minDeletionSize(char ** strs, int strsSize){
    int ans = 0;
    int len = strlen(strs[0]);
    // for each col
    for (int i = 0; i < len; i++){
        char prev = strs[0][i];
        // check if col is sorted
        for (int j = 1; j < strsSize; j++){
            if (strs[j][i] < prev){
                ans++;  // increment ans if not sorted
                break;
            }
            prev = strs[j][i];
        }
    }
    return ans;
}
