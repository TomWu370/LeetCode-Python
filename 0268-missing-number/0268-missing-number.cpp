class Solution {
public:
    int missingNumber(vector<int>& nums) {

        std::vector<int> integerList(nums.size()+1);

        // Use std::iota to generate the integer list
        std::iota(integerList.begin(), integerList.end(), 0);
        // difference only works with sorted lists
        std::sort(nums.begin(), nums.end());
        std::sort(integerList.begin(), integerList.end());
        std::vector<int> diff;

        std::set_symmetric_difference(nums.begin(), nums.end(), integerList.begin(), integerList.end(), 
        std::inserter(diff, diff.begin()));
        return diff[0];
    } 
};

