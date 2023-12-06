class Solution {
public:
    int getSum(int a, int b) {
        return log(pow(2,a)*pow(2,b))/log(2);
    }
};


// intuition bit manipulation, continuously update a, by adding the 2 binary
// then move the carried over binary bit and continue the process until all carries are exhaussted, then return a

// intuition 2
// x^y * x^z = x^y+z
// make x to become 2
// 2^y * 2^z = 2^y+z
// y+z = log(result)/log(2)