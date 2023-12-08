class Solution {
public:
    int compress(vector<char>& chars) {
        string ans = "";
        char currChar = chars[0];
        int count = 0;
        
        for (auto c : chars){
            if (c == currChar){
                count ++;
            }
            else{
                ans += currChar;
                if (count > 1){
                    ans += to_string(count);
                }
                currChar = c;
                count = 1;
            }
        }
        ans += currChar;
        if (count >1){
            ans += to_string(count);
        }

        for (int i = 0; i < ans.size(); i++){
            chars[i] = ans[i];
        }
        chars.resize(ans.size());
        return chars.size();
        
    }
};

// see python for implementation details
// to do inplace vector replacing in c++ you simply reassign values
// to resize inplace, simply use .resize()