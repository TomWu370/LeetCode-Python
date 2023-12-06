class Solution {
public:
    string addStrings(string num1, string num2) {
        string sum = "";
        int maxLength = max(num1.size(), num2.size());
        int carry = 0;
        int tempSum;
        int start1;
        int start2;
        for(int i = 0; i < maxLength; i++){
            start1 = num1.size() - i -1;
            start2 = num2.size() - i -1;
            if (start1 < 0){
                tempSum = num2[start2] + carry - '0';
            }
            else if (start2 < 0){
                tempSum = num1[start1] + carry - '0';
            }
            else{
                tempSum = num1[start1] + num2[start2] + carry - '0'*2;
            }
            if (carry > 0){
                carry = 0;
            }
            if (tempSum > 9){
                carry = tempSum / 10;
                tempSum %= 10;
            }
            sum += to_string(tempSum);
        }
        if (carry > 0){
            sum += to_string(carry);
        }
        reverse(sum.begin(), sum.end());
        return sum;  
    }
};

// do long addition
// however in c++ to a single letter in string is considered a char, and char represents ascii values
// to convert ascii to int, you would need to subtract from the ascii '0'
// intuition here is to start from the back to the front
// start1 and start2 will always point to the furtherest back value of a string regardless of length, then moves forward