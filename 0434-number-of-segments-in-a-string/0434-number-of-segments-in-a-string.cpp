class Solution {
public:
    int countSegments(string s) {
        istringstream words(s);
        int count = 0;
        string word;
        while (words >> word){
            if (!word.empty()){
                count++;
            }
        }
        return count;
        
    }
};