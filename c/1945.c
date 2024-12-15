// sum(num) will return the sum of digits of num
int sum(int num){
    int ret = 0;
    while (num){
        ret = ret + num % 10;
        num = (num - num % 10) / 10;
    }
    return ret;
}

int getLucky(char* s, int k) {
    int ret = 0;
    // 1 + 2
    for (int i = 0; s[i] != '\0'; i++){
        ret = ret + sum(s[i] - 96);
    }
    // 3
    k = k - 1;
    while (k){
        ret = sum(ret);
        k = k - 1;
    }
    return ret;
}
