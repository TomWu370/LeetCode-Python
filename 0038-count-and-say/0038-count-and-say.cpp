class Solution {
public:
    string countAndSay(int n) {
        string say = "1";
        vector<string> freq;
        string sayPart;
        
        for (int i = 0; i < n-1; i++){
            freq.clear();
            sayPart = "";
            for (auto num: say){
                if (sayPart.empty() || sayPart[0] == (num-'0')){
                    sayPart += (num-'0');
                }
                else{
                    freq.push_back(sayPart);
                    sayPart = (num-'0');
                }
            }
            if (!sayPart.empty()){
                freq.push_back(sayPart);
            }

            say = "";
            for (string fre: freq){
                say += to_string(fre.size()) + to_string(fre[0]);
            }
        }
        return say;
    }
};

// to convert char to string representation of int
// either subtract the char number from '0' char to get the appropriate ascii of the number
// or convert a slice of a string into a string, this will likely work for non numbers as well
