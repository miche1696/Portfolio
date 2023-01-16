#include <map>

class Solution {
public:
  vector<int> twoSum(vector<int> &nums, int target) {
    std::map<int,int> values;
    std::map<int,int>::iterator it;
    std::vector<int> result;
    int i;

    for (i=0; i< nums.size();i++){
        it = values.find(target-nums[i]);
        if (it != values.end()){
            result.push_back(i);
            result.push_back(it->second);
            return result;
        }
        values[nums[i]]=i;
    }
    return result;
  }
};