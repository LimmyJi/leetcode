int findLUSlength(char * a, char * b){
    int lena = strlen(a);
    int lenb = strlen(b);

    // if one string is longer than the other,
    //   it in its entirety is not a common subseq of a and b
    if (lena > lenb){
        return lena;
    }
    if (lena < lenb){
        return lenb;
    }
    // if a and b have the same length
    if (strcmp(a, b) == 0){
        // if they are the same string, they dont have an uncommon subseq
        return -1;
    }
    return lena;
}
