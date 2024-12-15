// return max of 2 nums
int max (int num1, int num2){
    if (num1 <= num2){
        return num2;
    }
    else{
        return num1;
    }
}

int clumsy (int n){
    if (n == 1 || n == 2){
        return n;
    }
    int ans = n * (n - 1) / (n - 2);
    n = n - 3;

    int op = 1;  // 1 = add, 2 = sub

    while (n > 0){
        if (op == 1){
            ans = ans + n;
            n--;
            op = 2;
        }
        // because of bedmas, we need to subtract (n * max(n - 1, 1) / max(n - 2, 1))
        //   we use max because in the case where n < 3, replace n - 1 or n - 2 with 1, so that
        //   multiplying/dividing does nothing
        else if (op == 2){
            ans = ans - (n * max(n - 1, 1) / max(n - 2, 1));
            n = n - 3;
            op = 1;
        }
    }
    return ans;
}
