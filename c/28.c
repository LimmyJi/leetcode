int strStr(char * haystack, char * needle){
    // get length of strings
    int len_haystack = 0;
    while (haystack[len_haystack] != '\0'){
        len_haystack++;
    }
    int len_needle = 0;
    while (needle[len_needle] != '\0'){
        len_needle++;
    }
    // for each possible starting point of needle in haystack,
    //   check if needle is there
    for (int i = 0; i <= len_haystack - len_needle; i++){
        int count = 0;
        for (int j = i; j < i + len_needle; j++){
            if (needle[j - i] != haystack[j]){
                break;
            }
            else{
                count++;
            }
            if (count == len_needle){
                return i;
            }
        }
    }
    return -1;
}
