public class Solution
{
    public int IsPrefixOfWord(string sentence, string searchWord)
    {
        int length = searchWord.Length;
        int sentLength = sentence.Length;
        int curPos = 0;
        int searchWordPos = 0;
        int ret = 0;
        // go thru the sentance 1 char at a time
        while (curPos < sentLength)
        {
            // check if the cur char matches up with the search word
            char c = sentence[curPos];
            if (c == searchWord[searchWordPos])
            {
                searchWordPos = searchWordPos + 1;
                // if we found the search word
                if (searchWordPos >= length)
                {
                    return ret + 1;
                }
                curPos = curPos + 1;
            } 
            else 
            {
                // if we didnt match the search word, skip to after next space
                searchWordPos = 0;
                while (curPos < sentLength && sentence[curPos] != ' ')
                {
                    curPos = curPos + 1;
                }
                ret = ret + 1;
                if (curPos < sentLength){
                    curPos = curPos + 1;
                }
            }
        }
        return -1;
    }
}
