class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> ranges;
        string start = "";
        for (int i = 0; i < nums.size(); i++){
            if (start.empty()){
                start = to_string(nums[i]);
            }
            if (i == nums.size()-1 || nums[i+1] != nums[i]+1){
                if (to_string(nums[i]) != start){
                    string range = start+"->"+to_string(nums[i]);
                    ranges.push_back(range);
                }
                else{
                    ranges.push_back(start);
                }
                start = "";
            }
        }
        return ranges;

    }
};

