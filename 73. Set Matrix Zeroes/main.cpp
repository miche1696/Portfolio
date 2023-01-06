class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int i,j;
        int n = matrix.size();
        int m = matrix[0].size();
        std::set<int> zeroColoumns;
        std::set<int> zeroRows;
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                if (matrix[i][j]==0){
                    zeroColoumns.insert(j);
                    zeroRows.insert(i);
                    }
                }
            }
            for (std::set<int>::iterator it=zeroColoumns.begin(); it!=zeroColoumns.end(); ++it){
                for (i=0; i<n;i++){
                    matrix[i][*it]=0;
                }
            }
            for (std::set<int>::iterator it=zeroRows.begin(); it!=zeroRows.end(); ++it){
                for (j=0; j<m;j++){
                    matrix[*it][j]=0;
                }
            }
        }
};