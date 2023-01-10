class Solution {
public:
    bool canJump(vector<int>& nums) {
        int required = 1;
        int i;
        printf("%d", nums.size()-2);
        for (i = nums.size()-2 ; i>=0; i--){
            if (nums[i]>=required){
                required = 1;
            }
            else{
                required++;
            }
        }
        if(required==1){return true;}
        return false;
    }
};
