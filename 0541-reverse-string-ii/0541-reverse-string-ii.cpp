class Solution {
public:
    string reverseStr(string s, int k) {
        int length = s.size();
        for (int i = 0; i<length; i += 2*k){
            if (i+k <= length){
            reverse(s.begin()+i, s.begin()+i+k);
            } else{
                reverse(s.begin()+i, s.end());
            }
        }
        return s;
    }
};