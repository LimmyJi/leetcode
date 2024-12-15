#include <stdbool.h>

// ascii lookup of capital letters
bool capital(char ch){
    if (65 <= ch && ch <= 90){
        return true;
    }
    return false;
}

// case 1, all capital in the word
bool case1(char * word, int len){
    for (int i = 0; i < len; i++){
        if (!(capital(word[i]))){
            return false;
        }
    }
    return true;
}

// case 2, none capital
bool case2(char * word, int len){
    for (int i = 0; i < len; i++){
        if (capital(word[i])){
            return false;
        }
    }
    return true;
}

// case 3, only 1st letter capital
bool case3(char * word, int len){
    if (!(capital(word[0]))){
        return false;
    }
    for (int i = 1; i < len; i++){
        if (capital(word[i])){
            return false;
        }
    }
    return true;
}

// true if one of the cases hold
bool detectCapitalUse(char * word){
    int len = strlen(word);
    return (case1(word, len) || case2(word, len) || case3(word, len));
}
