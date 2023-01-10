class Solution {
public:
    void rec(int i, int j, int actLen, int n, vector<int> retVec, vector<int>& nums, vector<vector<int>>& retVal){
    if (actLen>=i) {
        retVal.push_back(retVec); 
        return;
    }
    for (;j<n; j++){
        retVec.push_back(nums[j]);
        rec(i, j+1, actLen+1, n, retVec, nums, retVal);
        retVec.pop_back();
    }
    return;
}
    vector<vector<int>> subsets(vector<int>& nums) {
        int i;
        int n = nums.size();
        vector<vector<int>> retVal;
        vector<int> retVec;
        for (i=0; i<=n; i++){
            rec(i, 0, 0, n, retVec, nums, retVal);
        }
        return retVal;
    }
};