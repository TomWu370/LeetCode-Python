class Solution {
public:
    bool isPowerOfFour(int n) {
        if (n <= 0){
            return false;
        }
        double x = log2(n) / log2(4);
        double intCheck;
        return modf(x, &intCheck) == 0;
    }
};

// method for power of three can be applied here as well, only need to modify the calculation of x, swapping log2(3) to log2(4)
// double is used for better precision