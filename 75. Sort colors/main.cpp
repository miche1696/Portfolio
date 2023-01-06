#include <vector>

int main() {
    std::vector<int> nums = {2,0,1};

    int n = nums.size();
    int m = n-1, r = n-1, l=0, temp;
    
    while(true){
        if (r<=l) {return 0;}
        if (m<=l){
            if (nums[l]==1) {l++;}
            else if (nums[l]==2){
                while (nums[r]==2){r--;}
                if (r<=l) {return 1;}
                temp = nums[l];
                nums[l]=nums[r];
                nums[r]=temp;
                r--;
                l++;
            }
        }
        else{
            if (nums[l]==0) {l++;}
            else if (nums[l]==2){
                while (nums[r]==2){r--;}
                if (r<=l) {return 2;}
                temp = nums[l];
                nums[l]=nums[r];
                nums[r]=temp;
                r--;
            }
            else if (nums[l]==1){
                while (nums[m]!=0){m--;}
                if (m<0){return 3;} // da verificare
                temp = nums[l];
                nums[l]=nums[m];
                nums[m]=temp;
                l++;
            }
        }
    }
}
