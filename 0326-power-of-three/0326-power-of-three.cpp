class Solution {
public:
    bool isPowerOfThree(int n) {
        if (n <= 0){
            return false;
        }
        double x = log10(n) / log10(3);
        double intCheck;
        return modf(x, &intCheck) == 0;
    }
};

// Just compare ceil and floor value of d
// return floor(d)==ceil(d);

// double x = 55.343;
// double int_part1;
// modf ( x, &int_part1 ) == 0.0

// either use floor compare with ceil or modf to perform modulos of 2 number, if 0 then int