class Solution {
public:
    int missingNumber(vector<int>& nums) {

        int expected = 0;
        std::sort(nums.begin(), nums.end());
        int length = nums.size();
        for (int i = 0; i < length; i++){
            if (nums[i] != expected){
                return expected;
            }
            expected++;
        }
        return expected;
    } 
};

