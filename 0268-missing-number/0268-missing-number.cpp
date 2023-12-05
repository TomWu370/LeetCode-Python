class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int size = nums.size();
        
        int sum = accumulate(nums.begin(), nums.end(), 0);
        int actualSum = (size*(size+1))/2;
        return actualSum-sum;
    } 
};

