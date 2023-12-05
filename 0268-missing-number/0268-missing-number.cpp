class Solution {
public:
    int missingNumber(vector<int>& nums) {
        
        int sum = accumulate(nums.begin(), nums.end(), 0);
        int actualSum = (nums.size()*(nums.size()+1))/2;
        return actualSum-sum;
    } 
};

