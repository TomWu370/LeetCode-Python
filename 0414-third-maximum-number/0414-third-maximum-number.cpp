class Solution {
public:
    int thirdMax(vector<int>& nums) {
        // higher precision is required to handle edge cases for int precisions
        double first = -std::numeric_limits<double>::infinity();
        double second = -std::numeric_limits<double>::infinity();
        double third = -std::numeric_limits<double>::infinity();

        for (int i: nums){
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
        return (third > -std::numeric_limits<double>::infinity()) ? third : first;
        
    }
};