#include <string.h>

class Solution {
public:
    bool isPalindrome(int l, int r, string s){
        for(;l<r;l++,r--){
            if(s[l]!=s[r]){return false;}
        }
        return true;
    }

    string longestPalindrome(string s) {
        int l = s.size(), m = l;
        int i;
        while(l>0){
            for(i=0; i+l-1<m;i++){
                if(isPalindrome(i, i+l-1, s)){
                    return s.substr(i,l);
                }
            }
            l--;
        }
        return s;
    }
};