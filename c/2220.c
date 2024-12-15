int minBitFlips(int start, int goal) {
    int ret = 0;
    int cur = 1;
    // cur will be multiples of 2
    while (cur * 2 <= goal || cur * 2 <= start){
        cur = cur * 2;
    }
    while (1){
        if (!start && !goal){
            break;
        }
        // if start, goal are not both greater than cur
        //   or both less than eq to cur, then a bit needs to be
        ///  flipped
        if (start >= cur && goal < cur){
            start = start - cur;
            ret = ret + 1;
        }
        else if (start < cur && goal >= cur){
            goal = goal - cur;
            ret = ret + 1;
        }
        else if (start >= cur && goal >= cur){
            start = start - cur;
            goal = goal - cur;
        }
        cur = cur / 2;
    }
    return ret;
}
