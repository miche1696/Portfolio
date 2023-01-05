class Solution {
public:

    bool recur(int i, int j, vector<vector<char>>& board, string word,int m, int n){
    int k=0,g=0;
    //printf("\nWord size = %d\t(i,j) = (%d,%d)",word.size(),i,j);
    if (word.size()==0) return true;
    if (j-1>=0 && board[i][j-1]==word[0]) // Left
    {
        //printf("LEFT word[0] %c",word[0]);
        board[i][j-1]='0';
        if(recur(i,j-1,board,word.substr(1),m,n)) {return true;}
        board[i][j-1]=word[0];
    }
    if (i+1<m && board[i+1][j]==word[0]) // Up
    {
        //printf("UP word[0] %c",word[0]);
        board[i+1][j]='0';
        if(recur(i+1,j,board,word.substr(1),m,n)) {return true;}
        board[i+1][j]=word[0];
    }
    if (j+1<n && board[i][j+1]==word[0]) // Right
    {
        //printf("RIGHT word[0] %c",word[0]);
        board[i][j+1]='0';
        if(recur(i,j+1,board,word.substr(1),m,n)) {return true;}
        board[i][j+1]=word[0];
    }
    if (i-1>=0 && board[i-1][j]==word[0]) // Down
    {
        //printf("DOWN word[0] %c",word[0]);
        board[i-1][j]='0';
        if(recur(i-1,j,board,word.substr(1),m,n)) {return true;}
        board[i-1][j]=word[0];
    }
    return false;
}

    bool exist(vector<vector<char>>& board, string word) {
        int i, j;
        int m = board.size();
        int n = board[0].size();
        for(i=0;i<m;i++)
        {
            for(j=0;j<n;j++)
            {
                if (board[i][j]==word[0])
                {
                    //printf("word[0] %c\nword.substr(1) %s",word[0],word.substr(1).c_str());
                    board[i][j]='0';
                    if (recur(i,j,board,word.substr(1),m,n)) {return true;}
                    board[i][j]=word[0];
                }
            }
        }
        return false;
    }
};

// "ABCCED"

// Z A B C C
// Z S F C S
// Z A B E E

