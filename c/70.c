int climbStairs(int n) {
    // base cases
    if (n == 1){
        return 1;
    }
    if (n == 2){
        return 2;
    }
    // 45 since by constraints, n <= 45
    int dp[45] = {};
    for (int i=0; i < 45; i++){
        dp[i] = 0;
    }
    dp[0] = 1;
    dp[1] = 2;
    // for the i-th step, we either take 1 step from step i - 1
    //   or 2 steps from step i - 2
    for (int i = 2; i < n; i++){
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    return dp[n - 1];
}
