class Solution {
public:
    int getCount(string source, char target){
        int count = 0;

        for (char c : source) {
            if (c == target) {
                count++;
            }
        }
        return count;

    }
    string validIPAddress(string queryIP) {
        vector<string> sectors;
        string sector;
        stringstream stream(queryIP);
        if (queryIP.empty()){
            return "Neither";
        }

        if (queryIP.find('.') != string::npos && getCount(queryIP, '.') == 3){
            while (getline(stream, sector, '.')){
                sectors.push_back(sector);
            }

            if (sectors.size() == 4){
                for (auto sec : sectors){
                    if (!(all_of( sec.begin(), sec.end(), ::isdigit))){
                        return "Neither";
                    }
                    if (sec.empty() || sec.size() > 4 || (sec.size() > 1 && sec[0] == '0') || stoi(sec) < 0 || stoi(sec) >255){
                        return "Neither";
                    }
                }
                return "IPv4";
            }
        }
        else if (queryIP.back() != ':' && getCount(queryIP, ':') == 7){
            while (getline(stream, sector, ':')){
                sectors.push_back(sector);
            }
            if (sectors.size() == 8){
                string validChars = "0123456789abcdefABCDEF";
                for (auto sec : sectors){
                    if (sec.size() > 4 || sec.empty()){
                        return "Neither";
                    }
                    if (!(all_of( sec.begin(), sec.end(), [validChars](char c) {return validChars.find(c) != string::npos;} ))){
                        return "Neither";
                    }
                }
                return "IPv6";
            }
        }
        return "Neither";
    }
};

// intuition
// 1) a way to split the numbers from the . or :
// 2) a way to check if all characters in a string is acording to a certain condition
// 1 can be done via the combination of find, and getline, find returns the total occurences of a sub string
// and getline will return the substring before a specified character
// 2 can be done via all_of, either by passing a function, or defining your own function by declaring variables inside all_of
// Due to the amount of edge cases in this question, I won't be listing all of them out and how I solved them