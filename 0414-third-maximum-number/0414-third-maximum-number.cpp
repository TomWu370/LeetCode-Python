class Solution {
public:
    int thirdMax(vector<int>& nums) {
        // higher precision is required to handle edge cases for int precisions
        long first = LONG_MIN;
        long second = LONG_MIN;
        long third = LONG_MIN;

        for (int i: nums){
            // if i equal any existing value then skip to next iteration
            if (i == first || i == second || i == third){
                continue;
            }
            // if i is more than the first then propagate downwards
            if (i > first){
                third = second;
                second = first;
                first = i; 
            }
            // if i is more than second then propagate downwards if i is not equal to first
            else if (i > second && i != first){
                third = second;
                second = i;
            }
            // only update third if i is more than third but not the same as the previous values
            else if (i > third && i != second && i != first){
                third = i;
            }
        }
        // return third if not -infinity, otherwise return first
        return (third > LONG_MIN) ? third : first;
        
    }
};