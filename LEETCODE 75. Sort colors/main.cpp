class Solution {
public:
    void sortColors(vector<int>& nums) {

        int n = nums.size();
        int r = n-1, l=0, temp;
        while(l<r){
            if(nums[l]==2){ 
                while (r>l && nums[r]==2){r--;} 
                temp=nums[l];
                nums[l]=nums[r];
                nums[r]=temp;
                r--;
            }
            l++;
        }
        l=0;
        while(l<r){
            if(nums[l]==1){
                while (r>l && nums[r]!=0){r--;} 
                temp=nums[l];
                nums[l]=nums[r];
                nums[r]=temp;
                r--;
            }
            l++;
        }       
    }  
};